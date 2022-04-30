import json
from request_clients.ticker_requests_client import TickerRequestClient
from ticker_data_analyzer import TickerDataAnalyzer

print('Loading function')


def respond(status_code, res):
    return {
        'statusCode': status_code,
        'body': json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }


def lambda_handler(event, context):
    ticker_client = TickerRequestClient()
    report_generator = TickerDataAnalyzer()
    try:
        ticker_results = ticker_client.get_ticker_info(event)
    except ValueError as e:
        return respond(400, e.args[0])


    if ticker_results.json()['status'] == "ERROR":
        return respond(ticker_results.status_code, ticker_results.text)
    results = ticker_results.json()['results']

    report = report_generator.generate_report(results)

    return respond(200, report)
