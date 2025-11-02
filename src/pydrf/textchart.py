#! python3


from dataclasses import dataclass
from enum import Enum
from math import trunc


class RecordType(Enum):
    HEADER = 'H'
    RACE = 'R'
    STARTER = 'S'
    EXOTIC_WAGERING = 'E'
    ATTENDANCE = 'A'
    COMMENT = 'C'
    FOOTNOTE = 'F'

    def __eq__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value == other.value
        elif other.__class__ is str:
            return self.value == other
        return NotImplemented


class BreedIndicator(Enum):
    THOROUGHBRED = 'TB'
    QUARTER_HORSE = 'QH'
    ARABIAN = 'AR'
    PAINT = 'PT'
    MIXED_BREEDS = 'MX'

    def __eq__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value == other.value
        elif other.__class__ is str:
            return self.value == other
        return NotImplemented


class RestrictionCodes(Enum):
    AUCTION = 'A'
    RESTRICTED = 'R'
    STATE_BRED = 'S'

    def __eq__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value == other.value
        elif other.__class__ is str:
            return self.value == other
        return NotImplemented


class SexRestrictions(Enum):
    OPEN = ''
    CG = 'A'
    FM = 'B'
    C = 'C'
    CF = 'D'
    FG = 'E'
    G = 'G'
    H = 'H'
    M = 'M'

    def __eq__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value == other.value
        elif other.__class__ is str:
            return self.value == other
        return NotImplemented


class SurfaceCodes(Enum):
    DIRT = 'D'
    EQUITRACK = 'E'
    TURF = 'T'

    def __eq__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value == other.value
        elif other.__class__ is str:
            return self.value == other
        return NotImplemented


class CourseCodes(Enum):
    ALL_WEATHER_TRAINING = 'A'
    DIRT = 'D'
    ALL_WEATHER_TRACK = 'E'
    DIRT_TRAINING = 'F'
    INNER_TRACK = 'N'
    WOOD_CHIPS = 'W'
    TIMBER = 'B'
    DOWNHILL_TURF = 'C'
    TURF_TRAINING = 'G'
    INNER_TURF = 'I'
    JUMP = 'J'
    HURDLE = 'M'
    OUTER_TURF = 'O'
    STEEPLECHASE = 'S'
    TURF = 'T'
    HUNT_ON_TURF = 'U'

    def __eq__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value == other.value
        elif other.__class__ is str:
            return self.value == other
        return NotImplemented


class Index(Enum):
    pass

    def __eq__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented

    def __gt__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __lt__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def __gte__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __lte__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented


class HeaderIndex(Index):
    RECORD_TYPE_INDEX = 0
    COUNTRY_CODE_INDEX = 1
    TRACK_CODE_INDEX = 2
    RACE_DATE_INDEX = 3
    NUMBER_OF_RACES_INDEX = 4
    DAY_EVENING_FLAG_INDEX = 5
    SENDING_TRACK_INDEX = 6


