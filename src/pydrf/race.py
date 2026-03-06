#! python3


from .textchart import ExoticWageringData, RaceData
from .starter import Starter


class Race:
    def __init__(self, data: RaceData, starters: list[Starter], wagering: list[ExoticWageringData]):
        self.data: RaceData = data
        self.starters: list[Starter] = starters
        self.wagering: list[ExoticWageringData] = wagering

    def add_starter(self, starter: Starter) -> None:
        self.starters.append(starter)

    def add_wager(self, wager: ExoticWageringData) -> None:
        self.wagering.append(wager)
