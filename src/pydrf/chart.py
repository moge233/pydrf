#! python3


import csv

from .textchart import ExoticWageringData, Header, RaceData, RecordType, StarterPerformanceData
from .jockey import Jockey
from .race import Race
from .starter import Starter
from .trainer import Trainer


class Chart:
    def __init__(self, header: Header, races: list[Race | None]):
        self.header: Header = header
        self.races: list[Race | None] = races

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
        races: list[Race | None] = []
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
                        if (race_data.race_number - 1) == len(races):
                            races.append(Race(race_data, [], []))
                        else:
                            races.append(None)
                            races.append(Race(race_data, [], []))
                    elif line[0] == RecordType.STARTER:
                        starter_data: StarterPerformanceData = StarterPerformanceData.create(line)
                        jockey: Jockey = Jockey(
                            starter_data.jockey_last_name,
                            starter_data.jockey_first_name,
                            starter_data.jockey_middle_name,
                            starter_data.apprentice_type,
                            starter_data.jockey_key
                        )
                        trainer: Trainer = Trainer(
                            starter_data.trainer_last_name,
                            starter_data.trainer_first_name,
                            starter_data.trainer_middle_name,
                            starter_data.trainer_key
                        )
                        race: Race | None = races[starter_data.race_number - 1]
                        if race:
                            race.add_starter(Starter(starter_data, jockey, trainer))
                    elif line[0] == RecordType.EXOTIC_WAGERING:
                        exotic_wagering_data.append(ExoticWageringData.create(line))
                        wager_data: ExoticWageringData = ExoticWageringData.create(line)
                        race: Race | None = races[starter_data.race_number - 1]
                        if race:
                            race.add_wager(wager_data)
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
