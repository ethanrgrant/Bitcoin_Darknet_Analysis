import pandas as pd
import numpy as np

in_path = 'C:/Users/Ethan/Desktop/Columbia/Senior_Spring/Seminar/data/all_data.csv'
out_path = 'C:/Users/Ethan/Desktop/Columbia/Senior_Spring/Seminar/data/all_data.csv'

def do_interp():
    with open(in_path, 'r') as infile:
        df = pd.read_csv(infile)
        print df
        df.replace(0, np.nan)
        print df

        df = df.interpolate()
        print df
    df.to_csv(out_path)
