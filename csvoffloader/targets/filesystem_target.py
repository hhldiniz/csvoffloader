from csvoffloader.targets.base_target import BaseTarget


class FileSystemTarget(BaseTarget):
    async def offload(self, json_str: str):
        pass