class RaceDataIndex(Index):
    RECORD_TYPE_INDEX = 0
    RACE_NUMBER_INDEX = 1
    BREED_INDICATOR_INDEX = 2
    RACE_TYPE_INDEX = 3
    RESTRICTIONS_INDEX = 4
    SEX_RESTRICTION_INDEX = 5
    AGE_RESTRICTION_INDEX = 6
    DIVISION_INDEX = 7
    PURSE_USA_INDEX = 8
    REVERTS_MONEY_INDEX = 9
    AVAILABLE_MONEY_INDEX = 10
    PAID_TO_OTHERS_INDEX = 11
    ADDED_GUARANTEED_FLAG_INDEX = 12
    ADDED_MONEY_INDEX = 13
    INCLUDES1_TYPE_INDEX = 14
    INCLUDES1_MONEY_USA_INDEX = 15
    INCLUDES2_TYPE_INDEX = 16
    INCLUDES2_MONEY_USA_INDEX = 17
    INCLUDES3_TYPE_INDEX = 18
    INCLUDES3_MONEY_USA_INDEX = 19
    PLUS1_TYPE_INDEX = 20
    PLUS1_MONEY_USA_INDEX = 21
    PLUS2_TYPE_INDEX = 22
    PLUS2_MONEY_USA_INDEX = 23
    PLUS3_TYPE_INDEX = 24
    PLUS3_MONEY_USA_INDEX = 25
    MINIMUM_CLAIMING_PRICE_USA_INDEX = 26
    MAXIMUM_CLAIMING_PRICE_USA_INDEX = 27
    ABOUT_DISTANCE_INDICATOR_INDEX = 28
    DISTANCE_INDEX = 29
    DISTANCE_UNIT_INDEX = 30
    SURFACE_INDEX = 31
    COURSE_TYPE_INDEX = 32
    NUMBER_OF_HORSES_INDEX = 33
    RACE_GRADE_INDEX = 34
    RACE_NAME_INDEX = 35
    ABBREVIATED_RACE_NAME_INDEX = 36
    POST_TIME_INDEX = 37
    NEXT_RACE_OFF_TIME_INDEX = 38
    OFF_TIME_FOR_THIS_RACE_INDEX = 39
    CHUTE_STARTS_INDEX = 40
    RACE_CLASS_CODES_INDEX = 41
    TRACK_CONDITION_INDEX = 42
    OFF_TURF_INDICATOR_INDEX = 43
    TRACK_VARIANT_INDEX = 44
    DRF_SPEED_NUMBER_INDEX = 45
    # FOR FUTURE USE = 46
    WIND_SPEED_INDEX = 47
    WIND_DIRECTION_INDEX = 48
    RACE_TEMPERATURE_INDEX = 49
    FINAL_TIME_INDEX = 50
    FRACTION1_INDEX = 51
    FRACTION2_INDEX = 52
    FRACTION3_INDEX = 53
    FRACTION4_INDEX = 54
    FRACTION5_INDEX = 55
    INDIVIDUAL_TIME_INDEX = 56
    TIMER_TYPE_INDEX = 57
    WPS_POOL_INDEX = 58
    START_DESCRIPTION_INDEX = 59
    WEATHER_INDEX = 60
    TEMPORARY_RAIL_DISTANCE_INDEX = 61
    OFF_TURF_DISTANCE_CHANGE_FLAG_INDEX = 62
    OFFICIAL_INDICATOR_INDEX = 63


class ExoticWageringDataIndex(Index):
    RECORD_TYPE_INDEX = 0
    RACE_NUMBER_INDEX = 1
    WAGER_TYPE_INDEX = 2
    WAGERING_INDEX = 3
    WINNING_INDEX = 4
    MINIMUM_INDEX = 5
    POOL_TOTAL_INDEX = 6
    PAYOFF_AMOUNT_INDEX = 7
    CARRYOVER_INDEX = 8


class AttendanceAndHandleDataIndex(Index):
    RECORD_TYPE_INDEX = 0
    RACE_NUMBER_INDEX = 1
    LOCATION_TYPE_INDEX = 2
    LOCATION_INDEX = 3
    ATTENDANCE_INDEX = 4
    HANDLE_INDEX = 5
    # FOR FUTURE USE = 6
    # FOR FUTURE USE = 7


class CommentsAndRaceOdditiesDataIndex(Index):
    RECORD_TYPE_INDEX = 0
    RACE_NUMBER_INDEX = 1
    RESULT_COUNTRY_CODE_INDEX = 2
    TRACK_CODE_INDEX = 3
    RACE_DATE_INDEX = 4
    RESULT_RACE_NUMBER_INDEX = 5
    RESULT_DAY_EVENING_FLAG_INDEX = 6
    COMMENT_TYPE_INDEX = 7
    COMMENT_TEXT_INDEX = 8


class FootNotesIndex(Index):
    RECORD_TYPE_INDEX = 0
    RACE_NUMBER_INDEX = 1
    FOOT_NOTE_SEQUENCE_NUMBER_INDEX = 2
    FOOT_NOTE_TEXT_INDEX = 3


