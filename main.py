from cotacoes import Cotacao
from timer import Timer
import threading

# Essa é minha main classe que starta a aplicacao
class Main():
    def __init__(self):
        self.cotacao = Cotacao()
        self.timer = Timer(self.cotacao)
    
    def start(self):
        self.cotacao.inicia_candle()

        threading.Thread(target=self.cotacao.update_cotacao).start()
        threading.Thread(target=self.timer.contador).start()

Main().start()