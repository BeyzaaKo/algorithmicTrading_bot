import quandl

def get_stock_data(api_key, symbol, start_date=None, end_date=None):
    # Quandl API'si kullanarak veri çekme
    quandl.ApiConfig.api_key = api_key
    data = quandl.get(symbol, start_date=start_date, end_date=end_date)

    return data
