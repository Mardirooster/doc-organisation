import csv
import datetime
import os
import itertools
import calendar
from functools import reduce

def get_date(d, sep=''):
    month_dict = dict([(v,k) for k,v in enumerate(calendar.month_abbr)] + [(v,k) for k,v in enumerate(calendar.month_name)] + [(str(x),x) for x in range(1,13)])
    if sep:
        date = d.split(sep[-1])
    else:
        date = [d]
    if len(date) < 2:
        year = int(date[0])
        return datetime.date(year, 1, 1)

    try:
        month = month_dict[date[0].lstrip('0')]
    except KeyError as err:
        print(d, sep)
        raise KeyError
    if len(date) < 3:
        year = int(date[1])
        return datetime.date(year,month,1)
    else:
        day = int(date[1])
        year = int(date[2])
        return datetime.date(year,month,day)



base_path = 'C:\\Unnamed\\'
files = [os.path.join(base_path, f) for f in os.listdir(base_path) if f.endswith(".csv")]
if __name__ == '__main__':
    max_date_allowed = datetime.datetime.now().date()
    for t in files:
        d = []
        no_d = []
        with open(t, 'r') as f:
            reader = csv.reader(f)
            l = list(reader)

        for pdf, *dates in l:
            date_types = [list(g) for k,g in itertools.groupby(dates,lambda x:x in ('?',)) if not k]
            just_year = [l for l in date_types[-1:] if len(l) > 1]
            date_types = [l for l in date_types[:-1] if len(l) > 1]
            date_sep_tuples = []
            for sep, *dates in date_types:
                date_sep_tuples += map(lambda d: (d,sep), dates)
            try:
                dates = [d for d in [get_date(*t) for t in date_sep_tuples] if d < max_date_allowed]
            except KeyError as err:
                print(pdf, dates)
                raise
            if len(dates):
                dates.sort(reverse=True)
                max_date = dates[0]
                d.append((pdf,  max_date))
            else:
                if len(just_year):
                    try:
                        dates = [d for d in [get_date(t) for t in just_year[0][1:]] if d < max_date_allowed]
                    except KeyError as err:
                        print(pdf, dates)
                        raise
                    dates.sort(reverse=True)
                    max_date = dates[0]
                    d.append((pdf,  max_date))
                else:
                    no_d.append((pdf, '-'))
        #d.sort(key=lambda x: x[1])
        print(len(d), len(no_d))
        print('\n'.join(map(str, d[:100])))
        print('\n'.join(map(str, no_d)))
        
            
