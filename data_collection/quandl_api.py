# quandl_api.py

import quandl

def get_stock_data(api_key, symbol):
    # Quandl API'si kullanarak veri çekme
    quandl.ApiConfig.api_key = api_key
    data = quandl.get(symbol)

    return data
