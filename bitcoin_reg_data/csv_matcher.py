import csv
import os
import pandas as pd
import numpy as np

def do_match():
    csv_path = 'C:/Users/Ethan/Desktop/Columbia/Senior_Spring/Seminar/data/'

    with open(os.path.join(csv_path, 'bitcoin_price_data.csv'), 'r') as infile:
        cur_archive = pd.read_csv(infile)
        dates = list(cur_archive['Date'])
        delim = '-'
        dates = [d.split()[0].split(delim)[1].lstrip('0') + '-'  + d.split()[0].split(delim)[2].lstrip('0') + '-'
                 + d.split()[0].split(delim)[0].lstrip('0') for d in dates if len(d.split()[0].split(delim)) == 3]
        print dates
        price = list(cur_archive['Close Price'])

    with open(os.path.join(csv_path, 'gram_summary.csv'), 'r') as infile:
        cur_archive = pd.read_csv(infile)
        dnet_dates = list(cur_archive['Date'])

        dnet_dates = [d.split('/')[0] + '-' + d.split('/')[1].lstrip('0') + '-' + d.split('/')[2] for d in dnet_dates if len(d.split('/'))==3]
        print dnet_dates
        dnet_listings = list(cur_archive['Listings'])
        dnet_price = list(cur_archive['Cost'])

    dd = [d for d in dnet_dates]
    all_data = []
    for idx, date in enumerate(dates):
        #if a valid date
        if date in dnet_dates:
            dd.remove(date)
            i = dnet_dates.index(date)
            all_data.append((date, price[idx], dnet_listings[i], dnet_price[i]))
        else:
            all_data.append([date, price[idx], np.nan, np.nan])

    with open(os.path.join(csv_path, 'all_data.csv'), 'wb') as outfile:
        out = csv.writer(outfile)
        for d in all_data:
            out.writerow(d)
