import json
import requests

print('Loading function')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def get_stock_ticker(event):
    queryParameters = event['queryStringParameters']['']
    return queryParameters


def lambda_handler(event, context):
    url = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2021-07-22/2021-07-22?adjusted=true&sort=asc&limit=120&apiKey=NsSybiyV7LfRsy0CtMI9IcyRN2Dfkl54'
    response = requests.get(url)
    a = get_stock_ticker(event)
    info = {
        'context': str(context),
        'event': str(event),
        'response': str(response.text)
    }
    return respond(None, info)
