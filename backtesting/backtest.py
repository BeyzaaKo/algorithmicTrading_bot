'''Backtesting için gerekli olan kodları içeren dosya.'''


import backtrader as bt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class StatArbStrategy(bt.Strategy):
    params = (
        ('z_score_buy', -1.0),
        ('z_score_sell', 1.0),
    )

    def __init__(self):
        self.lead_data = self.datas[0].close
        self.leg_data = self.datas[1].close

    def next(self):
        spread = self.lead_data - self.leg_data

        if isinstance(spread, float):
            # spread bir float ise z-score'ı 0 olarak ayarla
            z_score = 0
        else:
            z_score = (spread - spread.mean()) / spread.std() if len(spread) > 1 else 0

        if z_score < self.params.z_score_buy:
            self.buy()
        elif z_score > self.params.z_score_sell:
            self.sell()


def run_backtest(df_lead, df_lag):
    cerebro = bt.Cerebro()

    # DataFrame'i direkt olarak ekleyin, PandasData'ya dönüştürmeye gerek yok
    data_lead = bt.feeds.PandasData(dataname=df_lead, name='lead')
    data_lag = bt.feeds.PandasData(dataname=df_lag, name='lag')

    cerebro.adddata(data_lead)
    cerebro.adddata(data_lag)

    cerebro.addstrategy(StatArbStrategy)

    cerebro.run()

    # Analiz için kullanılan nesneye erişim
    cerebro_analyzer = cerebro.runstrats[0]

    # Analiz sonuçlarını döndür
    return cerebro, cerebro_analyzer

    '''cerebro.adddata(data_lead)
    cerebro.adddata(data_lag)

    cerebro.addstrategy(StatArbStrategy)

    cerebro.run()

    # Analiz için kullanılan nesneye erişim
    cerebro_analyzer = cerebro.runstrats[0]

    # Analiz sonuçlarını döndür
    return cerebro, cerebro_analyzer'''