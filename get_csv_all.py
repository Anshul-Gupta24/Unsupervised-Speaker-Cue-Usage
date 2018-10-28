import json
import csv
from pathlib2 import Path
import os



def numdigits(num):

	s = str(num)

	return len(s)



def getzeros(ndigit):

	return '0'* (12 - ndigit)



def get_frames(folder):

	c=0
	for filename in os.listdir(folder):
		c+=1

	return c	


def get_csv(folder):

	numframes = get_frames(folder)
	
	# change!!
	name = folder[]

	csvfile = open('pose_'+name+'.csv','w')

	for n in range(numframes):
		print 'frame '+str(n)
		print ''

		ndigit = numdigits(n)

		filename = folder + '/' + name + '_'+getzeros(ndigit)+str(n)+'_keypoints.json'
		cfile = Path(filename)
		if cfile.is_file():
			f = open(filename)
			data = json.load(f)
			f.close()

			# modify for appropriate person
			person = 0

			pose =  data['people'][person]['pose_keypoints']

			wr = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
			wr.writerow(pose)
		
