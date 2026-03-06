#! python3


import csv

from src.pydrf.textchart import ExoticWageringData, Header, RaceData, RecordType, StarterPerformanceData
from src.pydrf.race import Race
from src.pydrf.starter import Starter


class Chart:
    def __init__(self, header: Header, races: list[Race]):
        self.header: Header = header
        self.races: list[Race] = races

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'Chart({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'Chart({ret[:-2]})'

    @staticmethod
    def parse_chart(path: str) -> 'Chart | None':
        races: list[Race] = []
        exotic_wagering_data: list[ExoticWageringData] = []
        try:
            with open(path) as chart_file:
                header: Header | None
                reader = csv.reader(chart_file.readlines())
                for line in reader:
                    if line[0] == RecordType.HEADER:
                        header = Header.create(line)
                    elif line[0] == RecordType.RACE:
                        race_data: RaceData = RaceData.create(line)
                        races.append(Race(race_data, [], []))
                    elif line[0] == RecordType.STARTER:
                        starter_data: StarterPerformanceData = StarterPerformanceData.create(line)
                        races[starter_data.race_number - 1].add_starter(Starter(starter_data))
                    elif line[0] == RecordType.EXOTIC_WAGERING:
                        exotic_wagering_data.append(ExoticWageringData.create(line))
                        wager_data: ExoticWageringData = ExoticWageringData.create(line)
                        races[starter_data.race_number - 1].add_wager(wager_data)
                    elif line[0] == RecordType.ATTENDANCE:
                        pass
                    elif line[0] == RecordType.COMMENT:
                        pass
                    elif line[0] == RecordType.FOOTNOTE:
                        pass
                return Chart(
                    header,
                    races,
                )
        except FileNotFoundError as e:
            print(f'[{e}]: could not find {path}')
            return None
