#! python3


import os
import tempfile
import unittest

from pydrf.chart import Chart


def _record(*fields: object) -> str:
    return ','.join(f'"{field}"' for field in fields)


def _parse(lines: list[str]) -> Chart:
    with tempfile.TemporaryDirectory() as directory:
        path = os.path.join(directory, 'TST20260101.chart')
        with open(path, 'w') as chart_file:
            chart_file.write('\n'.join(lines) + '\n')
        return Chart.parse_chart(path)


HEADER = _record('H', 'USA', 'TST', '20260101', '3', 'D', 'Test')


class ChartRecordTestCase(unittest.TestCase):

    def test_starter_horse_key_and_name(self) -> None:
        starter_row = ['S', 1, '000011113095TB', 'Belle Ofthe Dance'] + ['0'] * 88
        chart = _parse([HEADER, _record('R', 1, *(['0'] * 62)), _record(*starter_row)])
        starter = chart.races[0].starters[0]
        self.assertEqual(starter.horse_key, '000011113095TB')
        self.assertEqual(starter.name, 'Belle Ofthe Dance')

    def test_header_parsed(self) -> None:
        chart = _parse([HEADER, _record('R', 1, *(['0'] * 62))])
        self.assertEqual(chart.header.track_code, 'TST')
        self.assertEqual(chart.header.race_date, '20260101')

    def test_attendance_comment_and_footnote_records_ignored(self) -> None:
        chart = _parse([
            HEADER,
            _record('R', 1, *(['0'] * 62)),
            _record('S', 1, *(['0'] * 90)),
            _record('A', 0, 'T', 'On Track', '5321', '1234567.50', '', ''),
            _record('C', 1, '1', 'Race declared unofficial'),
            _record('F', 1, '1', 'Broke well and drew off.'),
        ])
        self.assertEqual(len(chart.races), 1)
        self.assertEqual(len(chart.races[0].starters), 1)

    def test_unknown_record_type_ignored(self) -> None:
        chart = _parse([HEADER, _record('R', 1, *(['0'] * 62)), _record('X', 1, 'unknown')])
        self.assertEqual(len(chart.races), 1)

    def test_records_for_cancelled_race_are_dropped(self) -> None:
        chart = _parse([
            HEADER,
            _record('R', 1, *(['0'] * 62)),
            _record('R', 3, *(['0'] * 62)),
            _record('S', 2, *(['0'] * 90)),
            _record('E', 2, 'EX', '1', '1-2', '2', '100', '10', '0'),
            _record('S', 3, *(['0'] * 90)),
        ])
        self.assertIsNone(chart.races[1])
        self.assertEqual(len(chart.races[0].starters), 0)
        self.assertEqual(len(chart.races[2].starters), 1)
        self.assertEqual(sum(len(race.wagering) for race in chart.races if race), 0)


if __name__ == '__main__':
    unittest.main()
