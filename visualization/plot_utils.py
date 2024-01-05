''' Backtest sonuçlarını ve alım-satım sinyallerini görselleştirmek için kullanılan grafik çizme işlevlerini içerir.'''


import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

def plot_prices_with_signals_candlestick(df_lead, df_lag, buy_signal_lead, sell_signal_lead, buy_signal_lag, sell_signal_lag, cerebro):
    # Combine lead and lag data
    df_combined = pd.DataFrame(index=df_lead.index)
    df_combined['Lead Open'] = df_lead['Adj. Open']
    df_combined['Lead High'] = df_lead['Adj. High']
    df_combined['Lead Low'] = df_lead['Adj. Low']
    df_combined['Lead Close'] = df_lead['Adj. Close']
    df_combined['Lag Open'] = df_lag['Adj. Open']
    df_combined['Lag High'] = df_lag['Adj. High']
    df_combined['Lag Low'] = df_lag['Adj. Low']
    df_combined['Lag Close'] = df_lag['Adj. Close']

    # Plot candlestick chart for lead and lag
    mpf.plot(df_combined, type='candle', style='yahoo', ylabel='Price', show_nontrading=True,
             title='Lead and Lag Candlestick Chart with Signals',
             alines=dict(alines=[
                 dict(value=df_combined.index[buy_signal_lead], color='g', linestyle='--', label='Buy Signal Lead'),
                 dict(value=df_combined.index[sell_signal_lead], color='r', linestyle='--', label='Sell Signal Lead'),
                 dict(value=df_combined.index[buy_signal_lag], color='b', linestyle='--', label='Buy Signal Lag'),
                 dict(value=df_combined.index[sell_signal_lag], color='y', linestyle='--', label='Sell Signal Lag'),
             ]))
    plt.show()

def plot_prices_with_signals(df_lead, df_lag, buy_signal, sell_signal, cerebro):
    # Figure 1: Lead ve Lag Grafikleri Bir Arada
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(df_lead['Adj. Close'].values, label='Lead Prices', color='blue')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Lead Prices', color='blue')
    ax1.tick_params('y', colors='blue')

    ax2 = ax1.twinx()
    ax2.plot(df_lag['Adj. Close'].values, label='Lag Prices', color='orange')
    ax2.set_ylabel('Lag Prices', color='orange')
    ax2.tick_params('y', colors='orange')

    plt.title('Lead and Lag Prices Together')
    plt.show()

    # Figure 2: Lead Grafik
    plt.figure(figsize=(10, 6))
    plt.plot(df_lead['Adj. Close'].values, label='Lead Prices', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Lead Prices')
    plt.title('Lead Prices Only')
    plt.show()

    # Figure 3: Lag Grafik
    plt.figure(figsize=(10, 6))
    plt.plot(df_lag['Adj. Close'].values, label='Lag Prices', color='orange')
    plt.xlabel('Time')
    plt.ylabel('Lag Prices')
    plt.title('Lag Prices Only')
    plt.show()

    # Figure 4: Alım Satım Sinyallerini Göster (Lead için)
    plt.figure(figsize=(10, 6))
    plt.plot(df_lead['Adj. Close'].values, label='Lead Prices', color='blue')
    plt.scatter(np.where(buy_signal)[0], df_lead['Adj. Close'][buy_signal], marker='^', color='g', label='Buy Signal Lead')
    plt.scatter(np.where(sell_signal)[0], df_lead['Adj. Close'][sell_signal], marker='v', color='r', label='Sell Signal Lead')
    plt.xlabel('Time')
    plt.ylabel('Lead Prices')
    plt.title('Lead Prices with Buy/Sell Signals')
    plt.legend()
    plt.show()

    # Figure 5: Alım Satım Sinyallerini Göster (Lag için)
    plt.figure(figsize=(10, 6))
    plt.plot(df_lag['Adj. Close'].values, label='Lag Prices', color='orange')
    plt.scatter(np.where(buy_signal)[0], df_lag['Adj. Close'][buy_signal], marker='^', color='g', label='Buy Signal Lag')
    plt.scatter(np.where(sell_signal)[0], df_lag['Adj. Close'][sell_signal], marker='v', color='r', label='Sell Signal Lag')
    plt.xlabel('Time')
    plt.ylabel('Lag Prices')
    plt.title('Lag Prices with Buy/Sell Signals')
    plt.legend()
    plt.show()

    # Figure 6: Lead ve Lag Alım Satım Sinyallerini Birlikte Göster
    plt.figure(figsize=(10, 6))
    plt.plot(df_lead['Adj. Close'].values, label='Lead Prices', color='blue')
    plt.plot(df_lag['Adj. Close'].values, label='Lag Prices', color='orange')
    plt.scatter(np.where(buy_signal)[0], df_lead['Adj. Close'][buy_signal], marker='^', color='g',
                label='Buy Signal Lead')
    plt.scatter(np.where(sell_signal)[0], df_lead['Adj. Close'][sell_signal], marker='v', color='r',
                label='Sell Signal Lead')
    plt.scatter(np.where(buy_signal)[0], df_lag['Adj. Close'][buy_signal], marker='^', color='b',
                label='Buy Signal Lag')
    plt.scatter(np.where(sell_signal)[0], df_lag['Adj. Close'][sell_signal], marker='v', color='y',
                label='Sell Signal Lag')
    plt.xlabel('Time')
    plt.ylabel('Prices')
    plt.title('Lead and Lag Prices with Buy/Sell Signals Together')
    plt.legend()
    plt.show()