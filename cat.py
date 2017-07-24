import os
import csv

base_path = 'C:\\Unnamed\\'
dirs = [os.path.join(base_path, 'dir'+str(x)) for x in range(29) ]

for d in dirs:
	cats = [d for d in next(os.walk(d))[1] if d != 'ocr-pdfs']

	pdfs = [f.rsplit('.',1)[0] for f in os.listdir(os.path.join(d,'ocr-pdfs')) if f.endswith('.pdf')]

	pdf_dict = dict(map(lambda x: (x,[]), pdfs))

	for cat in cats:
		files = [file.rsplit('-',1)[0] for file in os.listdir(os.path.join(d,cat)) if file.endswith('.png')]
		for f in files:
			try:
				pdf_dict[f] += [cat]
			except KeyError as err:
				#print(err)
				pass;


	with open(os.path.join(base_path, os.path.basename(os.path.normpath(d))+'-cats.csv'),'w+', newline='\n') as f:
	    w = csv.writer(f)
	    for pdf, categories in pdf_dict.items():
	    	w.writerow([pdf] + categories)
