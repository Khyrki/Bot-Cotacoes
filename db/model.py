from db.connection import cursor
from datetime import datetime

# Após o candle completo aqui eu mando para o banco de dados
class Model():
    def save_candle(self, candle_table, candle_value):
        
        sql = """INSERT INTO smarttbot."""+candle_table+""" (moeda, date_time, open, low, high, close)
              VALUES (%s, %s, %s, %s, %s, %s)"""
        
        val = ('Monero', datetime.today(), candle_value["open"], candle_value["low"], candle_value["high"], candle_value["close"])

        cursor.execute(sql, val)
