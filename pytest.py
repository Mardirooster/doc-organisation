from wand.image import Image
from wand.display import display
import os
import shutil



dir_path = "C:\\Unnamed\\"

dirs = [os.path.join(dir_path,'dir'+str(x)) for x in range(0,28)]

mov_dir = 'unsorted-cat'

for d in dirs:
	if not os.path.isdir(os.path.join(d,mov_dir)):
		os.mkdir(os.path.join(d,mov_dir))

	unsorted_dirs = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o)) and o.replace('-','1').isdigit()]
	for ud in unsorted_dirs:
		shutil.copytree(ud, os.path.join(d,mov_dir,ud.split('\\')[-1]))
		shutil.rmtree(ud)











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