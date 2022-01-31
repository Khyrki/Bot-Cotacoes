import time

# Esse é o timer que determina quando devo mandar o candle para o banco
# Optei por fazer de formar desacoplada para evitar o que o tempo da requisicao some com o tempo entre requisicoes
# e assim ocorra um atraso muito grande entre intervalos.
class Timer():
    def __init__(self, cotacao):
        self.segundos = 0
        self.cotacao = cotacao


    def contador(self):
        intervalos = [60, 300, 600]

        while True:
            self.segundos += 1
            for intervalo in intervalos:
                if self.segundos % intervalo == 0:
                    self.cotacao.close_cadle(intervalos.index(intervalo))
            time.sleep(1)
  