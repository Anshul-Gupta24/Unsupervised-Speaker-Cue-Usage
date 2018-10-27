import pandas as pd
import pickle


df = pd.read_csv('/home/anshul/tensorflow/tags/transcripts.csv', encoding='utf8')

urls = df['url'].values

urls = [u[26:-1] for u in urls]

#print urls[2460]

with open('/home/anshul/tensorflow/tags/talk_alltags','rb') as fp:
	talk_tags = pickle.load(fp)

with open('name_url','rb') as fp:
	name_url = pickle.load(fp)

perf = open('performances.txt','w')


keywords = ['live music', 'performance']


for i,t in enumerate(talk_tags):
	for kw in keywords:
		if kw in t:
			actual_url = name_url.get(urls[i])
			if actual_url is not None:
				perf.write(urls[i])
				perf.write('\n')
			break

