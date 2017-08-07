import shlex, subprocess
import os
import re
import csv
import datetime
from tqdm import tqdm

def get_val(v): return float(v.strip('"()').replace(',','').replace('-',''))



basedir = 'C:\\Unnamed\\'

amounts_2013 = os.path.join(basedir, '2013 amounts.csv')
transactions_csv = os.path.join(basedir,'transactions.csv')

transactions_pdfs_csv = os.path.join(basedir, 'transactions_pdfs.csv')


with open(transactions_csv, 'r') as f:
	reader = csv.reader(f)
	transactions = list(reader)

with open(amounts_2013, 'r') as f:
	reader = csv.reader(f)
	pdf_amounts = list(reader)




matched_transactions = []

for transaction in tqdm(transactions):
	amount = get_val(transaction[-1])
	pdfs = []
	for pdf,*amounts in pdf_amounts:

		if amount in map(get_val,amounts):
			pdfs.append(pdf)
	if pdfs:
		matched_transactions.append([transaction] + pdfs)

with open(transactions_pdfs_csv, 'w+', newline='\n') as f:
	writer = csv.writer(f, delimiter=',')
	writer.writerows(matched_transactions)