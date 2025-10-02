from fredapi import Fred

fred = Fred(api_key='YOUR_API_KEY')
target_date = '2023-11-01'

# Get the yield as a pandas Series for your date
yield_series = fred.get_series('DGS10', observation_start=target_date, observation_end=target_date)

if not yield_series.empty:
    print(f"Yield on {target_date}: {yield_series.iloc[0]}%")
else:
    print(f"No data for {target_date}.")
