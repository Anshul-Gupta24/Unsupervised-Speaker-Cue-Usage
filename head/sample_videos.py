import random


vids = open('videos.txt','r').read().split()

f = open('labels1.txt','r').read().split()

f = [int(v) for v in f]

f_chosen = random.sample(f,50)


for v in f_chosen:

	print vids[int(v)]


f_new = open('head_vids_new.txt','w')

for v in f_chosen:

	f_new.write(vids[int(v)])
	f_new.write('\n')
