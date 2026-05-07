import re

whitespace_character = " "
two_consecutive_whitespace_characters = f"[{whitespace_character}]{{2,}}"

class StringExtensions:
    @staticmethod
    def clean_text(text: str) -> str:
        return StringExtensions.__remove_consecutive_whitespace_characters__(text)

    @staticmethod
    def __remove_consecutive_whitespace_characters__(text: str) -> str:
        return re.sub(two_consecutive_whitespace_characters, whitespace_character, text)