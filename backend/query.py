

import pandas as pd
import requests

url = 'https://api.binance.com/api/v3/ticker/price'
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
df = df[['symbol', 'price']]

df.to_excel('savedfile.xlsx')