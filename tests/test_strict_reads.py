#! python3


import math
import unittest

from pydrf.textchart import (
    AttendanceAndHandleData,
    AttendanceAndHandleDataIndex,
    ExoticWageringData,
    ExoticWageringDataIndex,
    FieldError,
    Header,
    HeaderIndex,
    RaceData,
    RaceDataIndex,
    StarterPerformanceData,
    StarterPerformanceDataIndex,
    final_time_to_seconds,
    fraction_to_seconds,
    try_get_float,
    try_get_int,
)


def _row(record: str, index_type: type) -> list[str]:
    """A row of '0' fields long enough for every field of index_type."""
    return [record] + ['0'] * max(member.value for member in index_type)


class StrictGetTestCase(unittest.TestCase):

    def test_numbers_parse(self) -> None:
        self.assertEqual(try_get_int(['H', ' 12 '], HeaderIndex.COUNTRY_CODE_INDEX, strict=True), 12)
        self.assertEqual(try_get_float(['H', '124.41'], HeaderIndex.COUNTRY_CODE_INDEX, strict=True), 124.41)

    def test_zero_stays_zero(self) -> None:
        self.assertEqual(try_get_int(['H', '0'], HeaderIndex.COUNTRY_CODE_INDEX, strict=True), 0)
        self.assertEqual(try_get_float(['H', '0'], HeaderIndex.COUNTRY_CODE_INDEX, strict=True), 0.0)

    def test_blank_is_none(self) -> None:
        for value in ('', ' ', '   '):
            for getter in (try_get_int, try_get_float):
                with self.subTest(value=value, getter=getter.__name__):
                    self.assertIsNone(getter(['H', value], HeaderIndex.COUNTRY_CODE_INDEX, strict=True))

    def test_unreadable_value_raises_field_error(self) -> None:
        for getter, kind in ((try_get_int, 'int'), (try_get_float, 'float')):
            with self.subTest(getter=getter.__name__):
                with self.assertRaises(FieldError) as caught:
                    getter(['H', 'USA', 'KEE', 'Fast'], HeaderIndex.RACE_DATE_INDEX, strict=True)
                error = caught.exception
                self.assertIsInstance(error, ValueError)
                self.assertEqual((error.index, error.value, error.kind),
                                 (HeaderIndex.RACE_DATE_INDEX, 'Fast', kind))
                self.assertEqual(str(error), f"field 4 (RACE_DATE): 'Fast' is not a valid {kind}")

    def test_short_row_raises_field_error(self) -> None:
        for getter in (try_get_int, try_get_float):
            with self.subTest(getter=getter.__name__):
                with self.assertRaises(FieldError) as caught:
                    getter(['H'], HeaderIndex.TRACK_CODE_INDEX, strict=True)
                self.assertIsNone(caught.exception.value)
                self.assertEqual(str(caught.exception), 'field 3 (TRACK_CODE): missing (the row is too short)')

    def test_default_is_unchanged(self) -> None:
        self.assertEqual(try_get_int(['H', ' '], HeaderIndex.COUNTRY_CODE_INDEX), 0)
        self.assertTrue(math.isnan(try_get_float(['H', 'Fast'], HeaderIndex.COUNTRY_CODE_INDEX)))

    def test_time_conversions_pass_none_through(self) -> None:
        self.assertIsNone(final_time_to_seconds(None))
        self.assertIsNone(fraction_to_seconds(None))


class StrictCreateTestCase(unittest.TestCase):

    def test_every_record_reads_strictly(self) -> None:
        cases = [
            (Header, HeaderIndex, 'H', HeaderIndex.NUMBER_OF_RACES_INDEX, 'number_of_races'),
            (RaceData, RaceDataIndex, 'R', RaceDataIndex.PURSE_USA_INDEX, 'purse'),
            (ExoticWageringData, ExoticWageringDataIndex, 'E', ExoticWageringDataIndex.POOL_TOTAL_INDEX,
             'pool_total'),
            (AttendanceAndHandleData, AttendanceAndHandleDataIndex, 'A',
             AttendanceAndHandleDataIndex.ATTENDANCE_INDEX, 'attendance'),
            (StarterPerformanceData, StarterPerformanceDataIndex, 'S',
             StarterPerformanceDataIndex.WEIGHT_CARRIED_INDEX, 'weight_carried'),
        ]
        for record_type, index_type, record, index, attribute in cases:
            with self.subTest(record=record_type.__name__):
                row = _row(record, index_type)
                row[index.value] = ' '
                self.assertIsNone(getattr(record_type.create(row, strict=True), attribute))
                lenient = getattr(record_type.create(row), attribute)  # default: 0, or NaN for floats
                self.assertTrue(lenient == 0 or math.isnan(lenient))
                row[index.value] = 'x'
                with self.assertRaises(FieldError) as caught:
                    record_type.create(row, strict=True)
                self.assertIs(caught.exception.index, index)

    def test_blank_race_times_are_none(self) -> None:
        row = _row('R', RaceDataIndex)
        row[RaceDataIndex.FINAL_TIME_INDEX.value] = ''
        row[RaceDataIndex.FRACTION1_INDEX.value] = ''
        race = RaceData.create(row, strict=True)
        self.assertIsNone(race.final_time)
        self.assertIsNone(race.fraction1)
        self.assertEqual(race.fraction2, 0.0)


if __name__ == '__main__':
    unittest.main()
