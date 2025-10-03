from fredapi import Fred
fred = Fred(api_key='YOUR_API_KEY_HERE')

target_date = '2023-11-01'
yield_series = fred.get_series('DGS10', target_date, target_date)
print(yield_series.iloc[0])