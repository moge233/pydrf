#! python3


import os
import tempfile
import unittest

from pydrf.chart import Chart


def _record(*fields: object) -> str:
    return ','.join(f'"{field}"' for field in fields)


def _write_chart(directory: str, lines: list[str]) -> str:
    path = os.path.join(directory, 'TST20260101.chart')
    with open(path, 'w') as chart_file:
        chart_file.write('\n'.join(lines) + '\n')
    return path


class ExoticWageringAttachmentTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        lines = [_record('H', 'USA', 'TST', '20260101', '2', 'D', 'Test')]
        lines += [_record('R', number, *(['0'] * 62)) for number in (1, 2)]
        lines += [_record('S', number, *(['0'] * 90)) for number in (1, 2)]
        lines.append(_record('E', 1, 'EX', '1', '1-2', '2', '100', '10', '0'))
        lines.append(_record('E', 1, 'TRI', '1', '1-2-3', '1', '50', '25', '0'))
        lines.append(_record('E', 2, 'EX', '1', '2-1', '2', '80', '12', '0'))
        self._chart = Chart.parse_chart(_write_chart(self._tmp.name, lines))

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_wagers_attached_to_their_own_race(self) -> None:
        race_1, race_2 = self._chart.races
        self.assertEqual([w.wager_type for w in race_1.wagering], ['EX', 'TRI'])
        self.assertEqual([w.wager_type for w in race_2.wagering], ['EX'])

    def test_each_wager_attached_once(self) -> None:
        total = sum(len(race.wagering) for race in self._chart.races)
        self.assertEqual(total, 3)


if __name__ == '__main__':
    unittest.main()
