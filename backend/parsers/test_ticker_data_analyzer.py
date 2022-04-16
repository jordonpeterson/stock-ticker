from unittest import TestCase
from ticker_data_analyzer import TickerDataAnalyzer


class TestTickerDataAnalyzer(TestCase):
    def setUp(self):
        self.ticker_data_analyzer = TickerDataAnalyzer()

    def test_find_max_price(self):
        result = self.ticker_data_analyzer._find_max_price(self.results)
        self.assertEqual(150, result)

    def test_find_min_price(self):
        result = self.ticker_data_analyzer._find_min_price(self.results)
        self.assertEqual(30, result)

    def test_find_avg_price(self):
        result = self.ticker_data_analyzer._find_avg_price(self.results)
        self.assertEqual(81.67, result)

    def test_find_max_volume(self):
        result = self.ticker_data_analyzer._find_max_volume(self.results)
        self.assertEqual(1500, result)

    def test_find_min_volume(self):
        result = self.ticker_data_analyzer._find_min_volume(self.results)
        self.assertEqual(500, result)

    def test_find_avg_volume(self):
        result = self.ticker_data_analyzer._find_avg_volume(self.results)
        self.assertEqual(1000, result)

    def test_generate_report(self):
        result = self.ticker_data_analyzer.generate_report(self.results)
        self.assertEqual(150, result.max_price)
        self.assertEqual(30, result.min_price)
        self.assertEqual(81.67, result.avg_price)
        self.assertEqual(1500, result.max_volume)
        self.assertEqual(500, result.min_volume)
        self.assertEqual(1000, result.avg_volume)

    results = [
        {
            "v": 500,
            "h": 100,
            "l": 50,
        },
        {
            "v": 1000,
            "h": 150,
            "l": 100,
        },
        {
            "v": 1500,
            "h": 60,
            "l": 30,
        }
    ]
