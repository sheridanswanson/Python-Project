#question 1
import yfinance as yf
import pandas as pd
tesla=yf.Ticker("TSLA")
import json
tesla_data=tesla.history(period='max')
tesla_data.head()

#question 3
import yfinance as yf
import pandas as pd
gme=yf.Ticker("GME")
import json
gme_data=gme.history(period='max')
gme_data.head()
