import os
from DocumentRefiner.file.extensions.extensions import FileExtensions
from DocumentRefiner.file.model.extension import TEXT as TEXT_FILE_EXTENSION
from DocumentRefiner.file.model.extension import PORTABLE_DOCUMENT_FORMAT as PORTABLE_DOCUMENT_FORMAT_FILE_EXTENSION

class File:
    def __init__(self: File, file_path: str) -> None:
        self.file_path = file_path

    def read_file(self: File) -> list[str]:
        if not self.file_path.casefold().endswith((
                TEXT_FILE_EXTENSION.value.casefold(),
                PORTABLE_DOCUMENT_FORMAT_FILE_EXTENSION.value.casefold())):
            raise ValueError(
                "Invalid File: '{}'. Required Text, or Portable Document Format (PDF) file.".format(self.file_path))

        if not os.path.isfile(self.file_path):
            raise FileNotFoundError("File Not Found: '{}'.".format(self.file_path))

        return FileExtensions.handle_file(self.file_path.casefold())
