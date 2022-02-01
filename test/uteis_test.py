import requests
from uteis.uteis import Request

# 
def test_request():

    request = Request().monero_currency()

    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url)
    json = response.json()['BTC_XMR']

    assert request['id'] == json['id']
