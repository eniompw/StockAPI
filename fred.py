from fredapi import Fred
fred = Fred(api_key='YOUR_API_KEY')

target_date = '2023-11-01'
yield_series = fred.get_series('DGS10', target_date)
# yield_series = fred.get_series('DGS10', start_date, end_date)

print(yield_series.iloc[0])