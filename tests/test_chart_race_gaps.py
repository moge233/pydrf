#! python3


import os
import tempfile
import unittest

from pydrf.chart import Chart


def _record(*fields: object) -> str:
    return ','.join(f'"{field}"' for field in fields)


def _parse(race_numbers: list[int]) -> Chart:
    lines = [_record('H', 'USA', 'TST', '20260101', str(max(race_numbers)), 'D', 'Test')]
    lines += [_record('R', number, *(['0'] * 62)) for number in race_numbers]
    lines += [_record('S', number, *(['0'] * 90)) for number in race_numbers]
    with tempfile.TemporaryDirectory() as directory:
        path = os.path.join(directory, 'TST20260101.chart')
        with open(path, 'w') as chart_file:
            chart_file.write('\n'.join(lines) + '\n')
        return Chart.parse_chart(path)


class RaceNumberGapTestCase(unittest.TestCase):

    def test_no_gap(self) -> None:
        chart = _parse([1, 2, 3])
        self.assertEqual([race.number for race in chart.races], [1, 2, 3])

    def test_single_cancelled_race(self) -> None:
        chart = _parse([1, 3])
        self.assertIsNone(chart.races[1])
        self.assertEqual(chart.races[2].number, 3)
        self.assertEqual(len(chart.races[2].starters), 1)

    def test_consecutive_cancelled_races(self) -> None:
        chart = _parse([1, 4, 5])
        self.assertEqual(
            [race.number if race else None for race in chart.races],
            [1, None, None, 4, 5],
        )
        self.assertEqual(len(chart.races[3].starters), 1)

    def test_card_starting_after_cancelled_races(self) -> None:
        chart = _parse([3, 4])
        self.assertEqual(
            [race.number if race else None for race in chart.races],
            [None, None, 3, 4],
        )


if __name__ == '__main__':
    unittest.main()
