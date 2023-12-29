'''İstatistik arbitraj stratejisini içeren dosya.

Önceki versiyonda, df_lead ve df_lag DataFrame'lerinin içindeki tüm sütunları
kullanıyordunuz. Ancak güncellenmiş versiyonda, sadece kapanış fiyatlarını içeren lead_prices
ve lag_prices dizinlerini kullanmayı tercih ettik. Bu değişiklik, fonksiyonun genel kullanımını
esnek ve sade tutmayı amaçlamaktadır.

-->eski:
def run_stat_arb_strategy(df_lead, df_lag):
    spread = df_lead - df_lag
    mean_spread = spread.mean()
    std_spread = spread.std()

    z_score = (spread - mean_spread) / std_spread

    # Alım Satım Sinyalleri
    buy_signal = z_score < -1.0
    sell_signal = z_score > 1.0

    return buy_signal, sell_signal
Bu fonksiyon, iki DataFrame'i (df_lead ve df_lag) kullanarak spread hesaplamakta ve
ardından z puanını ve alım satım sinyallerini üretmektedir.'''


# import pandas as pd

def run_stat_arb_strategy(df_lead, df_lag):
    # 'close' sütununun yerine gerçek sütun adını kullanın
    spread = df_lead['Adj. Close'].values - df_lag['Adj. Close'].values
    mean_spread = spread.mean()
    std_spread = spread.std()

    z_score = (spread - mean_spread) / std_spread

    # Alım Satım Sinyalleri
    buy_signal = z_score < -1.0
    sell_signal = z_score > 1.0

    return buy_signal, sell_signal




