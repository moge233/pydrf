#! python3


import os
import tempfile
import unittest

from pydrf.chart import Chart
from pydrf.textchart import AttendanceAndHandleData, CommentsAndRaceOdditiesData, FieldError, FootNoteData


def _record(*fields: object) -> str:
    return ','.join(f'"{field}"' for field in fields)


def _parse(lines: list[str]) -> Chart:
    with tempfile.TemporaryDirectory() as directory:
        path = os.path.join(directory, 'TST20260101.chart')
        with open(path, 'w') as chart_file:
            chart_file.write('\n'.join(lines) + '\n')
        return Chart.parse_chart(path)


HEADER = _record('H', 'USA', 'TST', '20260101', '3', 'D', 'Test')
RACE_1 = _record('R', 1, *(['0'] * 62))
RACE_2 = _record('R', 2, *(['0'] * 62))


class CommentsAndRaceOdditiesDataTestCase(unittest.TestCase):

    def test_create(self) -> None:
        data = CommentsAndRaceOdditiesData.create(['C', '7', 'A', 'Race was hand timed. '])
        self.assertEqual(data, CommentsAndRaceOdditiesData(7, 'A', 'Race was hand timed.'))

    def test_create_strict(self) -> None:
        row = ['C', '7', 'A', 'Race was hand timed.']
        self.assertEqual(CommentsAndRaceOdditiesData.create(row, strict=True),
                         CommentsAndRaceOdditiesData(7, 'A', 'Race was hand timed.'))
        self.assertIsNone(CommentsAndRaceOdditiesData.create(['C', ' ', 'A', ''], strict=True).race_number)
        with self.assertRaises(FieldError):
            CommentsAndRaceOdditiesData.create(['C', 'x', 'A', ''], strict=True)


class FootNoteDataTestCase(unittest.TestCase):

    def test_create(self) -> None:
        data = FootNoteData.create(['F', '1', '2', 'pole, closed outside and was up late.'])
        self.assertEqual(data, FootNoteData(1, 2, 'pole, closed outside and was up late.'))

    def test_create_strict(self) -> None:
        self.assertEqual(FootNoteData.create(['F', '1', '2', 'drew off'], strict=True), FootNoteData(1, 2, 'drew off'))
        self.assertIsNone(FootNoteData.create(['F', '1', '', 'drew off'], strict=True).sequence_number)
        with self.assertRaises(FieldError):
            FootNoteData.create(['F', '1', 'two', 'drew off'], strict=True)


class ChartCommentTestCase(unittest.TestCase):

    def test_comments_attached_to_their_own_race(self) -> None:
        chart = _parse([
            HEADER,
            RACE_1,
            RACE_2,
            _record('C', 1, 'A', 'Race was hand timed.'),
            _record('C', 2, 'B', 'No Contest'),
        ])
        race_1, race_2 = chart.races
        self.assertEqual(race_1.comments, [CommentsAndRaceOdditiesData(1, 'A', 'Race was hand timed.')])
        self.assertEqual(race_2.comments, [CommentsAndRaceOdditiesData(2, 'B', 'No Contest')])

    def test_race_without_comments_has_none(self) -> None:
        chart = _parse([HEADER, RACE_1])
        self.assertEqual(chart.races[0].comments, [])

    def test_comment_for_cancelled_race_is_dropped(self) -> None:
        chart = _parse([
            HEADER,
            RACE_1,
            _record('R', 3, *(['0'] * 62)),
            _record('C', 2, 'A', 'Hand timed'),
        ])
        self.assertIsNone(chart.races[1])
        self.assertEqual(sum(len(race.comments) for race in chart.races if race), 0)


    def test_comment_for_race_past_the_last_is_dropped(self) -> None:
        chart = _parse([HEADER, RACE_1, _record('C', 10, 'A', 'Race cancelled')])
        self.assertEqual(chart.races[0].comments, [])

    def test_comment_with_race_number_zero_is_dropped(self) -> None:
        chart = _parse([HEADER, RACE_1, _record('C', 0, 'A', 'Card note')])
        self.assertEqual(chart.races[0].comments, [])


class ChartFootnoteTestCase(unittest.TestCase):

    def test_footnotes_attached_to_their_own_race(self) -> None:
        chart = _parse([
            HEADER,
            RACE_1,
            RACE_2,
            _record('F', 1, 1, 'NEOPHYTE settled off the pace inside,'),
            _record('F', 1, 2, 'closed outside and was up late.'),
            _record('F', 2, 1, 'ROCK TO FAME set the pace.'),
        ])
        race_1, race_2 = chart.races
        self.assertEqual([footnote.sequence_number for footnote in race_1.footnotes], [1, 2])
        self.assertEqual(race_2.footnotes, [FootNoteData(2, 1, 'ROCK TO FAME set the pace.')])

    def test_get_footnote_joins_lines_in_sequence_order(self) -> None:
        chart = _parse([
            HEADER,
            RACE_1,
            _record('F', 1, 2, 'closed outside and was up late.'),
            _record('F', 1, 1, 'NEOPHYTE settled off the pace inside,'),
        ])
        self.assertEqual(
            chart.races[0].get_footnote(),
            'NEOPHYTE settled off the pace inside, closed outside and was up late.'
        )

    def test_get_footnote_without_footnotes_is_empty(self) -> None:
        chart = _parse([HEADER, RACE_1])
        self.assertEqual(chart.races[0].get_footnote(), '')

    def test_footnote_with_comma_kept_whole(self) -> None:
        chart = _parse([HEADER, RACE_1, _record('F', 1, 1, 'ins, 3wd 1/4, up late')])
        self.assertEqual(chart.races[0].footnotes[0].text, 'ins, 3wd 1/4, up late')

    def test_footnote_for_cancelled_race_is_dropped(self) -> None:
        chart = _parse([
            HEADER,
            RACE_1,
            _record('R', 3, *(['0'] * 62)),
            _record('F', 2, 1, 'Broke well and drew off.'),
        ])
        self.assertIsNone(chart.races[1])
        self.assertEqual(sum(len(race.footnotes) for race in chart.races if race), 0)


    def test_footnote_for_race_past_the_last_is_dropped(self) -> None:
        chart = _parse([HEADER, RACE_1, _record('F', 10, 1, 'Broke well.')])
        self.assertEqual(chart.races[0].footnotes, [])


class ChartAttendanceTestCase(unittest.TestCase):

    def test_attendance_records_kept_on_chart(self) -> None:
        chart = _parse([
            HEADER,
            RACE_1,
            _record('A', 0, 'Track', '', '0', '13792', '', '#'),
            _record('A', 0, 'Total', '', '0', '228370', '', '#'),
        ])
        self.assertEqual(chart.attendance, [
            AttendanceAndHandleData(0, 'Track', '', 0, 13792.0),
            AttendanceAndHandleData(0, 'Total', '', 0, 228370.0),
        ])

    def test_chart_without_attendance_has_none(self) -> None:
        chart = _parse([HEADER, RACE_1])
        self.assertEqual(chart.attendance, [])

    def test_chart_constructed_without_attendance_has_none(self) -> None:
        chart = Chart(chart_header := _parse([HEADER]).header, [])
        self.assertEqual(chart.header, chart_header)
        self.assertEqual(chart.attendance, [])


if __name__ == '__main__':
    unittest.main()
