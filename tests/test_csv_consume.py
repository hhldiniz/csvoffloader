from unittest import IsolatedAsyncioTestCase

from csvoffloader.sources.filesystem_source import FileSystemSource
from csvoffloader.targets.filesystem_target import FileSystemTarget


class TestCSVConsume(IsolatedAsyncioTestCase):
    def __init__(self):
        super().__init__()
        self.file_system_source = FileSystemSource(FileSystemTarget())

    async def test_csv_folder_consumption(self):
        await self.file_system_source.consume()
