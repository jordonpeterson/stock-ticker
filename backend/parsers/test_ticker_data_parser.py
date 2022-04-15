from unittest import TestCase


class TestTickerDataParser(TestCase):
    def test_parse(self):
        self.fail()
    # def build_response_object(self, response):
    #     info = response.json()['results'][0]
    #     max_price = info['h']
    #     min_price = info['l']
    #     avg_price = np.mean(max_price, min_price)
    #     volume_weighted_average_price = info['vw']
    #     return {
    #         'maxPrice': max_price,
    #         'minPrice': min_price,
    #         'avgPrice': avg_price,
    #         'maxVolume': ,
    #         'minVolume': ,
    #         'avgVolume': ,
    #     }