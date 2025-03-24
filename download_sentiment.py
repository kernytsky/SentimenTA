#!/usr/bin/env python3

import pandas as pd
from wsb_scanner import WSBScanner
#wsb_scanner import get_swaggy_stocks, get_ape_wisdom, get_trending_stocks
from datetime import datetime

# Call the functions and get the data frames
scanner = WSBScanner()

limit = 100
aw = scanner.get_ape_wisdom(limit)
st = scanner.get_trending_stocks(limit)

# Get the current timestamp
timestamp = datetime.now().strftime('%y%m%d_%H%M%S')

# Save the data frames to CSV files with timestamp
aw.to_csv(f'/Users/andrew/projects/trade/SentimenTA/data/{timestamp}_apewisdom.csv', index=False)
st.to_csv(f'/Users/andrew/projects/trade/SentimenTA/data/{timestamp}_stocktwits.csv', index=False)
