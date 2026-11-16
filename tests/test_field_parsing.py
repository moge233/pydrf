#! python3


import math
import unittest

from pydrf.textchart import (
    AttendanceAndHandleData,
    HeaderIndex,
    final_time_to_seconds,
    fraction_to_seconds,
    try_get_float,
    try_get_int,
    try_get_str,
)


class TryGetTestCase(unittest.TestCase):

    def test_str_strips_trailing_whitespace(self) -> None:
        row = ['H', 'USA ', 'KEE']
        self.assertEqual(try_get_str(row, HeaderIndex.COUNTRY_CODE_INDEX), 'USA')

    def test_int_parses_number(self) -> None:
        row = ['H', '12 ']
        self.assertEqual(try_get_int(row, HeaderIndex.COUNTRY_CODE_INDEX), 12)

    def test_int_blank_or_text_is_zero(self) -> None:
        for value in (' ', '', 'Fast'):
            with self.subTest(value=value):
                self.assertEqual(try_get_int(['H', value], HeaderIndex.COUNTRY_CODE_INDEX), 0)

    def test_float_parses_number(self) -> None:
        row = ['H', '124.41']
        self.assertEqual(try_get_float(row, HeaderIndex.COUNTRY_CODE_INDEX), 124.41)

    def test_float_blank_or_text_is_nan(self) -> None:
        for value in (' ', '', 'Fast'):
            with self.subTest(value=value):
                self.assertTrue(math.isnan(try_get_float(['H', value], HeaderIndex.COUNTRY_CODE_INDEX)))

    def test_short_row_raises_index_error(self) -> None:
        for getter in (try_get_str, try_get_int, try_get_float):
            with self.subTest(getter=getter.__name__):
                with self.assertRaises(IndexError):
                    getter(['H'], HeaderIndex.TRACK_CODE_INDEX)


class TimeConversionTestCase(unittest.TestCase):

    def test_final_time_with_minutes(self) -> None:
        self.assertEqual(final_time_to_seconds(124.41), 84.41)

    def test_final_time_under_a_minute(self) -> None:
        self.assertEqual(final_time_to_seconds(58.26), 58.26)

    def test_fraction_with_minutes(self) -> None:
        self.assertEqual(fraction_to_seconds(11155), 71.55)

    def test_fraction_under_a_minute(self) -> None:
        self.assertEqual(fraction_to_seconds(2242), 22.42)


class AttendanceAndHandleDataTestCase(unittest.TestCase):

    def test_create(self) -> None:
        data = AttendanceAndHandleData.create(['A', '0', 'T', 'On Track', '5321', '1234567.50', ''])
        self.assertEqual(data, AttendanceAndHandleData(0, 'T', 'On Track', 5321, 1234567.50))


if __name__ == '__main__':
    unittest.main()
