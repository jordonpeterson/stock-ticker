import requests


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


def verify_its_a_get_request(event):
    rest_type = event['httpMethod']
    if rest_type.casefold() != 'GET'.casefold():
        raise ValueError("This endpoint only supports GET requests. The attempted request was a " + rest_type)


class TickerRequestClient:

    def __init__(self):
        self.urlBase = 'https://api.polygon.io/v2'

    def get_ticker_info(self, event):
        verify_its_a_get_request(event)
        ticker = get_query_param(event, 'ticker')
        start_date = get_query_param(event, 'startDate')
        end_date = get_query_param(event, 'endDate')
        response = self.make_ticker_info_rest_request(ticker, start_date, end_date)
        return response

    def make_ticker_info_rest_request(self, ticker, start_date, end_date):
        # move API key to environment variable in lambda
        params = {'apiKey': 'NsSybiyV7LfRsy0CtMI9IcyRN2Dfkl54'}
        url = self.urlBase + "/aggs/ticker/" + ticker + "/range/1/day/" + start_date + "/" + end_date
        return requests.get(url, params)

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