class StarterPerformanceDataIndex(Index):
    RECORD_TYPE_INDEX = 0
    RACE_NUMBER_INDEX = 1
    HORSE_KEY_INDEX = 2
    HORSE_NAME_INDEX = 3
    HORSE_FOALING_DATE_INDEX = 4
    AREA_FOALED_INDEX = 5
    BREED_OF_HORSE_INDEX = 6
    SEX_OF_HORSE_INDEX = 7
    COLOR_INDEX = 8
    DAMS_NAME_INDEX = 9
    DAMS_YEAR_OF_BIRTH_INDEX = 10
    DAMS_BREED_TYPE_INDEX = 11
    SIRES_NAME_INDEX = 12
    SIRES_YEAR_OF_BIRTH_INDEX = 13
    SIRES_BREED_TYPE_INDEX = 14
    BROODMARES_SIRES_NAME_INDEX = 15
    BROODMARES_SIRES_YEAR_OF_BIRTH_INDEX = 16
    BROODMARES_SIRES_BREED_TYPE_INDEX = 17
    SIRES_SIRES_NAME_INDEX = 18
    SIRES_SIRES_YEAR_OF_BIRTH_INDEX = 19
    SIRES_SIRES_BREED_TYPE_INDEX = 20
    WEIGHT_CARRIED_INDEX = 21
    HORSE_WEIGHT_INDEX = 22
    MEDICATIONS_INDEX = 23
    EQUIPMENT_INDEX = 24
    EARNINGS_USA_INDEX = 25
    JOCKEYS_LAST_NAME_INDEX = 26
    JOCKEYS_FIRST_NAME_INDEX = 27
    JOCKEYS_MIDDLE_NAME_INDEX = 28
    APPRENTICE_TYPE_INDEX = 29
    TRAINERS_LAST_NAME_INDEX = 30
    TRAINERS_FIRST_NAME_INDEX = 31
    TRAINERS_MIDDLE_NAME_INDEX = 32
    OWNERS_LAST_NAME_INDEX = 33
    OWNERS_FIRST_NAME_INDEX = 34
    OWNERS_MIDDLE_NAME_INDEX = 35
    ODDS_INDEX = 36
    NONBETTING_INDICATOR_INDEX = 37
    COUPLED_FLAG_INDEX = 38
    COUPLED_FINISH_INDEX = 39
    FAVORITE_INDICATOR_INDEX = 40
    POST_POSITION_INDEX = 41
    PROGRAM_NUMBER_INDEX = 42
    POSITION_AT_START_INDEX = 43
    POSITION_AT_POC1_INDEX = 44
    POSITION_AT_POC2_INDEX = 45
    POSITION_AT_POC3_INDEX = 46
    POSITION_AT_POC4_INDEX = 47
    POSITION_AT_POC5_INDEX = 48
    ORIGINAL_FINISH_INDEX = 49
    OFFICIAL_FINISH_INDEX = 50
    LENGTH_AHEAD_AT_POC1_INDEX = 51
    LENGTH_AHEAD_AT_POC2_INDEX = 52
    LENGTH_AHEAD_AT_POC3_INDEX = 53
    LENGTH_AHEAD_AT_POC4_INDEX = 54
    LENGTH_AHEAD_AT_POC5_INDEX = 55
    LENGTH_AHEAD_AT_FINISH_INDEX = 56
    LENGTH_BEHIND_AT_POC1_INDEX = 57
    LENGTH_BEHIND_AT_POC2_INDEX = 58
    LENGTH_BEHIND_AT_POC3_INDEX = 59
    LENGTH_BEHIND_AT_POC4_INDEX = 60
    LENGTH_BEHIND_AT_POC5_INDEX = 61
    LENGTH_BEHIND_AT_FINISH_INDEX = 62
    DEAD_HEAT_FLAG_INDEX = 63
    INDIVIDUAL_HORSE_CLAIMING_PRICE_INDEX = 64
    SHORT_COMMENTS_INDEX = 65
    LONG_COMMENTS_INDEX = 66
    WIN_PAYOFF_INDEX = 67
    PLACE_PAYOFF_INDEX = 68
    SHOW_PAYOFF_INDEX = 69
    CLAIMED_INDICATOR_INDEX = 70
    CLAIMING_TRAINER_KEY_INDEX = 71
    CLAIMING_TRAINER_TYPE_INDEX = 72
    CLAIMING_TRAINER_LAST_NAME_INDEX = 73
    CLAIMING_TRAINER_FIRST_NAME_INDEX = 74
    CLAIMING_TRAINER_MIDDLE_NAME_INDEX = 75
    CLAIMING_OWNER_KEY_INDEX = 76
    CLAIMING_OWNER_TYPE_INDEX = 77
    CLAIMING_OWNER_LAST_NAME_INDEX = 78
    CLAIMING_OWNER_FIRST_NAME_INDEX = 79
    CLAIMING_OWNER_MIDDLE_NAME_INDEX = 80
    SCRATCH_REASON_CODE_INDEX = 81
    DISQUALIFICATION_INDICATOR_INDEX = 82
    DISQUALIFICATION_PLACING_INDEX = 83
    TROUBLE_INDICATOR_INDEX = 84
    CORRECTED_WEIGHT_INDICATOR_INDEX = 85
    OVER_WEIGHT_INDEX = 86
    INDIVIDUAL_HORSE_TIME_INDEX = 87
    SPEED_INDEX = 88
    BREEDER_NAME_INDEX = 89
    JOCKEY_KEY_INDEX = 90
    TRAINER_KEY_INDEX = 91


