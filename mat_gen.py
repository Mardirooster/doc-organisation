#
#	hash pickles are in the form [dirname]_[image size]_[hashtype]
#	and return (fnames,hashes)
#

import os
import pickle
import numpy as np
from tqdm import tqdm
from sklearn.cluster import DBSCAN
from collections import defaultdict
from itertools import combinations

# from cluster.py in imclus
def compute_dists(hashes):
	# precompute distance matrix
	mat = np.zeros((len(hashes), len(hashes)))
	for i, j in tqdm(combinations(range(len(hashes)), 2)):
		dist = hashes[i] - hashes[j]
		mat[i, j] = mat[j,i] = dist
	return mat



base_dir = "C:\\Unnamed\\"
sizes = ['small', 'medium', 'large']

dir_path = os.path.dirname(os.path.realpath(__file__))
hash_dir = os.path.join(dir_path, "hashes")


hashfiles = [os.path.join(hash_dir, f) for f in os.listdir(hash_dir) if f.endswith(".hash")]

details = [(f,) + tuple(f.split('\\')[-1].split('.')[0].split('_')) for f in hashfiles]

for filename, directory, size, hashtype in details:
	# process hashfiles
	mat_filename = '.'.join(['_'.join([directory,size,hashtype]), 'mat'])

	if not os.path.exists(mat_filename):
		with open(filename, 'rb') as f:
			(fnames, hashes) = map(list,(zip(*pickle.load(f))))

		mat = compute_dists(hashes)

		with open(os.path.join(hash_dir, mat_filename), 'wb') as f:
			pickle.dump(mat, f, -1)




