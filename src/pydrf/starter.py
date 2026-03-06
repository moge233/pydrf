#! python3


from .textchart import StarterPerformanceData


class Starter:
    def __init__(self, data: StarterPerformanceData):
        self.data: StarterPerformanceData = data

        # Make the data more human readable/usable
        self.data.odds /= 100
        self.data.length_ahead_at_poc1 /= 100
        self.data.length_ahead_at_poc2 /= 100
        self.data.length_ahead_at_poc3 /= 100
        self.data.length_ahead_at_poc4 /= 100
        self.data.length_ahead_at_poc5 /= 100
        self.data.length_ahead_at_finish /= 100
        self.data.length_behind_at_poc1 /= 100
        self.data.length_behind_at_poc2 /= 100
        self.data.length_behind_at_poc3 /= 100
        self.data.length_behind_at_poc4 /= 100
        self.data.length_behind_at_poc5 /= 100
        self.data.length_behind_at_finish /= 100

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
