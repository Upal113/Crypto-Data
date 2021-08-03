import requests
import pandas as pd
import datetime as dt
import time
import json
import openpyxl
import numpy


i = 1
coin_data_list = []


while True:
  print(i)
  r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true')
  response = r.json()
  current_price = response['bitcoin']['usd']
  market_cap = response['bitcoin']['usd_market_cap']
  price_change = response['bitcoin']["usd_24h_change"]
  price_volume = response['bitcoin']['usd_24h_vol']
  current_date = dt.datetime.now()

  coin_dict = {
    'Current Price' : current_price,
    'Market Cap' : market_cap,
    'Price Change' : price_change,
    'Price Volume' : price_volume,
    'Date' : current_date,
  }
  coin_data_list.append(coin_dict)
  i = i+1
  coin_df = pd.DataFrame(coin_data_list)
  if i%2==0:
    print(coin_df)
    coin_data_list = []
    data=json.dumps(json.loads(coin_df.to_json(orient='records')), indent=2)
    print(coin_df.to_dict())
    r = requests.post(url='https://sheetdb.io/api/v1/w8gxxz5g2sphr/import/json', data={'json':data})
    print(r.json())
    print(data)
    print(coin_data_list)
  time.sleep(60)  
