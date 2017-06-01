#import main
import os
import imagehash
import pickle
import imagehash
from PIL import Image
import logging
from tqdm import tqdm

def compute_hashes(files, hashfunc, hashfuncname="HASHING"):
    hashes = []
    fnames = []
    width = os.get_terminal_size().columns
    print("\n")
    print('-'.join(["#######", hashfuncname,  "#######"]).center(width))
    for f in tqdm(files):
        image = Image.open(f)
        try:
            hash = hashfunc(image)
        except OSError as err:
            raise OSError(str(err),f)
        hashes.append(hash)
        fnames.append(f)
    return fnames, hashes





base_dir = "C:\\Unnamed\\"
pngs_dir = "pngs-small"

dir_path = os.path.dirname(os.path.realpath(__file__))
output_dir = os.path.join(dir_path, "hashes")


hash_funcs = {
    'dhash': imagehash.whash,
    'phash': imagehash.phash,
    'whash': imagehash.whash
    }


dirs = ['dir'+str(x) for x in range(29) ]
png_dirs = list(zip([os.path.join(base_dir, d, pngs_dir) for d in dirs],dirs))
existing_png_dirs = [(x,y) for (x,y) in png_dirs if os.path.isdir(x)]

logging.basicConfig(format='%(levelname)s:%(message)s', filename='hash_gen.log',  level=logging.DEBUG)

for png_d,d in existing_png_dirs:
    for hash_name, hash_func in hash_funcs.items():
        out_file_name = '_'.join([d,pngs_dir.split('-')[-1], hash_name])
        out_file = os.path.join(output_dir, out_file_name)

        if not os.path.exists(out_file):
            files = [os.path.join(png_d, f) for f in os.listdir(png_d) if f.endswith(".png")]
            try:
                fnames, hashes = compute_hashes(files, hash_func, hash_name)
                with open(out_file, 'wb') as f:
                    pickle.dump(zip(fnames,hashes), f, -1)
            except OSError as err:
                logging.error(' ... '.join(err.args))
                pass






#clusters = main.main()

#main.show_clusters(clusters)