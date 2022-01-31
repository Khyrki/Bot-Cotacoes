from uteis.uteis import Request
import time

# Aqui de fato eu monto o candle com as inforcamoes da api
class Cotacao():
    def __init__(self):
        'instanciar a classe que conversa com o banco de dados'
        pass

    um_minuto = {}
    cinco_minutos = {}
    dez_minutos = {}
    intervalos = [um_minuto, cinco_minutos, dez_minutos]


    def inicia_candle(self):
        api_response = Request().monero_currency()
        self.um_minuto['open'] = api_response['last']
        self.cinco_minutos['open'] = api_response['last']
        self.dez_minutos['open'] = api_response['last']


    def set_cotacao_atual(self, cotacao, intervalo):
        if 'high' not in intervalo or intervalo['high'] < cotacao:
            intervalo['high'] = cotacao
        
        if 'low' not in intervalo or intervalo['low'] > cotacao:
            intervalo['low'] = cotacao
            

    def update_cotacao(self):
        while True:
            api_response = Request().monero_currency()
            for intervalo in self.intervalos:
                self.set_cotacao_atual(api_response['last'], intervalo)
            time.sleep(3)


    def close_cadle(self, index):
        # solucao paleativa para informar em qual tabela será salva cada candle
        tabela = ''
        if index == 0:
            tabela = 'candle_1min'
        elif index == 1:
            tabela = 'candle_5min'
        else:
            tabela = 'candle_10min'

        api_response = Request().monero_currency()

        self.intervalos[index]['close'] = api_response['last']
        
        'Funcao que salva o candle no banco de dados'

        self.intervalos[index]['open'] = api_response['last']
        self.intervalos[index]['high'] = api_response['last']
        self.intervalos[index]['low'] = api_response['last']