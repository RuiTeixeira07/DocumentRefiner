import os

text_file_extension = ".TXT"
read_mode = "r"

class File:
    def __init__(self: File, file_path: str) -> None:
        self.file_path = file_path

    def read_file(self: File) -> list[str]:
        if not self.file_path.casefold().endswith(text_file_extension.casefold()):
            raise ValueError("Invalid File: '{}'. Required Text file.".format(self.file_path))

        if not os.path.isfile(self.file_path):
            raise FileNotFoundError("File Not Found: '{}'.".format(self.file_path))

        with open(self.file_path, read_mode) as file:
            return file.readlines()