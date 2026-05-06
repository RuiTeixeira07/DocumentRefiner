import os

class Format:
    @staticmethod
    def request_file_path(file_name: str, file_extensions: list[str], recommended_file_path: str, must_exist: bool = True) -> str:
        normalized_file_extensions = tuple([file_extension.casefold() for file_extension in file_extensions])

        while True:
            file_path = input(f"Insert path to {file_name} (Recommended '{recommended_file_path}'): ").strip()

            if not file_path:
                file_path = recommended_file_path

            if not must_exist and file_path.casefold().endswith(normalized_file_extensions):
                return file_path.upper()

            if must_exist and file_path.casefold().endswith(normalized_file_extensions) and os.path.isfile(file_path):
                return file_path.upper()