


hash_lists = [x.hash.tolist() for x in hashes]

test = [zip(*x) for x in list(zip(*hash_lists))]


lambda x: x.count(True) >= (len(x) / 2)


hash_lists = [x.hash.tolist() for x in hashes]
zipped_hashes = [zip(*x) for x in list(zip(*hash_lists))]
average = [map(lambda x: x.count(True) >= (len(x) / 2),x) for x in zipped_hashes]

average_hash = imagehash.ImageHash(np.array(t_average))

files = [os.path.join(dir, f) for f in os.listdir(dir) if f.endswith(".png")]

fnames, hashes = compute_hashes(files, imagehash.phash, hash_name)

with open(out_file, 'wb') as f:
    pickle.dump(zip(fnames,hashes), f, -1)


with open( out_file, 'wb') as f:
    pickle.dump(mat, f, -1)    


clusters = cluster(mat, fnames, eps=7, min_samples=5)

ordered_d = OrderedDict(sorted(clusters.viewitems(), key=lambda x: len(x[1])))


ordered_d = dict(sorted(clusters.items(), key = lambda item : len(item[1]), reverse=true))


convert -density 800 "Embedding 1_1170.pdf"[3] -resize x4400 -crop 800x400+400+800 -quality 100 "out/out.png"