def try_get_str(row: list[str], index: Index) -> str:
    try:
        return row[index.value].rstrip()
    except ValueError:
        return ''


def try_get_int(row: list[str], index: Index) -> int:
    try:
        return int(row[index.value].rstrip())
    except ValueError:
        return int(0)


def try_get_float(row: list[str], index: Index) -> float:
    try:
        return float(row[index.value].rstrip())
    except ValueError:
        return float('nan')


def final_time_to_seconds(final_time: float) -> float:
    minutes: float = trunc(final_time / 100)
    return round(minutes * 60 + final_time - minutes * 100, 2)


def fraction_to_seconds(fraction: float) -> float:
    minutes: float = trunc(fraction / 10000)
    return round(minutes * 60 + fraction / 100 - minutes * 100, 2)


@dataclass
class Header:
    country_code: str
    track_code: str
    race_date: str
    number_of_races: int
    time_flag: str
    sending_track: str

    @staticmethod
    def create(row: list[str]) -> 'Header':
        return Header(
            try_get_str(row, HeaderIndex.COUNTRY_CODE_INDEX),
            try_get_str(row, HeaderIndex.TRACK_CODE_INDEX),
            try_get_str(row, HeaderIndex.RACE_DATE_INDEX),
            try_get_int(row, HeaderIndex.NUMBER_OF_RACES_INDEX),
            try_get_str(row, HeaderIndex.DAY_EVENING_FLAG_INDEX),
            try_get_str(row, HeaderIndex.SENDING_TRACK_INDEX)
        )


