import os

base_path = 'C:\\Unnamed\\'
dirs = [os.path.join(base_path, 'dir'+str(x)) for x in range(29) ][:1]

for d in dirs:
	cats = [d for d in next(os.walk(d))[1] if d != 'ocr-pdfs']

	pdfs = [f.rsplit('.',1)[0] for f in os.listdir(os.path.join(d,'ocr-pdfs')) if f.endswith('.pdf')]

	pdf_dict = dict(map(lambda x: (x,[]), pdfs))

	print(pdf_dict)

	for cat in cats:
		files = [file.rsplit('-',1)[0] for file in os.listdir(os.path.join(d,cat)) if file.endswith('.png')]
		for f in files:
			print(f)
			try:
				pdf_dict[f] += [cat]
			except KeyError as err:
				print(err)
				pass;


	print(pdf_dict)
