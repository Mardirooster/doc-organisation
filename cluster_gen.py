
import os
import pickle
import numpy as np
from tqdm import tqdm
from sklearn.cluster import DBSCAN
from collections import defaultdict
from itertools import combinations




def cluster(mat, fnames, eps, min_samples, metric='precomputed'):
	m = DBSCAN(eps=eps, min_samples=min_samples, metric=metric)
	labels = m.fit_predict(mat)
	clusters = defaultdict(list)
	for i, lbl in enumerate(labels):
		clusters[lbl].append(fnames[i])
	return clusters




dir_path = os.path.dirname(os.path.realpath(__file__))
hash_dir = os.path.join(dir_path, "hashes")

matfiles = [os.path.join(hash_dir, f) for f in os.listdir(hash_dir) if f.endswith(".mat")]

details = [(f,) + tuple(f.split('\\')[-1].split('.')[0].split('_')) for f in matfiles]

for filename, directory, size, hashtype in details:
	cluster_filename = '.'.join(['_'.join([directory,size,hashtype]), 'cluster'])