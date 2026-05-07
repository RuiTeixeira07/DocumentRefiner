from DocumentRefiner.resources.format.format import Format

class Refiner:
    @staticmethod
    def refine(
        data: str,
        remove_consecutive_whitespace_characters: bool = True) -> str:

        return Format.clean_text(data) if remove_consecutive_whitespace_characters else data