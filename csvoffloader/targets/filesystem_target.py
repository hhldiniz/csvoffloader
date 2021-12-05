import os.path

from csvoffloader.targets.base_target import BaseTarget


class FileSystemTarget(BaseTarget):
    def __init__(self, target_path: str = "../outputs", target_file_name: str = "output.json"):
        self.target_path = target_path
        self.target_file_name = target_file_name

    async def offload(self, json_str: str):
        if not os.path.exists(self.target_path):
            os.mkdir(self.target_path)
        with open(os.path.join(self.target_path, self.target_file_name), "w") as out_file:
            out_file.write(json_str)

