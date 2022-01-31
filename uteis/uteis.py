import requests

# Classe que realiza a consulta ao API, optei por fazer apenas com uma moeda pois estava
# ficando sem tempo e ainda tinha que configurar o docker, fazer a documentacao e testar,
# mas acredito que esteja bem generico e facil de escalar no futuro
class Request:
    url = 'https://poloniex.com/public?command=returnTicker'

    def monero_currency(self, moeda='BTC_XMR'):
        response = requests.get(self.url)
        json = response.json()
        return json[moeda]
