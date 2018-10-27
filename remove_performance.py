import pickle
import os

perf = open('performances2.txt','r').read()
perf = perf.split()

vids = []
for csv in os.listdir('../Anshul/cuts_csv'):
	vids.append(csv)


c=0
for csv in vids:
	for p in perf:
		if p in csv:
			print csv
			os.rename('../Anshul/cuts_csv/' + csv, '../Anshul/removed_csv/' + csv)
			c+=1

print ''
print c
