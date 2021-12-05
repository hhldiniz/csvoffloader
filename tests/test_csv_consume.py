from unittest import IsolatedAsyncioTestCase

from csvoffloader.sources.filesystem_source import FileSystemSource
from csvoffloader.targets.filesystem_target import FileSystemTarget


class TestCSVConsume(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.file_system_source = FileSystemSource(FileSystemTarget(), "./test_source_files/test_source.json")

    async def test_csv_folder_consumption(self):
        await self.file_system_source.consume()
