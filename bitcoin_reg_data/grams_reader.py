import csv
import datetime as dt
import pandas as pd
import os


def do_grams():
    archive_path = 'C:/Users/Ethan/Desktop/Columbia/Senior_Spring/Seminar/data/grams/'
    out_path = 'C:/Users/Ethan/Desktop/Columbia/Senior_Spring/Seminar/data/gram_summary.csv'
    num_days = len(os.listdir(archive_path))
    print num_days
    day_map = {}
    day_list = os.listdir(archive_path)
    dates = [dt.datetime.strptime(ts, "%Y-%m-%d") for ts in day_list if len(ts.split('-'))==3]
    sorteddates = [dt.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]
    archive_map = {}
    for day in sorteddates:
        for archive in os.listdir(os.path.join(archive_path, day)):
            with open(os.path.join(archive_path, day, archive), 'r') as infile:
                try:
                    cur_archive = pd.read_csv(infile)
                    if archive in archive_map:
                        archive_map[archive].append((len(cur_archive['price']), sum(cur_archive['price'])))
                    else:
                        archive_map[archive] = [(len(cur_archive['price']), sum(cur_archive['price']))]
                except:
                    print str(os.path.join(archive_path, day, archive))
    avg_map = {}
    for archive in archive_map:
        lens = [l[0] for l in archive_map[archive]]
        sums = [l[1] for l in archive_map[archive]]
        avg_map[archive] = (sum(lens)/float(len(lens)), sum(sums)/len(sums))

    for day in sorteddates:
        day_cost = 0
        day_listings = 0
        for archive in archive_map:
            if archive in os.listdir(os.path.join(archive_path, day)):
                with open(os.path.join(archive_path, day, archive), 'r') as infile:
                    try:
                        cur_archive = pd.read_csv(infile)
                        day_listings += len(cur_archive['price'])
                        day_cost += sum(cur_archive['price'])
                    except:
                        print str(os.path.join(archive_path, day, archive))
            else:
                day_listings += avg_map[archive][0]
                day_cost += avg_map[archive][1]
        day_map[day] = [day_listings, day_cost]

    with open(out_path, 'wb') as csvfile:
        out = csv.writer(csvfile)
        for day in sorteddates:
            out.writerow([day, day_map[day][0], day_map[day][1]])
