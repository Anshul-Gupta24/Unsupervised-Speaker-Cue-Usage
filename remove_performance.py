import pickle
import os

perf = open('performances.txt','r').read()
perf = perf.split()

vids = []
for csv in os.listdir('../TED/cuts_csv'):
	vids.append(csv)


c=0
for csv in vids:
	for p in perf:
		if p in csv:
			print csv
			os.rename('../TED/cuts_csv/' + csv, '../TED/removed_csv/' + csv)
			c+=1

print ''
print c
