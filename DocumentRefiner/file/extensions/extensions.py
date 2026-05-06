import pypdf
from DocumentRefiner.file.model.extension import TEXT as TEXT_FILE_EXTENSION
from DocumentRefiner.file.model.extension import PORTABLE_DOCUMENT_FORMAT as PORTABLE_DOCUMENT_FORMAT_FILE_EXTENSION

read_mode = "r"

class FileExtensions:
    @staticmethod
    def handle_file(file_path: str) -> list[str]:
        if file_path.casefold().endswith(TEXT_FILE_EXTENSION.value.casefold()):
            return FileExtensions.__handle_text_file__(file_path)

        if file_path.casefold().endswith(PORTABLE_DOCUMENT_FORMAT_FILE_EXTENSION.value.casefold()):
            return FileExtensions.__handle_portable_document_format_file__(file_path)

        return []

    @staticmethod
    def __handle_text_file__(file_path: str) -> list[str]:
        with open(file_path, read_mode) as file:
            return file.readlines()

    @staticmethod
    def __handle_portable_document_format_file__(file_path: str) -> list[str]:
        reader = pypdf.PdfReader(file_path)

        return [page.extract_text() for page in reader.pages]