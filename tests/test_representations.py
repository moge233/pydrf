#! python3


import unittest

from pydrf.chart import Chart
from pydrf.jockey import Jockey
from pydrf.owner import Owner
from pydrf.race import Race
from pydrf.starter import Starter
from pydrf.textchart import Header, RaceData, StarterPerformanceData, TextChart
from pydrf.trainer import Trainer


class RepresentationTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.header = Header.create(['H', 'USA', 'TST', '20260101', '1', 'D', 'Test'])
        self.race_data = RaceData.create(['R', '1'] + ['0'] * 62)
        self.starter_data = StarterPerformanceData.create(['S', '1'] + ['0'] * 90)
        self.jockey = Jockey('Ortiz', 'Jose', 'L.', ' ', 1547)
        self.trainer = Trainer('Sharp', 'Joe', ' ', 184)

    def assert_representation(self, obj: object, class_name: str, first_field: str) -> None:
        self.assertEqual(str(obj), repr(obj))
        self.assertTrue(str(obj).startswith(f'{class_name}({first_field}='))
        self.assertTrue(str(obj).endswith(')'))

    def test_owner(self) -> None:
        owner = Owner('Mulholland Farm', ' ', ' ')
        self.assert_representation(owner, 'Owner', 'last_name')
        self.assertIn('last_name=Mulholland Farm', str(owner))

    def test_jockey(self) -> None:
        self.assert_representation(self.jockey, 'Jockey', 'last_name')
        self.assertIn('key=1547', str(self.jockey))

    def test_trainer(self) -> None:
        self.assert_representation(self.trainer, 'Trainer', 'last_name')
        self.assertIn('key=184', str(self.trainer))

    def test_starter(self) -> None:
        starter = Starter(self.starter_data, self.jockey, self.trainer)
        self.assert_representation(starter, 'Starter', 'name')

    def test_race(self) -> None:
        race = Race(self.race_data, [], [])
        self.assert_representation(race, 'Race', 'number')
        self.assertIn('number=1', str(race))

    def test_chart(self) -> None:
        chart = Chart(self.header, [Race(self.race_data, [], [])])
        self.assert_representation(chart, 'Chart', 'header')

    def test_text_chart(self) -> None:
        text_chart = TextChart(self.header, [self.race_data], [self.starter_data])
        self.assert_representation(text_chart, 'TextChart', 'header')


if __name__ == '__main__':
    unittest.main()
