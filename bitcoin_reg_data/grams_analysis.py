import os

def do_analysis():
    archive_path = 'C:/Users/Ethan/Desktop/Columbia/Senior_Spring/Seminar/data/grams/'
    archive_map = {}
    for day in os.listdir(archive_path):
        day_cost = 0
        day_listings = 0
        for archive in os.listdir(os.path.join(archive_path, day)):
            if archive in archive_map:
                archive_map[archive] += 1
            else:
                archive_map[archive] = 1
    for archive in archive_map:
        if archive_map[archive] >= 90:
            print archive
