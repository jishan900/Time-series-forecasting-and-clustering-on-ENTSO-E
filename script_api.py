# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from entsoe import EntsoePandasClient
import pandas as pd

client = EntsoePandasClient(api_key="194685ce-04f3-4822-8293-6af13a07b0b9")

start = pd.Timestamp('2023-03-12 00:00', tz='Europe/Brussels')
end = pd.Timestamp('2024-03-12 23:59', tz='Europe/Brussels')
country_code = 'DE_LU'  # Germany-Luxembourg Bidding Zone
country_code_from = 'DE_LU'  # Assuming transactions or flows within the same market area
country_code_to = 'DE_LU'  # Assuming transactions or flows within the same market area
type_marketagreement_type = 'A01'
contract_marketagreement_type = "A01"
process_type = 'A51'


client.query_day_ahead_prices(country_code, start=start, end=end)
client.query_net_position(country_code, start=start, end=end, dayahead=True)
client.query_generation(country_code, start=start, end=end)


# Retrieve day ahead prices
try:
    day_ahead_prices = client.query_day_ahead_prices(country_code, start=start, end=end)
    print(day_ahead_prices)
except Exception as e:
    print(f"An error occurred fetching day-ahead prices: {e}")

# Retrieve net position
try:
    net_position = client.query_net_position(country_code, start=start, end=end, dayahead=True)
    print(net_position)
except Exception as e:
    print(f"An error occurred fetching net position: {e}")

# Retrieve generation data
try:
    generation_data = client.query_generation(country_code, start=start, end=end)
    print(generation_data)
except Exception as e:
    print(f"An error occurred fetching generation data: {e}")

# Retrieve load data
try:
    load_data = client.query_load(country_code, start=start, end=end)
    print(load_data)
except Exception as e:
    print(f"An error occurred fetching load data: {e}")
    

#client.query_day_ahead_prices(country_code, start=start, end=end)
#client.query_net_position(country_code, start=start, end=end, dayahead=True)
client.query_generation(country_code, start=start, end=end)



import os
path = 'C:/Users/Asifuzzaman.jishan/Downloads/ENTSO-E_API_Py/CSV_data'
os.mkdir(path)

ts = client.query_generation(country_code, start=start, end=end)
ts.to_csv('C:/Users/Asifuzzaman.jishan/Downloads/ENTSO-E_API_Py/CSV_data/expected_csv_data.csv')
print('CSV saved!')
