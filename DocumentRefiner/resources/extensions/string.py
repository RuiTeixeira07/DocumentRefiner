import re

carriage_return = "\r"
line_feed = "\n"
end_of_line = carriage_return + line_feed
two_consecutive_paragraphs = f"({carriage_return}|{line_feed}|{end_of_line}){{2,}}"

empty_line= 2 * line_feed

whitespace_character = " "
two_consecutive_whitespace_characters = f"[{whitespace_character}]{{2,}}"

blank_lines = f"[{whitespace_character}]+({carriage_return}|{line_feed}|{end_of_line})"

class StringExtensions:
    @staticmethod
    def clean_text(text: str) -> str:
        text = StringExtensions.remove_consecutive_whitespace_characters(text)
        text = StringExtensions.remove_blank_lines(text)
        text = StringExtensions.remove_consecutive_paragraphs(text)

        return text

    @staticmethod
    def remove_consecutive_paragraphs(text: str) -> str:
        return re.sub(two_consecutive_paragraphs, empty_line, text)

    @staticmethod
    def remove_blank_lines(text: str) -> str:
        return re.sub(blank_lines, line_feed, text)

    @staticmethod
    def remove_consecutive_whitespace_characters(text: str) -> str:
        return re.sub(two_consecutive_whitespace_characters, whitespace_character, text)