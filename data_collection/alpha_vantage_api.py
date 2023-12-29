'''Hisse senedi verilerini çekmek için Alpha Vantage API ile ilgili kodları içeren dosya.'''

from alpha_vantage.timeseries import TimeSeries
import pandas as pd


from alpha_vantage.timeseries import TimeSeries

def get_stock_data(api_key, symbol):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    df = data['4. close']
    return df