@dataclass
class RaceData:
    race_number: int
    breed_indicator: str
    race_type: str
    restrictions: str
    sex_restriction: str
    age_restriction: str
    division: str
    purse: int
    reverts_money: int
    available_money: int
    paid_to_others: int
    guaranteed_flag: str
    added_money: int
    includes_money_type1: str
    includes_money1: int
    includes_money_type2: str
    includes_money2: int
    includes_money_type3: str
    includes_money3: int
    plus_money_type1: str
    plus_money1: int
    plus_money_type2: str
    plus_money2: int
    plus_money_type3: str
    plus_money3: int
    minimum_claiming_price: int
    maximum_claiming_price: int
    about_distance_indicator: str
    distance: int
    distance_unit: str
    surface: str
    course_type: str
    number_of_horses: int
    race_grade: str
    race_name: str
    abbreviated_race_name: str
    post_time: str
    next_race_off_time: str
    this_race_off_time: str
    chute_starts: str
    race_class_codes: str
    track_condition: str
    off_turf_indicator: str
    track_variant: int
    drf_speed_number: int
    # reserved
    wind_speed: int
    wind_direction: str
    race_temperature: int
    final_time: float
    fraction1: float
    fraction2: float
    fraction3: float
    fraction4: float
    fraction5: float
    individual_time: float
    timer_type: str
    wps_pool: int
    start_description: str
    weather: str
    temporary_rail_distance: int
    off_turf_distance_change_flag: str
    official_indicator: str

    @staticmethod
    def create(row: list[str]) -> 'RaceData':
        return RaceData(
            try_get_int(row, RaceDataIndex.RACE_NUMBER_INDEX),
            try_get_str(row, RaceDataIndex.BREED_INDICATOR_INDEX),
            try_get_str(row, RaceDataIndex.RACE_TYPE_INDEX),
            try_get_str(row, RaceDataIndex.RESTRICTIONS_INDEX),
            try_get_str(row, RaceDataIndex.SEX_RESTRICTION_INDEX),
            try_get_str(row, RaceDataIndex.AGE_RESTRICTION_INDEX),
            try_get_str(row, RaceDataIndex.DIVISION_INDEX),
            try_get_int(row, RaceDataIndex.PURSE_USA_INDEX),
            try_get_int(row, RaceDataIndex.REVERTS_MONEY_INDEX),
            try_get_int(row, RaceDataIndex.AVAILABLE_MONEY_INDEX),
            try_get_int(row, RaceDataIndex.PAID_TO_OTHERS_INDEX),
            try_get_str(row, RaceDataIndex.ADDED_GUARANTEED_FLAG_INDEX),
            try_get_int(row, RaceDataIndex.ADDED_MONEY_INDEX),
            try_get_str(row, RaceDataIndex.INCLUDES1_TYPE_INDEX),
            try_get_int(row, RaceDataIndex.INCLUDES1_MONEY_USA_INDEX),
            try_get_str(row, RaceDataIndex.INCLUDES2_TYPE_INDEX),
            try_get_int(row, RaceDataIndex.INCLUDES2_MONEY_USA_INDEX),
            try_get_str(row, RaceDataIndex.INCLUDES3_TYPE_INDEX),
            try_get_int(row, RaceDataIndex.INCLUDES3_MONEY_USA_INDEX),
            try_get_str(row, RaceDataIndex.PLUS1_TYPE_INDEX),
            try_get_int(row, RaceDataIndex.PLUS1_MONEY_USA_INDEX),
            try_get_str(row, RaceDataIndex.PLUS2_TYPE_INDEX),
            try_get_int(row, RaceDataIndex.PLUS2_MONEY_USA_INDEX),
            try_get_str(row, RaceDataIndex.PLUS3_TYPE_INDEX),
            try_get_int(row, RaceDataIndex.PLUS3_MONEY_USA_INDEX),
            try_get_int(row, RaceDataIndex.MINIMUM_CLAIMING_PRICE_USA_INDEX),
            try_get_int(row, RaceDataIndex.MAXIMUM_CLAIMING_PRICE_USA_INDEX),
            try_get_str(row, RaceDataIndex.ABOUT_DISTANCE_INDICATOR_INDEX),
            try_get_int(row, RaceDataIndex.DISTANCE_INDEX),
            try_get_str(row, RaceDataIndex.DISTANCE_UNIT_INDEX),
            try_get_str(row, RaceDataIndex.SURFACE_INDEX),
            try_get_str(row, RaceDataIndex.COURSE_TYPE_INDEX),
            try_get_int(row, RaceDataIndex.NUMBER_OF_HORSES_INDEX),
            try_get_str(row, RaceDataIndex.RACE_GRADE_INDEX),
            try_get_str(row, RaceDataIndex.RACE_NAME_INDEX),
            try_get_str(row, RaceDataIndex.ABBREVIATED_RACE_NAME_INDEX),
            try_get_str(row, RaceDataIndex.POST_TIME_INDEX),
            try_get_str(row, RaceDataIndex.NEXT_RACE_OFF_TIME_INDEX),
            try_get_str(row, RaceDataIndex.OFF_TIME_FOR_THIS_RACE_INDEX),
            try_get_str(row, RaceDataIndex.CHUTE_STARTS_INDEX),
            try_get_str(row, RaceDataIndex.RACE_CLASS_CODES_INDEX),
            try_get_str(row, RaceDataIndex.TRACK_CONDITION_INDEX),
            try_get_str(row, RaceDataIndex.OFF_TURF_INDICATOR_INDEX),
            try_get_int(row, RaceDataIndex.TRACK_VARIANT_INDEX),
            try_get_int(row, RaceDataIndex.DRF_SPEED_NUMBER_INDEX),
            try_get_int(row, RaceDataIndex.WIND_SPEED_INDEX),
            try_get_str(row, RaceDataIndex.WIND_DIRECTION_INDEX),
            try_get_int(row, RaceDataIndex.RACE_TEMPERATURE_INDEX),
            final_time_to_seconds(try_get_float(row, RaceDataIndex.FINAL_TIME_INDEX)),
            fraction_to_seconds(try_get_float(row, RaceDataIndex.FRACTION1_INDEX)),
            fraction_to_seconds(try_get_float(row, RaceDataIndex.FRACTION2_INDEX)),
            fraction_to_seconds(try_get_float(row, RaceDataIndex.FRACTION3_INDEX)),
            fraction_to_seconds(try_get_float(row, RaceDataIndex.FRACTION4_INDEX)),
            fraction_to_seconds(try_get_float(row, RaceDataIndex.FRACTION5_INDEX)),
            try_get_float(row, RaceDataIndex.INDIVIDUAL_TIME_INDEX),
            try_get_str(row, RaceDataIndex.TIMER_TYPE_INDEX),
            try_get_int(row, RaceDataIndex.WPS_POOL_INDEX),
            try_get_str(row, RaceDataIndex.START_DESCRIPTION_INDEX),
            try_get_str(row, RaceDataIndex.WEATHER_INDEX),
            try_get_int(row, RaceDataIndex.TEMPORARY_RAIL_DISTANCE_INDEX),
            try_get_str(row, RaceDataIndex.OFF_TURF_DISTANCE_CHANGE_FLAG_INDEX),
            try_get_str(row, RaceDataIndex.OFFICIAL_INDICATOR_INDEX)
        )


