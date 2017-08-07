import shlex, subprocess
import os
import re
import csv
import datetime
from tqdm import tqdm


def get_date(d):
	try:
		date = list(map(int, re.split('/|-',d)))
		#return datetime.date(date[2],date[0],date[1])
		return datetime.date(*date)
	except ValueError as err:
		print(d)
		return datetime.date(1900,1,1)


money_reg = r'\b[+-]?[0-9]{1,3}(?:,?[0-9]{3})*\.[0-9]{2}\b'

basedir = 'C:\\Unnamed\\'
date_list_csvs = [os.path.join(basedir,'dir'+str(x)+'-just-dates.csv') for x in range(2,28)]

date_list = []

for date_list_csv in date_list_csvs:
	with open(date_list_csv, 'r') as f:
	    reader = csv.reader(f)
	    date_list += list(reader)

#print(date_list)

maxdate = datetime.date(2014,3,1)

mindate = datetime.date(2012,9,1)

dates_2013 = [f for f,*dates in date_list if any(mindate <= get_date(date) <= maxdate for date in dates)]

texts_2013 = [('.'.join([f.rsplit('.',1)[0],'txt']),f) for f in dates_2013]

transactions_csv = os.path.join(basedir,'transactions.csv')



pdf_amounts = []

for text_file,pdf in texts_2013:
	try:
		with open(text_file, 'r') as f:
			lines = f.readlines()
	except UnicodeDecodeError as err:
		with open(text_file, 'r',encoding="utf8") as f:
			lines = f.readlines()

	matches = [pdf]

	for line in lines:
		match = re.search(money_reg,line)
		if match:
			matches.append(float(match.group(0).replace(',','')))

	pdf_amounts.append(matches)

#print(pdf_amounts[:100])

with open(os.path.join(basedir, '2013 amounts.csv'), 'w+', newline='\n') as f:
	writer = csv.writer(f)
	writer.writerows(pdf_amounts)


# matched_transactions = []

# for transaction in tqdm(transactions[:100]):
# 	amount = get_val(transaction[-1])
# 	pdfs = []
# 	for pdf_amount in pdf_amounts[:200]:
# 		print(amount)
# 		print(pdf_amount)
# 		if amount in pdf_amounts:
# 			pdfs.append(pdf_amount[0])

# 	matched_transactions.append(transaction + pdfs)

# print(matched_transactions)