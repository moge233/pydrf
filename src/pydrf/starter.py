#! python3


from .textchart import StarterPerformanceData


class Starter:
    def __init__(self, data: StarterPerformanceData):
        self.data: StarterPerformanceData = data

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'Starter({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'Starter({ret[:-2]})'