@dataclass
class ExoticWageringData:
    race_number: int
    wager_type: str
    wagering: int
    winning: str
    minimum: int
    pool_total: float
    payoff: float
    carryover: float

    @staticmethod
    def create(row: list[str]) -> 'ExoticWageringData':
        return ExoticWageringData(
            try_get_int(row, ExoticWageringDataIndex.RACE_NUMBER_INDEX),
            try_get_str(row, ExoticWageringDataIndex.WAGER_TYPE_INDEX),
            try_get_int(row, ExoticWageringDataIndex.WAGERING_INDEX),
            try_get_str(row, ExoticWageringDataIndex.WINNING_INDEX),
            try_get_int(row, ExoticWageringDataIndex.MINIMUM_INDEX),
            try_get_float(row, ExoticWageringDataIndex.POOL_TOTAL_INDEX),
            try_get_float(row, ExoticWageringDataIndex.PAYOFF_AMOUNT_INDEX),
            try_get_float(row, ExoticWageringDataIndex.CARRYOVER_INDEX)
        )


@dataclass
class AttendanceAndHandleData:
    race_number: int
    location_type: str
    location: str
    attendance: int
    handle: float

    @staticmethod
    def create(row: list[str]) -> 'AttendanceAndHandleData':
        return AttendanceAndHandleData(
            try_get_int(row, AttendanceAndHandleDataIndex.RACE_NUMBER_INDEX),
            try_get_str(row, AttendanceAndHandleDataIndex.LOCATION_TYPE_INDEX),
            try_get_str(row, AttendanceAndHandleDataIndex.LOCATION_INDEX),
            try_get_int(row, AttendanceAndHandleDataIndex.ATTENDANCE_INDEX),
            try_get_float(row, AttendanceAndHandleDataIndex.HANDLE_INDEX)
        )


