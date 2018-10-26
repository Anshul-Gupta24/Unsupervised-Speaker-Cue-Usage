import numpy as np


probs0 = open('vids_probs0.txt','r').read()
probs0 = probs0.split()
probs0 = np.array([float(x) for x in probs0])

probs1 = open('vids_probs1.txt','r').read()
probs1 = probs1.split()
probs1 = np.array([float(x) for x in probs1])

top_n = 25

print probs0.argsort()[-top_n:][::-1]
max_probs0 =  probs0.argsort()[-top_n:][::-1]
print probs1.argsort()[-top_n:][::-1]
max_probs1 =  probs1.argsort()[-top_n:][::-1]

vids = open('videos.txt', 'r').read()
vids = vids.split()

vids_probs0 = [vids[i] for i in max_probs0]
vids_probs1 = [vids[i] for i in max_probs1]

v_probs0 = open('cutsvids_probs0.txt','w')
v_probs1 = open('cutsvids_probs1.txt','w')

for v in vids_probs0:
	v_probs0.write(v)
	v_probs0.write('\n')

for v in vids_probs1:
	v_probs1.write(v)
	v_probs1.write('\n')

print vids_probs0
print ''
print ''
print ''
print vids_probs1
