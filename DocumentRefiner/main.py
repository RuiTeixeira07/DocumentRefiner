from DocumentRefiner.file.file import File
from DocumentRefiner.file.format.format import Format

text_file_extension = ".TXT"
recommended_document_data_path = f"../assets/DocumentData{text_file_extension}"

class Main:
    @staticmethod
    def run() -> None:
        document_data = File(
            Format.request_file_path(
                "Document Data",
                text_file_extension,
                recommended_document_data_path)).read_file()

        for line in document_data:
            print(line)

if __name__ == '__main__':
    main = Main()
    main.run()