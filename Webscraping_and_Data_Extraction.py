''' Your job is to extract financial data like historical share price and quarterly revenue reportings 
from various sources using Python libraries and webscraping on popular stocks. 
After collecting this data you will visualize it in a dashboard to identify patterns or trends. 
The stocks we will work with are Tesla and GameStop '''

import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

companies = [{'company': 'Tesla','ticker_symbol': 'TSLA', 'index': 1, 'period': 'max',
              'url': 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'}, 
             {'company': 'GameStop','ticker_symbol': 'GME', 'index': 1, 'period': 'max',
              'url': 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'}]

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

def extract_yf_stock_data(ticker_symbol: str, period: str):
    ticker = yf.Ticker(ticker_symbol)
    table_data = ticker.history(period=period)
    table_data.reset_index(inplace=True)
    return table_data

def extract_pd_revenue_data(url: str, index: int ):
    tables_list = pd.read_html(url)
    table_revenue = tables_list[index]
    table_revenue.columns = ['Date', 'Revenue']
    table_revenue['Revenue'] = table_revenue['Revenue'].str.replace(',|\\$','', regex=True)
    table_revenue.dropna(inplace=True)
    table_revenue = table_revenue[table_revenue['Revenue'] != '']
    return table_revenue

def extract_bs4_revenue_data(url: str, index: int):
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data, 'html5lib')
    
    table_revenue = pd.DataFrame(columns=['Date', 'Revenue'])
    body_list = soup.find_all("tbody")
    body = body_list[index]

    for row in body.find_all('tr'):
        col = row.find_all('td')

        date = col[0].text
        revenue = col[1].text
        
        cell_dataframe = pd.DataFrame.from_records([{'Date': date, 'Revenue': revenue}])
        table_revenue = pd.concat([table_revenue, cell_dataframe], ignore_index=True)

    table_revenue['Revenue'] = table_revenue['Revenue'].str.replace(',|\\$','', regex=True)
    table_revenue.dropna(inplace=True)
    table_revenue = table_revenue[table_revenue['Revenue'] != '']
    return table_revenue


for company in companies:
    table_data = extract_yf_stock_data(company['ticker_symbol'], company['period'])
    # table_revenue = extract_pd_revenue_data(company['url'], company['index'])
    table_revenue = extract_bs4_revenue_data(company['url'], company['index'])

    make_graph(table_data, table_revenue, company['company'])



