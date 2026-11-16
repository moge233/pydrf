#! python3


import os
import tempfile
import unittest

from pydrf.chart import Chart


class MissingChartFileTestCase(unittest.TestCase):

    def test_missing_file_raises(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, 'MISSING20260101.chart')
            with self.assertRaises(FileNotFoundError):
                Chart.parse_chart(path)


if __name__ == '__main__':
    unittest.main()
