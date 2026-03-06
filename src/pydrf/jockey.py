#! python3


class Jockey:
    def __init__(self, last_name: str, first_name: str, middle_name: str, apprentice_type: str, key: int):
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.middle_name: str = middle_name
        self.apprentice_type: str = apprentice_type
        self.key: int = key

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'Jockey({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'Jockey({ret[:-2]})'
