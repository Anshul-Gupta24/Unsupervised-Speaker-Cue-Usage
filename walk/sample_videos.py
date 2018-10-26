import random


vids = open('videos.txt','r').read().split()

f = open('labels1.txt','r').read().split()

f = [int(v) for v in f]

f_chosen = random.sample(f,25)


f_new = open('nowalking_vids.txt','w')

for v in f_chosen:

	f_new.write(vids[int(v)])
	f_new.write('\n')
