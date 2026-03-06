#! python3


class Jockey:
    def __init__(self, last_name: str, first_name: str, middle_name: str, apprentice_type: str, key: int):
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.middle_name: str = middle_name
        self.apprentice_type: str = apprentice_type
        self.key: int = key
