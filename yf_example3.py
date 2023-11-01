"""yf_example2.py

Example of a function to download stock prices from Yahoo Finance for a specific year.
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(YYYY):
    year =  YYYY
    tic = "QAN.AX"
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    start = f'{year}-01-01'
    end = f'{year+1}-01-01'
    yf_example2.yf_prc_to_csv(tic, pth, start=start, end=end)

if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)