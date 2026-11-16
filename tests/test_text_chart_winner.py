#! python3


import unittest

from pydrf.textchart import Header, StarterPerformanceData, TextChart, StarterPerformanceDataIndex


def _starter(race_number: int, finish: int, dead_heat: str, name: str) -> StarterPerformanceData:
    row = ['S', str(race_number)] + ['0'] * 90
    row[StarterPerformanceDataIndex.HORSE_NAME_INDEX.value] = name
    row[StarterPerformanceDataIndex.ORIGINAL_FINISH_INDEX.value] = str(finish)
    row[StarterPerformanceDataIndex.DEAD_HEAT_FLAG_INDEX.value] = dead_heat
    return StarterPerformanceData.create(row)


class GetWinnerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        header = Header.create(['H', 'USA', 'TST', '20260101', '2', 'D', 'Test'])
        starters = [
            _starter(1, 2, 'N', 'Second'),
            _starter(1, 1, 'N', 'Winner'),
            _starter(2, 1, 'Y', 'Dead Heat A'),
            _starter(2, 1, 'Y', 'Dead Heat B'),
        ]
        self._chart = TextChart(header, [], starters)

    def test_outright_winner(self) -> None:
        self.assertEqual(self._chart.get_winner(1).horse_name, 'Winner')

    def test_dead_heat_for_win_raises_lookup_error(self) -> None:
        with self.assertRaises(LookupError):
            self._chart.get_winner(2)

    def test_unknown_race_raises_lookup_error(self) -> None:
        with self.assertRaises(LookupError):
            self._chart.get_winner(3)


if __name__ == '__main__':
    unittest.main()
