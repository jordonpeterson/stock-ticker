from functools import reduce
import numpy as np


def find_max(stock_ticker_results, key):
    max_value = reduce(lambda old_value, new_value: old_value if old_value[key] > new_value[
        key] else new_value, stock_ticker_results)
    return max_value[key]


def find_min(stock_ticker_results, key):
    min_value = reduce(lambda old_value, new_value: old_value if old_value[key] < new_value[key] else new_value,
                       stock_ticker_results)
    return min_value[key]


class TickerDataAnalyzer:
    max_price_key = 'h'
    min_price_key = 'l'
    volume_key = 'v'
    price_significant_figures = 2

    def find_max_price(self, stock_ticker_results):
        max_price = find_max(stock_ticker_results, self.max_price_key)
        return round(max_price, self.price_significant_figures)

    def find_min_price(self, stock_ticker_results):
        min_price = find_min(stock_ticker_results, self.min_price_key)
        return round(min_price, self.price_significant_figures)

    # TODO verify if we calculated average price the right way
    def find_avg_price(self, stock_ticker_results):
        total_price = 0
        for result in stock_ticker_results:
            total_price += np.mean([
                result[self.max_price_key],
                result[self.min_price_key]
            ])
        avg_price = total_price / len(stock_ticker_results)
        return round(avg_price, self.price_significant_figures)

    def find_max_volume(self, stock_ticker_results):
        return find_max(stock_ticker_results, self.volume_key)

    def find_min_volume(self, stock_ticker_results):
        return find_min(stock_ticker_results, self.volume_key)

    def find_avg_volume(self, stock_ticker_results):
        cumulative_volume = 0
        for result in stock_ticker_results:
            cumulative_volume += result[self.volume_key]
        return cumulative_volume / len(stock_ticker_results)
