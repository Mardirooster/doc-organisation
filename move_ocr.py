import os
import shutil


base_path = 'C:\\Unnamed\\'
dirs = [os.path.join(base_path, 'dir'+str(x)) for x in range(29) ][:17]


for d in dirs:
	if os.path.isdir(os.path.join(d, 'pdfs')):
		files = [os.path.join(d, 'pdfs', f) for f in os.listdir(os.path.join(d, 'pdfs')) if f.endswith("ocr.pdf")]

		ocred_pdfs = [os.path.join(d, 'pdfs', '.'.join([f.rsplit('-',1)[0], 'pdf'])) for f in files if os.path.isfile(f)]

		print(d, len(ocred_pdfs), len(files))

		ocr_dir = os.path.join(d, 'ocr-pdfs')
		if not os.path.isdir(ocr_dir):
			os.mkdir(ocr_dir)

		for f, ocr_f in zip(files, ocred_pdfs):
			shutil.move(f, os.path.join(ocr_dir,os.path.basename(f)))
			shutil.move(ocr_f, os.path.join(ocr_dir,os.path.basename(ocr_f)))