import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('ted_main.csv')
df_tr = pd.read_csv('transcripts.csv')

# align transcripts and tags

url1 = df['url'].values
url2 = df_tr['url'].values

indexes = []

for i, u in enumerate(url1):
	if u not in url2:
		indexes.append(i)

df.drop(df.index[indexes], inplace=True)
url1 = df['url'].values
		
print 'total len:', len(df.values)
print 'total len:', len(df_tr.values)


# checks if there are any repeats in the data

unique, counts = np.unique(url2, return_counts=True)
d = dict(zip(unique, counts))
for i in d:
	if d[i]>1:
		print i


# Get tags for every talk

tags = df['tags']

num_rows = df.shape[0]
all_tags=[]
talk_tags = []

for i in range(num_rows):
	
	l=tags.values[i].replace('\'',',')
	l=l.replace('[',',')
	l=l.replace(']',',')
	l = l.split(',')

	l = filter(lambda x: x!='', l)
	l = filter(lambda x: x!=' ', l)

	all_tags.extend(l)
	talk_tags.append(l)

set_tags = set(all_tags)

freq = [all_tags.count(w) for w in set_tags]
tf = {a:i for a,i in zip(set_tags,freq)}


# Prints all tags by frequency of occurence

tf = sorted(tf.iteritems(), key=lambda (k,v): (v,k))
print tf


with open('talk_alltags','wb') as fp:
	pickle.dump(talk_tags,fp)
