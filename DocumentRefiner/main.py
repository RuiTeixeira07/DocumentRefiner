from DocumentRefiner.file.file import File
from DocumentRefiner.format.format import Format
from DocumentRefiner.file.model.extension import TEXT as TEXT_FILE_EXTENSION
from DocumentRefiner.file.model.extension import PORTABLE_DOCUMENT_FORMAT as PORTABLE_DOCUMENT_FORMAT_FILE_EXTENSION
from DocumentRefiner.file.model.extension import DOCX as DOCX_FILE_EXTENSION

recommended_document_data_path = f"../assets/DocumentData{TEXT_FILE_EXTENSION.value}"

class Main:
    @staticmethod
    def run() -> None:
        document_data = File(
            Format.request_file_path(
                "Document Data",
                [
                    TEXT_FILE_EXTENSION.value,
                    PORTABLE_DOCUMENT_FORMAT_FILE_EXTENSION.value,
                    DOCX_FILE_EXTENSION.value
                ],
                recommended_document_data_path)).read_file()

        for line in document_data:
            print(line)

if __name__ == '__main__':
    main = Main()
    main.run()