from unittest import TestCase
import json

from backend import lambda_function


class Test(TestCase):
    def test_lambda_handler(self):
        result = lambda_function.lambda_handler(self.lambdaEvent, {})
        body = json.loads(result['body'])
        response = json.loads(body['response'])
        assert result

    lambdaEvent = {'resource': '/stock-ticker',
                   'path': '/stock-ticker',
                   'httpMethod': 'GET',
                   'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Cache-Control': 'no-cache',
                               'Host': '4u13q8f5d9.execute-api.us-east-2.amazonaws.com',
                               'Postman-Token': 'd9748097-91f2-4ba8-a962-a5262d4e1087',
                               'User-Agent': 'PostmanRuntime/7.28.3',
                               'X-Amzn-Trace-Id': 'Root=1-6258adff-757314c3295bd15620516782',
                               'X-Forwarded-For': '73.127.14.89', 'X-Forwarded-Port': '443',
                               'X-Forwarded-Proto': 'https'},
                   'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate, br'],
                                         'Cache-Control': ['no-cache'],
                                         'Host': ['4u13q8f5d9.execute-api.us-east-2.amazonaws.com'],
                                         'Postman-Token': ['d9748097-91f2-4ba8-a962-a5262d4e1087'],
                                         'User-Agent': ['PostmanRuntime/7.28.3'],
                                         'X-Amzn-Trace-Id': ['Root=1-6258adff-757314c3295bd15620516782'],
                                         'X-Forwarded-For': ['73.127.14.89'], 'X-Forwarded-Port': ['443'],
                                         'X-Forwarded-Proto': ['https']},
                   'queryStringParameters': {'a': '1', 'b': '2', 'c': '3'},
                   'multiValueQueryStringParameters': {'a': ['1'], 'b': ['2'], 'c': ['3']}, 'pathParameters': None,
                   'stageVariables': None,
                   'requestContext': {'resourceId': '30epc6', 'resourcePath': '/stock-ticker', 'httpMethod': 'GET',
                                      'extendedRequestId': 'QmAgAFV3CYcFfYQ=',
                                      'requestTime': '14/Apr/2022:23:27:59 +0000', 'path': '/prod/stock-ticker',
                                      'accountId': '533578317714', 'protocol': 'HTTP/1.1', 'stage': 'prod',
                                      'domainPrefix': '4u13q8f5d9', 'requestTimeEpoch': 1649978879886,
                                      'requestId': 'd22513ec-76a6-4234-90c4-969d492a1c58',
                                      'identity': {'cognitoIdentityPoolId': None, 'accountId': None,
                                                   'cognitoIdentityId': None, 'caller': None,
                                                   'sourceIp': '73.127.14.89', 'principalOrgId': None,
                                                   'accessKey': None, 'cognitoAuthenticationType': None,
                                                   'cognitoAuthenticationProvider': None, 'userArn': None,
                                                   'userAgent': 'PostmanRuntime/7.28.3', 'user': None},
                                      'domainName': '4u13q8f5d9.execute-api.us-east-2.amazonaws.com',
                                      'apiId': '4u13q8f5d9'}, 'body': None, 'isBase64Encoded': False}
