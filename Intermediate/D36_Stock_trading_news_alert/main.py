import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "_DUMMY_STOCK_API_"
NEWS_API_KEY = "_DUMMY_NEWS_API_"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

# get stock data for tesla
stock_data = response.json()["Time Series (Daily)"]

# convert only stock data to list and remove dates - 0 is yesterday, 1 is day before yesterday
stock_data_list = [n for (k, n) in stock_data.items()]
stock_date = [k for (k, n) in stock_data.items()]

# yesterday's data - yesterday's closing
yesterday_data = stock_data_list[0]
yesterday_close = float(yesterday_data["4. close"])

# day before yesterday's data - day before yesterday's closing
db_yesterday_data = stock_data_list[1]
db_yesterday_close = float(db_yesterday_data["4. close"])

# absolute difference and percentage difference between - yesterday's close and day before yesterday's close
difference = abs(yesterday_close - db_yesterday_close)
percent_diff = (difference / yesterday_close) * 100

#TODO 5. - If percentage is greater than 5 then pget news.
if percent_diff > 0.1:
    news_parameters = {
        "q": "tesla",
        "from": stock_date[0],
        "to": stock_date[0],
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
        
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"][:3]

    print(f"TSLA {percent_diff}% change")
    for n in articles:
        print(n["title"])

