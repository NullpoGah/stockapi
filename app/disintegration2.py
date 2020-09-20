import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

data = pd.read_csv('./tickers.csv')

def ticker_comparison(requested_company):
    tickers = data['Company'].unique()
    result = process.extract(requested_company, tickers, limit=1, scorer=fuzz.token_sort_ratio)[0]
    if result[1]>66:
        return data.loc[lambda data: data['Company'] == result[0], 'Symbol'].values[0]
    else:
        return False

# print(ticker_comparison('Yandex'))
