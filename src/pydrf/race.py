#! python3


from .textchart import ExoticWageringData, RaceData
from .starter import Starter


class Race:
    def __init__(self, data: RaceData, starters: list[Starter], wagering: list[ExoticWageringData]):
        self.number: int = data.race_number
        self.breed_indicator: str = data.breed_indicator
        self.type: str = data.race_type
        self.restrictions: str = data.restrictions
        self.sex_restriction: str = data.sex_restriction
        self.age_restriction: str = data.age_restriction
        self.purse: int = data.purse
        self.minimum_claiming_price: int = data.minimum_claiming_price
        self.maximum_claiming_price: int = data.maximum_claiming_price
        self.about_distance_indicator: str = data.about_distance_indicator
        self.distance: float = data.distance / 10.0
        self.distance_unit: str = data.distance_unit
        self.surface: str = data.surface
        self.course_type: str = data.course_type
        self.field_size: int = data.number_of_horses
        self.grade: str = data.race_grade
        self.name: str = data.race_name
        self.abbreviated_name: str = data.abbreviated_race_name
        self.post_time: str = data.post_time
        self.next_off_time: str = data.next_race_off_time
        self.off_time: str = data.this_race_off_time
        self.chute_starts: str = data.chute_starts
        self.class_codes: str = data.race_class_codes
        self.track_condition: str = data.track_condition
        self.off_turf_indicator: str = data.off_turf_indicator
        self.track_variant: int = data.track_variant
        self.drf_speed_number: int = data.drf_speed_number
        # reserved
        self.wind_speed: int = data.wind_speed
        self.wind_direction: str = data.wind_direction
        self.temperature: int = data.race_temperature
        self.final_time: float = data.final_time
        self.fraction1: float = data.fraction1
        self.fraction2: float = data.fraction2
        self.fraction3: float = data.fraction3
        self.fraction4: float = data.fraction4
        self.fraction5: float = data.fraction5
        self.individual_time: float = data.individual_time
        self.timer_type: str = data.timer_type
        self.wps_pool: int = data.wps_pool
        self.start_description: str = data.start_description
        self.weather: str = data.weather
        self.temporary_rail_distance: int = data.temporary_rail_distance
        self.off_turf_distance_change_flag: str = data.off_turf_distance_change_flag
        self.official_indicator: str = data.official_indicator
        self.starters: list[Starter] = starters
        self.wagering: list[ExoticWageringData] = wagering

    def __str__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'Race({ret[:-2]})'

    def __repr__(self):
        ret = ''
        for k, v in vars(self).items():
            ret += f'{k}={v}, '
        return f'Race({ret[:-2]})'

    def add_starter(self, starter: Starter) -> None:
        self.starters.append(starter)

    def add_wager(self, wager: ExoticWageringData) -> None:
        self.wagering.append(wager)
