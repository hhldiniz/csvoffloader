import os.path
from typing import IO

from sources.base_source import BaseSource
from targets.base_target import BaseTarget


class FileSystemSource(BaseSource):
    def __init__(self, target: BaseTarget, path: [str, None] = None, file: [IO, None] = None):
        super().__init__(target)
        if not file:
            self.is_file = os.path.isfile(path)
            self.is_dir = os.path.isdir(path)
        else:
            self.is_file = True
            self.is_dir = False

    def consume(self):
        pass
