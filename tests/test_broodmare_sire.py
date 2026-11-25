#! python3
"""Tests for the broodmare sire (dam's sire) fields of starter records."""


import os
import tempfile
import unittest

from pydrf.chart import Chart
from pydrf.textchart import StarterPerformanceData, StarterPerformanceDataIndex


def _starter_row(**fields: str) -> list[str]:
    """Build an S record with every field set to '0', then apply overrides.

    Args:
        **fields: Index member names (without ``_INDEX``) and their values.

    Returns:
        The row.
    """
    size = max(member.value for member in StarterPerformanceDataIndex) + 1
    row = ['S'] + ['0'] * (size - 1)
    for name, value in fields.items():
        row[StarterPerformanceDataIndex[f'{name}_INDEX'].value] = value
    return row


def _quoted(row: list[str]) -> str:
    """Join a row as a quoted CSV line, the way charts are written."""
    return ','.join(f'"{value}"' for value in row)


class BroodmareSireTestCase(unittest.TestCase):
    """The dam's sire is read in both lenient and strict mode."""

    def test_fields_are_read(self) -> None:
        """The name and year of birth come from fields 16 and 17."""
        row = _starter_row(
            BROODMARES_SIRES_NAME='Tapit',
            BROODMARES_SIRES_YEAR_OF_BIRTH='2001',
            SIRES_NAME='Into Mischief',
        )
        for strict in (False, True):
            with self.subTest(strict=strict):
                data = StarterPerformanceData.create(row, strict=strict)
                self.assertEqual(data.broodmares_sires_name, 'Tapit')
                self.assertEqual(data.broodmares_sires_year_of_birth, '2001')
                self.assertEqual(data.sires_name, 'Into Mischief')

    def test_trailing_spaces_are_stripped(self) -> None:
        """Text fields are right-stripped like the other name fields."""
        row = _starter_row(BROODMARES_SIRES_NAME='Tapit   ')
        data = StarterPerformanceData.create(row)
        self.assertEqual(data.broodmares_sires_name, 'Tapit')

    def test_blank_fields_are_empty(self) -> None:
        """A blank dam's sire reads as an empty string in both modes."""
        row = _starter_row(
            BROODMARES_SIRES_NAME='', BROODMARES_SIRES_YEAR_OF_BIRTH=' '
        )
        for strict in (False, True):
            with self.subTest(strict=strict):
                data = StarterPerformanceData.create(row, strict=strict)
                self.assertEqual(data.broodmares_sires_name, '')
                self.assertEqual(data.broodmares_sires_year_of_birth, '')

    def test_parsed_chart_starter_carries_the_dams_sire(self) -> None:
        """A starter parsed from a chart file exposes its dam's sire."""
        header = '"H","USA","TST","20260101","1","D","Test"'
        race = _quoted(['R', '1'] + ['0'] * 62)
        starter_line = _quoted(
            _starter_row(
                RACE_NUMBER='1',
                BROODMARES_SIRES_NAME='Tapit',
                BROODMARES_SIRES_YEAR_OF_BIRTH='2001',
            )
        )
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'TST20260101.chart')
            with open(path, 'w') as chart_file:
                chart_file.write('\n'.join([header, race, starter_line]))
                chart_file.write('\n')
            chart = Chart.parse_chart(path)
        race_1 = chart.races[0]
        assert race_1 is not None
        starter = race_1.starters[0]
        self.assertEqual(starter.broodmares_sires_name, 'Tapit')
        self.assertEqual(starter.broodmares_sires_year_of_birth, '2001')


if __name__ == '__main__':
    unittest.main()
