#! python3


class Owner:
    def __init__(self, last_name: str, first_name: str, middle_name: str):
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.middle_name: str = middle_name

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'Owner({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'Owner({ret[:-2]})'
