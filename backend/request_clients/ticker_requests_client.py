import requests
import os


def get_query_param(event, query_param_name):
    query_parameters = event['queryStringParameters']
    if query_param_name in query_parameters:
        param = query_parameters[query_param_name]
        # Add other validation. The query params come from the frontend and are not safe.
        if len(param) == 0:
            raise ValueError("The " + query_param_name + " query parameter was empty. Value: " + param)
        return param
    else:
        raise ValueError("The " + query_param_name + " query parameter was missing")


def verify_request_is_of_expected_rest_type(event, expected_type):
    rest_type = event['httpMethod']
    if rest_type.casefold() != expected_type.casefold():
        raise ValueError(
            "This endpoint only supports " + expected_type + "requests. The attempted request was a " + rest_type)


class TickerRequestClient:
    def __init__(self):
        self.urlBase = 'https://api.polygon.io/v2'
        self.polygon_api_key = os.environ['POLYGON_API_KEY']

    def get_ticker_info(self, event):
        verify_request_is_of_expected_rest_type(event, 'GET')
        ticker = get_query_param(event, 'ticker')
        if len(ticker) > 5:
            raise ValueError(
                "Ticker: " + ticker + " is too long. The maximum length is 5 characters. Its actual length was "
                + len(ticker))

        start_date = get_query_param(event, 'startDate')
        end_date = get_query_param(event, 'endDate')
        response = self.make_ticker_info_rest_request(ticker, start_date, end_date)
        return response

    def make_ticker_info_rest_request(self, ticker, start_date, end_date):
        params = {'apiKey': self.polygon_api_key}
        url = self.urlBase + "/aggs/ticker/" + ticker + "/range/1/day/" + start_date + "/" + end_date
        return requests.get(url, params)
