'''Ana uygulama dosyası, tüm diğer modülleri içeren ve projeyi başlatan dosya.'''


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import quandl
import backtrader as bt

from data_collection.quandl_api import get_stock_data
from strategy.statistical_arbitrage import run_stat_arb_strategy
from backtesting.backtest import run_backtest
from visualization.plot_utils import plot_prices_with_signals

def main():
    # Veri Toplama
    symbol_lead = 'WIKI/MSFT'  # MSFT için Quandl simgesi
    symbol_lag = 'WIKI/IBM'    # IBM için Quandl simgesi
    api_key = 'mauY_7fP_tLjytR4ks-P'

    #'AC39YAMCYPHC6JMK' alpha vantage api (günde 25 istek yapıyor)
    #symbol_lead = 'MSFT'  # MSFT için Alpha Vantage simgesi
    #symbol_lag = 'IBM'  # IBM için Alpha Vantage simgesi
    #api_key = 'AC39YAMCYPHC6JMK'

    # Quandl API'siyle veri çekme
    df_lead = get_stock_data(api_key, symbol_lead)
    df_lag = get_stock_data(api_key, symbol_lag)

    # Her iki DataFrame'i ortak tarih aralığına göre filtrele
    # dataFrame'lerin aynı tarih aralığına sahip olduğundan emin olmamız gerekiyor
    common_start_date = max(df_lead.index.min(), df_lag.index.min())
    common_end_date = min(df_lead.index.max(), df_lag.index.max())

    df_lead_filtered = df_lead[(df_lead.index >= common_start_date) & (df_lead.index <= common_end_date)]
    df_lag_filtered = df_lag[(df_lag.index >= common_start_date) & (df_lag.index <= common_end_date)]

    # Filtrelenmiş DataFrame'leri yazdır
    #print("Filtered Lead DataFrame:")
    #print(df_lead_filtered.head())

    #print("\nFiltered Lag DataFrame:")
    #print(df_lag_filtered.head())

    # Strateji Geliştirme
    buy_signal, sell_signal = run_stat_arb_strategy(df_lead_filtered, df_lag_filtered)

    # Backtesting
    cerebro, cumulative_return = run_backtest(df_lead_filtered, df_lag_filtered)

    # Grafikleri Çiz
    #plot_prices_with_signals(df_lead_filtered, df_lag_filtered, buy_signal, sell_signal, cerebro)
    cerebro.plot(style='candlestick')  # Backtrader'ın kendi grafiğini kullanabilirsiniz

    # Sonuçları Yazdır
    print("Backtest Sonuçları:")
    print("Cerebro Nesnesi:", cerebro)
    print("Kümülatif Getiri Analizi:", cumulative_return)

if __name__ == "__main__":
    main()