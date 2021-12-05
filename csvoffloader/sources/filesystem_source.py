import csv
import json
import os.path
from os import walk
from typing import IO

from csvoffloader.sources.base_source import BaseSource
from csvoffloader.targets.base_target import BaseTarget
from csvoffloader.utils.json_encoder import MyJsonEncoder


class FileSystemSource(BaseSource):
    def __init__(self, target: BaseTarget, path: [str, None] = None, file: [IO, None] = None):
        super().__init__(target)
        if not file:
            self.is_file = os.path.isfile(path)
            self.is_dir = os.path.isdir(path)
        else:
            self.is_file = True
            self.is_dir = False
        self.path = path

    async def consume(self):
        if self.is_dir:
            for (dir_path, dir_names, filenames) in walk(self.path):
                for name in filenames:
                    with open(name, mode="r") as csv_file:
                        await self.__offload_file(csv_file)
        elif self.is_file:
            with open(self.path, mode="r") as csv_file:
                await self.__offload_file(csv_file)
        else:
            raise Exception("Path is invalid")

    async def __offload_file(self, csv_file):
        csv_reader = csv.DictReader(csv_file)
        await self.target.offload(json.dumps(dict(list(csv_reader)[0]), cls=MyJsonEncoder))
