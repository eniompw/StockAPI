import csv
import requests

def get_stock_info(company_name):
    """Fetches stock symbol and price for S&P 500 company"""
    try:
        # Get company symbol from S&P 500 list
        sp500_response = requests.get(
            "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv"
        )
        sp500_companies = csv.DictReader(sp500_response.text.splitlines())
        
        # Search for company symbol in S&P 500 list
        company_symbol = None
        for company in sp500_companies:
            company_name_matches = company_name.lower() in company['Security'].lower()
            if company_name_matches:
                company_symbol = company['Symbol']
                break
                
        if not company_symbol:
            return None
            
        # Get current stock price from Yahoo Finance
        yahoo_response = requests.get(
            f"https://query1.finance.yahoo.com/v8/finance/chart/{company_symbol}",
            headers={'User-Agent': 'Python/3.x'}
        )
        stock_data = yahoo_response.json()
        current_price = stock_data['chart']['result'][0]['meta']['regularMarketPrice']
        
        return {
            'symbol': company_symbol,
            'price': current_price
        }
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    """Interactive loop for stock price lookups"""
    while True:
        company_name = input("Enter a company name (or 'q' to exit): ").lower()
        if company_name == 'q':
            break
            
        if stock_info := get_stock_info(company_name):
            formatted_price = f"${stock_info['price']:.2f}"
            print(f"{company_name} ({stock_info['symbol']}): {formatted_price}")
        else:
            print(f"Could not fetch stock information for {company_name}")
        print()

if __name__ == "__main__":
    main()