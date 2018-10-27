import random
import sys

num_samples = 25
filename = sys.argv[1]

vids = open('videos.txt','r').read().split()

f = open(filename,'r').read().split()

f = [int(v) for v in f]

f_chosen = random.sample(f,num_samples)


for v in f_chosen:

	print vids[int(v)]


f_new = open('head_vids_new.txt','w')

for v in f_chosen:

	f_new.write(vids[int(v)])
	f_new.write('\n')
