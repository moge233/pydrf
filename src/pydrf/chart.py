#! python3


import csv

from .textchart import (
    AttendanceAndHandleData,
    CommentsAndRaceOdditiesData,
    ExoticWageringData,
    FootNoteData,
    Header,
    RaceData,
    RecordType,
    StarterPerformanceData,
)
from .jockey import Jockey
from .race import Race
from .starter import Starter
from .trainer import Trainer


def _race_at(races: list[Race | None], race_number: int | None) -> Race | None:
    """The race with this number, or None if the card has no such race."""
    if race_number is None or not 1 <= race_number <= len(races):
        return None
    return races[race_number - 1]


class Chart:
    def __init__(
        self,
        header: Header,
        races: list[Race | None],
        attendance: list[AttendanceAndHandleData] | None = None
    ):
        self.header: Header = header
        self.races: list[Race | None] = races
        self.attendance: list[AttendanceAndHandleData] = attendance if attendance is not None else []

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
    def parse_chart(path: str) -> 'Chart':
        races: list[Race | None] = []
        exotic_wagering_data: list[ExoticWageringData] = []
        attendance: list[AttendanceAndHandleData] = []
        with open(path) as chart_file:
            header: Header | None = None
            reader = csv.reader(chart_file.readlines())
            for line in reader:
                if line[0] == RecordType.HEADER:
                    header = Header.create(line)
                elif line[0] == RecordType.RACE:
                    race_data: RaceData = RaceData.create(line)
                    while len(races) < race_data.race_number - 1:
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
                    wager_data: ExoticWageringData = ExoticWageringData.create(line)
                    exotic_wagering_data.append(wager_data)
                    race: Race | None = races[wager_data.race_number - 1]
                    if race:
                        race.add_wager(wager_data)
                elif line[0] == RecordType.ATTENDANCE:
                    attendance.append(AttendanceAndHandleData.create(line))
                elif line[0] == RecordType.COMMENT:
                    comment_data: CommentsAndRaceOdditiesData = CommentsAndRaceOdditiesData.create(line)
                    race = _race_at(races, comment_data.race_number)
                    if race:
                        race.add_comment(comment_data)
                elif line[0] == RecordType.FOOTNOTE:
                    footnote_data: FootNoteData = FootNoteData.create(line)
                    race = _race_at(races, footnote_data.race_number)
                    if race:
                        race.add_footnote(footnote_data)
            if header is None:
                raise ValueError(f'{path}: chart has no header (H) record')
            return Chart(
                header,
                races,
                attendance,
            )
