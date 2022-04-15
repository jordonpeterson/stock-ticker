import json
from request_clients import ticker_requests_client

print('Loading function')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    ticker_client = ticker_requests_client.TickerRequestClient()

    response = ticker_client.get_ticker_info(event)

    info = {
        'context': str(context),
        'event': str(event),
        'response': str(response.text)
    }
    return respond(None, info)
