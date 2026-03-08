#! python3


from .jockey import Jockey
from .textchart import StarterPerformanceData
from .trainer import Trainer


class Starter:
    def __init__(self, data: StarterPerformanceData, jockey: Jockey, trainer: Trainer):
        self.name: str = data.horse_name
        self.foaling_date: str = data.horse_foaling_date
        self.sex: str = data.sex_of_horse
        self.color: str = data.color
        self.dams_name: str = data.dams_name
        self.dams_year_of_birth: str = data.dams_year_of_birth
        self.sires_name: str = data.sires_name
        self.sires_year_of_birth: str = data.sires_year_of_birth
        self.weight_carried: int = data.weight_carried
        self.weight: int = data.horse_weight
        self.medications: str = data.medications
        self.equipment: str = data.equipment
        self.earnings: int = data.earnings
        self.odds: float = data.odds
        self.coupled_flag: str = data.coupled_flag
        self.coupled_finish: str = data.coupled_finish
        self.favorite_indicator: str = data.favorite_indicator
        self.post_position: int = data.post_position
        self.program_number: str = data.program_number
        self.position_at_start: int = data.position_at_start
        self.position_at_poc1: int = data.position_at_poc1
        self.position_at_poc2: int = data.position_at_poc2
        self.position_at_poc3: int = data.position_at_poc3
        self.position_at_poc4: int = data.position_at_poc4
        self.position_at_poc5: int = data.position_at_poc5
        self.original_finish: int = data.original_finish
        self.official_finish: int = data.official_finish
        self.length_ahead_at_poc1: float = data.length_ahead_at_poc1
        self.length_ahead_at_poc2: float = data.length_ahead_at_poc2
        self.length_ahead_at_poc3: float = data.length_ahead_at_poc3
        self.length_ahead_at_poc4: float = data.length_ahead_at_poc4
        self.length_ahead_at_poc5: float = data.length_ahead_at_poc5
        self.length_ahead_at_finish: float = data.length_ahead_at_finish
        self.length_behind_at_poc1: float = data.length_behind_at_poc1
        self.length_behind_at_poc2: float = data.length_behind_at_poc2
        self.length_behind_at_poc3: float = data.length_behind_at_poc3
        self.length_behind_at_poc4: float = data.length_behind_at_poc4
        self.length_behind_at_poc5: float = data.length_behind_at_poc5
        self.length_behind_at_finish: float = data.length_behind_at_finish
        self.dead_heat_flag: str = data.dead_heat_flag
        self.claiming_price: float = data.horse_claiming_price
        self.short_comments: str = data.short_comments
        self.long_comments: str = data.long_comments
        self.win_payoff: float = data.win_payoff
        self.place_payoff: float = data.place_payoff
        self.show_payoff: float = data.show_payoff
        self.claimed_indicator: str = data.claimed_indicator
        self.scratch_reason_code: str = data.scratch_reason_code
        self.disqualification_indicator: str = data.disqualification_indicator
        self.disqualification_placing: int = data.disqualification_placing
        self.trouble_indicator: str = data.trouble_indicator
        self.corrected_weight_indicator: str = data.corrected_weight_indicator
        self.over_weight: int = data.over_weight
        self.speed_index: int = data.speed_index
        self.breeder_name: str = data.breeder_name
        self.jockey: Jockey = jockey
        self.trainer: Trainer = trainer

        # Make the data more human readable/usable
        self.odds /= 100
        self.length_ahead_at_poc1 /= 100
        self.length_ahead_at_poc2 /= 100
        self.length_ahead_at_poc3 /= 100
        self.length_ahead_at_poc4 /= 100
        self.length_ahead_at_poc5 /= 100
        self.length_ahead_at_finish /= 100
        self.length_behind_at_poc1 /= 100
        self.length_behind_at_poc2 /= 100
        self.length_behind_at_poc3 /= 100
        self.length_behind_at_poc4 /= 100
        self.length_behind_at_poc5 /= 100
        self.length_behind_at_finish /= 100

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
