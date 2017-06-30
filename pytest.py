import os
import shutil as s



dir_path = "C:\\Unnamed\\"

dirs = [os.path.join(dir_path,'dir'+str(x)) for x in range(0,28)]

pdf_dirs = [os.path.join(d, 'pdfs') for d in dirs if os.path.isdir(os.path.join(d, 'pdfs'))]



for pdf_dir in pdf_dirs:
	ocr_files = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith('-ocr.pdf')]

	if(ocr_files and not os.path.isdir(pdf_dir.replace('pdfs','ocr-pdfs',1))):
		os.mkdir(pdf_dir.replace('pdfs','ocr-pdfs',1))
	for ocr_file in ocr_files:
		base_file = '.'.join([ocr_file.rsplit('-',1)[0],'pdf'])

		print(base_file)
		try:
			s.move(base_file,base_file.replace('pdfs','ocr-pdfs',1))
			s.move(ocr_file,ocr_file.replace('pdfs','ocr-pdfs',1))
		except s.Error as err:
			print(err)
			pass









# with Image(filename=filename, resolution=800) as img:
# 	img.compression_quality = 100
# 	with img.convert('png') as converted:
# 		#img.save(filename=os.path.join(dir_path,sort_dir, 'out', 'out.png'))
# 		converted.crop(2150, 1750, width=1550, height=1100)
# 		#converted.sample(620,440)
# 		converted.save(filename=os.path.join(dir_path,sort_dir, 'out', 'out.png'))




#for filename, directory, size, hashtype in details:
	#cluster_filename = os.path.join(hash_dir, '.'.join(['_'.join([directory,size,hashtype]), 'cluster']))

	# if not os.path.exists(cluster_filename):
	
#p.show_clusters(*p.cluster(*p.mat_fnames(detail), eps=7, min_samples=5))