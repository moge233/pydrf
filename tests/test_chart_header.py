#! python3


import os
import tempfile
import unittest

from pydrf.chart import Chart


def _record(*fields: object) -> str:
    return ','.join(f'"{field}"' for field in fields)


class ChartHeaderTestCase(unittest.TestCase):

    def _parse(self, text: str) -> Chart:
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'TST20260101.chart')
            with open(path, 'w') as chart_file:
                chart_file.write(text)
            return Chart.parse_chart(path)

    def test_empty_file_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, 'no header'):
            self._parse('')

    def test_chart_without_header_raises_value_error(self) -> None:
        text = _record('R', 1, *(['0'] * 62)) + '\n'
        with self.assertRaisesRegex(ValueError, 'no header'):
            self._parse(text)


if __name__ == '__main__':
    unittest.main()
