from unittest import TestCase
import json

from backend import lambda_function


class Test(TestCase):
    def test_lambda_handler(self):
        result = lambda_function.lambda_handler(self.lambdaEvent, {})
        body = json.loads(result['body'])
        response = json.loads(body['response'])
        assert response

    lambdaEvent = {'resource': '/stock-ticker',
                   'path': '/stock-ticker',
                   'httpMethod': 'GET',
                   'headers': {
                       'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Cache-Control': 'no-cache',
                       'Host': '4u13q8f5d9.execute-api.us-east-2.amazonaws.com',
                   },
                   'queryStringParameters': {'ticker': 'AAPL',
                                             'startDate': '2020-01-01',
                                             'endDate': '2020-12-31'},
                   'body': None}
