import shlex, subprocess
import os
import re
import csv
import datetime
from tqdm import tqdm
import ast

basedir = 'C:\\Unnamed\\'
transactions_pdfs_csv = os.path.join(basedir, 'transactions_pdfs.csv')
pdf_dates_csv = os.path.join(basedir, 'pdf-dates.csv')
common_words = ['transfer', 'hospital']
def rreplace(s, old, new, occurrence):
	li = s.rsplit(old, occurrence)
	return new.join(li)


with open(transactions_pdfs_csv, 'r') as f:
	reader = csv.reader(f)
	transactions_pdfs = list(reader)

with open(pdf_dates_csv, 'r') as f:
	reader = csv.reader(f)
	pdf_dates_list = list(reader)

pdf_dates_dict = {d[0]: d[1:] for d in pdf_dates_list}



reduced_transaction_pdfs = []

for transaction, *pdfs in transactions_pdfs[:100]:
	trans = ast.literal_eval(transaction)

	reduced = [transaction]

	for pdf in pdfs:
		words = [x for x in trans[7].split(' ') if len(x) > 3 and x.lower() not in common_words]

		text_file = rreplace(pdf, 'pdf', 'txt', 1)
		try:
			with open(text_file, 'r') as f:
				lines = f.readlines()
		except UnicodeDecodeError as err:
			with open(text_file, 'r',encoding="utf8") as f:
				lines = f.readlines()



		if any(word in line for word in words for line in lines):
			reduced += [pdf]

	#if len(reduced) == 2:
	if len(reduced) > 1:
		reduced_transaction_pdfs += [reduced]

print(len(reduced_transaction_pdfs))
date_reduced_transaction_pdfs = []

for transaction, *pdfs in reduced_transaction_pdfs:
	datel = ast.literal_eval(transaction)[3].split('/')
	date = datetime.date(int(datel[2]),int(datel[0]),int(datel[1]))

	date_reduced = [transaction]

	days = datetime.timedelta(days=20)

	for pdf in pdfs:
		for pdf_date in pdf_dates_dict[pdf]:
			d = datetime.date(*list(map(int,pdf_date.split('-'))))

			if ((date-days) <= d <= (date+days)):
				print(str(d) + "   " + str(date))
				date_reduced += [pdf]
				break
	if len(date_reduced) > 1:
		date_reduced_transaction_pdfs += [date_reduced]


print(len(date_reduced_transaction_pdfs))


