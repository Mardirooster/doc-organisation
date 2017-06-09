
import os
import shlex, subprocess, multiprocessing
from wand.image import Image
from wand.display import display
from tqdm import tqdm




if __name__ == '__main__':

	dir_path = "C:\\Unnamed\\"

	sort_dir = 'invoice-submission'



	dirs = [os.path.join(dir_path,'dir'+str(x)) for x in range(0,28) if os.path.isdir(os.path.join(dir_path,'dir'+str(x), sort_dir))]
	print(dirs)

	cmd_list = []

	for d in dirs:
		print(d)
		files = [os.path.join(d, f) for f in os.listdir(os.path.join(d, sort_dir)) if f.endswith(".png")]
		
		for file in tqdm(files):
			#convert -density 1000 "Embedding 1_1181.pdf"[2] -resize x4400 -crop 600x400+1050+850 -quality 100 "out/out.png"
			pdf, number = os.path.basename(file).rsplit('.',1)[0].rsplit('-',1)

			filename = os.path.join(d, '.'.join([pdf,'pdf']))
			print(filename)
			if number:
				filename += ''.join(['[', number, ']'])

			with Image(filename=filename, resolution=800) as img:
				img.compression_quality = 100
				with img.convert('png') as converted:
					#img.save(filename=os.path.join(dir_path,sort_dir, 'out', 'out.png'))
					converted.crop(2150, 1750, width=1550, height=1100)
					#converted.sample(620,440)
					outfile = os.path.join(d, 'out', '.'.join([pdf, 'png']))
					print(outfile)
					converted.save(filename=outfile)

			#p.wait()

