import os
import csv


vendor_file = 'C:\\proj\\docsort\\vendors.csv'

base_path = 'C:\\Unnamed\\'
category_files = [os.path.join(base_path, 'dir'+str(x) + '-cats.csv') for x in range(29) ]

with open(vendor_file, 'r') as f:
    reader = csv.reader(f)
    vendor_list = list(reader)