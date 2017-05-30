import sys
import os
from os import listdir
from os.path import isfile, join
import csv
import pickle
from itertools import combinations

import cv2
import numpy as np

from PIL import Image
import imagehash
from sklearn.cluster import DBSCAN
from collections import defaultdict

import argparse
from tqdm import tqdm




def compute_hashes(files, hashfunc=imagehash.whash):
    hashes = []
    fnames = []
    width = os.get_terminal_size().columns
    print("\n")
    print("####### - HASHING - #######".center(width))
    for f in tqdm(files):

        image = Image.open(f)
        hash = hashfunc(image)
        hashes.append(hash)
        fnames.append(f)

    return fnames, hashes


# these two functions are taken from
# from cluster.py in imclus
def compute_dists(hashes):
    # precompute distance matrix
    mat = np.zeros((len(hashes), len(hashes)))
    for i, j in tqdm(combinations(range(len(hashes)), 2)):
        dist = hashes[i] - hashes[j]
        mat[i, j] = mat[j,i] = dist
    return mat

def cluster(mat, fnames, eps, min_samples, metric='precomputed'):
    m = DBSCAN(eps=eps, min_samples=min_samples, metric=metric)
    labels = m.fit_predict(mat)
    clusters = defaultdict(list)
    for i, lbl in enumerate(labels):
        clusters[lbl].append(fnames[i])
    return clusters


def show_clusters(clusters):
    width = os.get_terminal_size().columns
    print("\n\n\t-----------------------------","\n\t  total\t\t:\t",len(fnames),"\n\t-----------------------------")
    for i,cluster in clusters.items():
        print("\t","unsorted\t:" if i < 0 else i, "" if i < 0 else "\t\t:", "\t", len(cluster))
        count = 0
        for f in cluster:
            image = cv2.imread(f)
            small = cv2.resize(image, (0,0), fx=0.2, fy=0.2) 
            cv2.imshow(f,small)
            count += 1
            if count%20 == 0:
                k = cv2.waitKey(0)
                if k == 32:
                    cv2.destroyAllWindows()
                    break
                cv2.destroyAllWindows()
            if count > 100:
                cv2.destroyAllWindows()
                break

        q = cv2.waitKey(0)
        if q == 32:
            break
        cv2.destroyAllWindows()




if __name__ == '__main__':

    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #image_dir = os.path.join(dir_path,'images')

    #image_dir = "C:\\proj\\docsort\\images"

    image_dir = "C:\\Unnamed\\dir0\\pngs"

    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--writefile", help="hash file name to write to, default hashes.csv")
    parser.add_argument("-r", "--readfile", help="hash file name to read from")
    parser.add_argument("-l", "--length", help="number of images to load", type=int)
    args = parser.parse_args()


    # either calculate hashes or read from file
    if not args.readfile:
        files = [f for f in listdir(image_dir) if f.endswith(".png")]
        if args.length:
            files = files[:args.length]

        fnames, hashes = compute_hashes(list(map(lambda x: os.path.join(image_dir, x), files)), imagehash.whash)  #, imagehash.dhash)

        if args.writefile:
            with open(args.writefile, 'wb') as f:
                pickle.dump(zip(fnames,hashes), f, -1)
        
    else:
        with open(args.readfile, 'rb') as f:
            (fnames, hashes) = map(list,(zip(*pickle.load(f))))
            # print(list(map(str,(hashes))))


    
    hash_dict = dict(zip(fnames,hashes))
    mat = compute_dists(hashes)


    #
    #   CLUSTERING BIT: change eps and min_samples to change clustering
    #
    # works pretty well with whash
    clusters = cluster(mat, fnames, eps=7, min_samples=10)

    unsorted = [hash_dict[x] for x in clusters[-1]]

    #mat = compute_dists(unsorted)
    #new_clusters = cluster(mat, clusters[-1], eps=8, min_samples=5)

    #print(clusters)

    #print(clusters[-1])

    #
    #   DISPLAY CLUSTERED IMAGES
    #
    show_clusters(clusters)






