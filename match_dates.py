import csv
import datetime
import os
import itertools
import calendar
import re
from tqdm import tqdm

base_path = 'C:\\Unnamed\\'
def get_date(d, sep=''):
    try:
        month_dict = dict([(v,k) for k,v in enumerate(calendar.month_abbr)] + [(v,k) for k,v in enumerate(calendar.month_name)] + [(str(x),x) for x in range(1,13)])
        if sep:
            date = d.split(sep[-1])
        else:
            date = [d]
        if len(date) < 2:
            year = int(date[0])
            return datetime.date(year, 1, 1)

        month = month_dict[date[0].lstrip('0')]

        if len(date) < 3:
            year = int(date[1])
            return datetime.date(year,month,1)
        else:
            day = int(date[1])
            year = int(date[2])
            return datetime.date(year,month,day)
    except KeyError as err:
        return None

def get_date(d): return datetime.date(*map(int, re.split('/|-',d)))


files = [os.path.join(base_path, f) for f in os.listdir(base_path) if f.endswith("dates.csv")]

journal_dates = 'C:\\proj\\docsort\\dates.csv'
matched_dates = 'C:\\proj\\docsort\\matched-dates.csv'

with open(journal_dates, 'r') as f:
    reader = csv.reader(f)
    l = list(reader)

with open(matched_dates, 'r') as f:
    reader = csv.reader(f)
    matched_dates_list = list(reader)

last_id_written = matched_dates_list[-1][0]

t = next((i
      for i, entry in enumerate(l)
      if last_id_written in entry),
     None)

del l[:t+1]
print(t)

reduced_csv = matched_dates
reduced_csv_file = open(reduced_csv, 'a+', newline="\n", encoding="utf-8")
file_writer = csv.writer(reduced_csv_file, delimiter=',')

for id, date in tqdm(l):
    try:
        if int(id) > 0:
            line = [id]
            adate = list(map(int, re.split('/|-',date)))
            d = datetime.date(adate[2], adate[0], adate[1])

            for file in files:
                with open(file, 'r') as f:
                    reader = csv.reader(f)
                    fl = list(reader)

                for pdf, *dates in fl:
                    #print(dates)
                    dates = list(map(get_date,dates))
                    if d in dates:
                        line += [pdf]

            file_writer.writerow(line)
    except ValueError as err:
        print(err)
        pass;


