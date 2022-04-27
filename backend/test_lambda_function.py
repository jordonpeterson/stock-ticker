import unittest

from backend import lambda_function


class MyTestCase(unittest.TestCase):
    def test_lambda_handler_success(self):
        result = lambda_function.lambda_handler(self.success_lambda_event, {})
        assert result['statusCode'] == 200

    def test_lambda_handler_failure(self):
        result = lambda_function.lambda_handler(self.failure_lambda_event, {})
        assert result['statusCode'] == 400

    success_lambda_event = {'httpMethod': 'GET',
                            'queryStringParameters': {'ticker': 'AAPL',
                                                      'startDate': '2020-01-01',
                                                      'endDate': '2020-12-31'},
                            }
    failure_lambda_event = {'httpMethod': 'GET',
                            'queryStringParameters': {'ticker': 'AAPL',
                                                      'startDate': 'INVALID',
                                                      'endDate': '2020-12-31'},
                            }


if __name__ == '__main__':
    unittest.main()