@dataclass
class StarterPerformanceData:
    race_number: int
    horse_key: str
    horse_name: str
    horse_foaling_date: str
    area_foaled: str
    breed_of_horse: str
    sex_of_horse: str
    color: str
    dams_name: str
    dams_year_of_birth: str
    dams_breed_type: str
    sires_name: str
    sires_year_of_birth: str
    sires_breed_type: str
    weight_carried: int
    horse_weight: int
    medications: str
    equipment: str
    earnings: int
    jockey_last_name: str
    jockey_first_name: str
    jockey_middle_name: str
    apprentice_type: str
    trainer_last_name: str
    trainer_first_name: str
    trainer_middle_name: str
    owner_last_name: str
    owner_first_name: str
    owner_middle_name: str
    odds: float
    nonbetting_indicator: str
    coupled_flag: str
    coupled_finish: str
    favorite_indicator: str
    post_position: int
    program_number: str
    position_at_start: int
    position_at_poc1: int
    position_at_poc2: int
    position_at_poc3: int
    position_at_poc4: int
    position_at_poc5: int
    original_finish: int
    official_finish: int
    length_ahead_at_poc1: float
    length_ahead_at_poc2: float
    length_ahead_at_poc3: float
    length_ahead_at_poc4: float
    length_ahead_at_poc5: float
    length_ahead_at_finish: float
    length_behind_at_poc1: float
    length_behind_at_poc2: float
    length_behind_at_poc3: float
    length_behind_at_poc4: float
    length_behind_at_poc5: float
    length_behind_at_finish: float
    dead_heat_flag: str
    horse_claiming_price: float
    short_comments: str
    long_comments: str
    win_payoff: float
    place_payoff: float
    show_payoff: float
    claimed_indicator: str
    claiming_trainer_key: int
    claiming_trainer_type: str
    claiming_trainer_last_name: str
    claiming_trainer_first_name: str
    claiming_trainer_middle_name: str
    claiming_owner_key: int
    claiming_owner_type: str
    claiming_owner_last_name: str
    claiming_owner_first_name: str
    claiming_owner_middle_name: str
    scratch_reason_code: str
    disqualification_indicator: str
    disqualification_placing: int
    trouble_indicator: str
    corrected_weight_indicator: str
    over_weight: int
    individual_horse_time: float
    speed_index: int
    breeder_name: str
    jockey_key: int
    trainer_key: int

    @staticmethod
    def create(row: list[str]) -> 'StarterPerformanceData':
        return StarterPerformanceData(
            try_get_int(row, StarterPerformanceDataIndex.RACE_NUMBER_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.HORSE_KEY_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.HORSE_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.HORSE_FOALING_DATE_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.AREA_FOALED_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.BREED_OF_HORSE_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.SEX_OF_HORSE_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.COLOR_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.DAMS_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.DAMS_YEAR_OF_BIRTH_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.DAMS_BREED_TYPE_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.SIRES_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.SIRES_YEAR_OF_BIRTH_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.SIRES_BREED_TYPE_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.WEIGHT_CARRIED_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.HORSE_WEIGHT_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.MEDICATIONS_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.EQUIPMENT_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.EARNINGS_USA_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.JOCKEYS_LAST_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.JOCKEYS_FIRST_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.JOCKEYS_MIDDLE_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.APPRENTICE_TYPE_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.TRAINERS_LAST_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.TRAINERS_FIRST_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.TRAINERS_MIDDLE_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.OWNERS_LAST_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.OWNERS_FIRST_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.OWNERS_MIDDLE_NAME_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.ODDS_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.NONBETTING_INDICATOR_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.COUPLED_FLAG_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.COUPLED_FINISH_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.FAVORITE_INDICATOR_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.POST_POSITION_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.PROGRAM_NUMBER_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.POSITION_AT_START_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.POSITION_AT_POC1_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.POSITION_AT_POC2_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.POSITION_AT_POC3_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.POSITION_AT_POC4_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.POSITION_AT_POC5_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.ORIGINAL_FINISH_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.OFFICIAL_FINISH_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_AHEAD_AT_POC1_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_AHEAD_AT_POC2_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_AHEAD_AT_POC3_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_AHEAD_AT_POC4_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_AHEAD_AT_POC5_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_AHEAD_AT_FINISH_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_BEHIND_AT_POC1_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_BEHIND_AT_POC2_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_BEHIND_AT_POC3_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_BEHIND_AT_POC4_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_BEHIND_AT_POC5_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.LENGTH_BEHIND_AT_FINISH_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.DEAD_HEAT_FLAG_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.INDIVIDUAL_HORSE_CLAIMING_PRICE_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.SHORT_COMMENTS_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.LONG_COMMENTS_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.WIN_PAYOFF_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.PLACE_PAYOFF_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.SHOW_PAYOFF_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.CLAIMED_INDICATOR_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.CLAIMING_TRAINER_KEY_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.CLAIMING_TRAINER_TYPE_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.CLAIMING_TRAINER_LAST_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.CLAIMING_TRAINER_FIRST_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.CLAIMING_TRAINER_MIDDLE_NAME_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.CLAIMING_OWNER_KEY_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.CLAIMING_OWNER_TYPE_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.CLAIMING_OWNER_LAST_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.CLAIMING_OWNER_FIRST_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.CLAIMING_OWNER_MIDDLE_NAME_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.SCRATCH_REASON_CODE_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.DISQUALIFICATION_INDICATOR_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.DISQUALIFICATION_PLACING_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.TROUBLE_INDICATOR_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.CORRECTED_WEIGHT_INDICATOR_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.OVER_WEIGHT_INDEX),
            try_get_float(row, StarterPerformanceDataIndex.INDIVIDUAL_HORSE_TIME_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.SPEED_INDEX),
            try_get_str(row, StarterPerformanceDataIndex.BREEDER_NAME_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.JOCKEY_KEY_INDEX),
            try_get_int(row, StarterPerformanceDataIndex.TRAINER_KEY_INDEX)
        )
