
import os
import pickle
import numpy as np
from tqdm import tqdm
from sklearn.cluster import DBSCAN
from collections import defaultdict
from itertools import combinations
import shutil




def cluster(mat, fnames, eps, min_samples, metric='precomputed'):
    m = DBSCAN(eps=eps, min_samples=min_samples, metric=metric)
    labels = m.fit_predict(mat)
    clusters = defaultdict(list)
    for i, lbl in enumerate(labels):
        clusters[lbl].append(fnames[i])
    return clusters

def mat_fnames(filename, directory, size, hashtype):
    hash_path = os.path.join(hash_dir, '.'.join(['_'.join([directory,size,hashtype]), 'hash']))
    with open(hash_path, 'rb', -1) as f:
        (fnames, _) = map(list,(zip(*pickle.load(f))))
    with open(filename, 'rb', -1) as f:
        mat = pickle.load(f)
    return mat, fnames

def move_clusters(clusters, filedir):
    for name, cluster in clusters.items():
        directory = os.path.join(filedir, str(name))
        if not os.path.exists(directory):
            os.mkdir(directory)
        for f in cluster:
            try:
                shutil.move(f, directory)
            except OSError as err:
                pass



hash_algo = "phash"
filepath = "C:\\Unnamed\\"



dir_path = os.path.dirname(os.path.realpath(__file__))
hash_dir = os.path.join(dir_path, "hashes")

matfiles = [os.path.join(hash_dir, f) for f in os.listdir(hash_dir) if f.endswith(".mat")]

details = [(f,) + tuple(f.split('\\')[-1].split('.')[0].split('_')) for f in matfiles if hash_algo in f]
print(details)

for filename, directory, size, hashtype in details:
  cluster_filename = os.path.join(hash_dir, '.'.join(['_'.join([directory,size,hashtype]), 'cluster']))

  if not os.path.exists(cluster_filename):
      dirpath = os.path.join(filepath,directory)
      is_not_clustered = os.path.isdir(os.path.join(dirpath, 'pngs-medium'))
      print(os.path.join(dirpath, 'pngs-medium'))
      print(is_not_clustered)
      if is_not_clustered:
          clusters = cluster(*mat_fnames(filename, directory, size, hashtype), eps=7, min_samples=5)
          move_clusters(clusters, dirpath)
