vids_walk = open('vids_probs1.txt','r').read()
vids_walk = vids_walk.split()

vids_nowalk = open('vids_probs0.txt','r').read()
vids_nowalk = vids_nowalk.split()

for cuts in os.listdir(XX):

	for v in vids_nowalk:
		if cuts in v:
			os.rename(XX + cuts, YY + cuts)

	for v in vids_walk:
		if cuts in v:
			os.rename(XX + cuts, YY + cuts)
