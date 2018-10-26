import pandas as pd
import numpy as np
import os
from sklearn import preprocessing
import matplotlib.pyplot as plt


def get_features(root, f):

	df = pd.read_csv(root+'cuts_csv/'+f, header = None)

	num_frames = df.shape[0]
	#print num_frames


	########
	# DROP LAST 10 sec

	#df.drop(df.index[num_frames-250:num_frames], inplace = True)
	#num_frames = num_frames - 250

	if(df.shape[0] < 250):
		return None

	########


	neck_x = df.iloc[:,3:4].values
	neck_y = df.iloc[:,1:2].values
	#neck_conf = df.iloc[:,5:6].values
	nose_y = df.iloc[:,4:5].values
	#nose_conf = df.iloc[:,2:3].values
	shoulder1_x = df.iloc[:,15:16].values
	shoulder2_x = df.iloc[:,6:7].values

	
	### normalize by confidence

	#neck_x = np.multiply(neck_x, neck_conf)
	#neck_y = np.multiply(neck_y, neck_conf)
	#nose_y = np.multiply(nose_y, nose_conf)
	
	###

	
	frames = num_frames

	# get cuts in video clip
	# Removed in favour of more accurate cuts from pyscenedetect tool

	'''
	zoom = nose_y - neck_y

	cuts = []
	for i in range(1,frames):
		if((abs(neck_x[i] - neck_x[i-1])>10) or (abs(zoom[i] - zoom[i-1]) > 10)):
			#if(len(cuts)>0):	
	 			#if((i - cuts[-1])>10):
				#	cuts.append(i)
			#else:
				cuts.append(i)
	cuts.append(frames)
	
	# remove cuts where no person is detected

	#cs=0
	#for ce in cuts:
	#	if(np.sum(neck_x[cs:ce]) == 0):
	#		cuts.remove(ce)

	'''

	# Get cuts in video
	# Obtained using pyscenedetect library

	df_cuts = pd.read_csv(root+'shots/'+f[5:], skiprows=[0])

	cuts = df_cuts['Frame Number (Start)'].values
	cuts = [int(c) for c in cuts]
	#cuts = []
	cuts.append(num_frames)
	#print cuts

	
	# get inverse zoom level for every cut; zoom = (nose_y - neck_y)

	cs = 0
	izoom = {}
	#izoom[cs]=1
	for ce in cuts:

		if (np.mean(nose_y[cs:ce])==0) or (np.mean(neck_y[cs:ce])==0):
			izoom[cs] = 0

		else:
			zoom = np.mean(abs(nose_y[cs:ce] - neck_y[cs:ce]))
			#izoom[cs] = (1 / zoom) * 5
			izoom[cs] = 1
	
	#	print izoom[cs]
	#	izoom[cs]=1
		cs = ce

	#print izoom

	
	def remove_zeros(arr):

		non_zero = []

		for x in arr:
			if(x!=0):
				non_zero.append(x)


		return non_zero
	
	
	####
	
	#	Features
	#	Note: All features are normalized by the inverse of the zoom level

	####



	full_data = remove_zeros(neck_x)
	if(len(full_data)<250):
		return None


	# FEATURE 1: std dev of x axis movement across a cut
	
	cs=0
	neck_x_std = 0
	num_cuts = 0
	for ce in cuts:
		std_nonzero = remove_zeros(neck_x[cs:ce])
		if(((izoom[cs] != 0) and (len(std_nonzero)>(0.5*(ce-cs))))):

			neck_x_temp = remove_zeros(neck_x[cs:ce])
			#neck_x_temp = neck_x[cs:ce]
	
			neck_x_std_temp = np.std(neck_x_temp) * (izoom[cs]) 

			neck_x_std += neck_x_std_temp
			#print 'std', neck_x_std_temp
			num_cuts += 1
		cs = ce

	neck_x_std_mean = neck_x_std 
	if(num_cuts != 0):
		neck_x_std_mean = neck_x_std / num_cuts
	else:
		return None

	#print neck_x_std_mean


	print ''
	print ''


	# FEATURE 2: speed of x axis movement across a cut

	cs = 0
	speed = 0
	frames_used = 0
	for ce in cuts:
		#mean_tmp = np.mean(neck_x[cs:ce])
		speed_nonzero = np.array(remove_zeros(neck_x[cs:ce]))
		if((izoom[cs]!=0) and (len(speed_nonzero)>(0.5*(ce-cs)))):
			#neck_x_speed_temp = abs(neck_x[cs:ce-1] - neck_x[cs+1:ce])
			neck_x_speed_temp = abs(speed_nonzero[:-1] - speed_nonzero[1:])
			#neck_x_speed_temp = remove_zeros(neck_x_speed_temp)
			speed += np.sum(neck_x_speed_temp) * (izoom[cs])
			frames_used += len(neck_x_speed_temp)
			#print 'speed', speed
		cs=ce

	if frames_used == 0:
		return None
	neck_x_speed = speed / frames_used

	#print neck_x_speed
	print ''
	print ''


	'''	
	# FEATURE 3: amount of time a person's side profile is visible


	cs = 0
	side_total = 0
	for ce in cuts:
	
		shoulder_diff = abs(shoulder1_x[cs:ce] - shoulder2_x[cs:ce])
		shoulder_diff *= izoom[cs]
		#print 'sdiff ', len(shoulder_diff)
		for i, s in enumerate(shoulder_diff):
			if s < 20 and s!=0:
				#print (cs + i)
				side_total += 1

		cs = ce


	print 'side ', side_total



	# FEATURE 1: std dev of y axis movement across a cut
	
	cs=0
	neck_y_std = 0
	for ce in cuts:
		neck_y_std += np.std(neck_y[cs:ce]) * izoom[cs] 
		cs = ce


	#neck_y_std_mean = neck_y_std / len(cuts)


	# FEATURE 2: speed of y axis movement across a cut

	cs = 0
	speed = 0
	for ce in cuts:
		neck_y_speed_temp = abs(neck_y[cs:ce-1] - neck_y[cs+1:ce])
		speed += np.sum(neck_y_speed_temp) * izoom[cs] 
		cs=ce

	neck_y_speed = speed / (frames-len(cuts))


	'''


	# FEATURE 3: acceleration of x axis movement across a cut

	cs = 0
	acc = 0
	frames_used = 0
	for ce in cuts:
		#mean_tmp = np.mean(neck_x[cs:ce])
		acc_nonzero = np.array(remove_zeros(neck_x[cs:ce]))
		if((izoom[cs]!=0) and (len(acc_nonzero)>(0.5*(ce-cs)))):
			#neck_x_speed_temp = abs(neck_x[cs:ce-1] - neck_x[cs+1:ce])
			neck_x_speed_temp = abs(acc_nonzero[:1] - acc_nonzero[1:])
			neck_x_acc_temp = abs(neck_x_speed_temp[:-1] - neck_x_speed_temp[1:])
			#neck_x_acc_temp = remove_zeros(neck_x_acc_temp)
			acc += np.sum(neck_x_acc_temp) * izoom[cs]
			frames_used += len(neck_x_acc_temp)
			
		cs=ce

	if frames_used == 0:
		return None
	neck_x_acc = acc / frames_used


	return neck_x_std_mean, neck_x_speed, neck_x_acc#, neck_y_std_mean
	
	
def get_input(root):
	
	#filenames=[]
	#root = './vids_csv/'

	filenames = [] 

	for fname in os.listdir(root+'/cuts_csv'):
		filenames.append(fname)

	#print filenames
	
	vids = open('videos.txt', 'w')

	
	'''
	#filenames = [root+'f1.csv',root+'f2.csv',root+'f3.csv',root+'f4.csv',root+'fn3.csv',root+'fn4.csv',root+'fn5.csv']
	
	for _,_,files in os.walk(folder):
		filenames.extend(files)
		break
	'''	

	num_files = len(filenames)
	num_features = 3
	
	#X = np.zeros((num_files,num_features))
	X = []

	for i,f in enumerate(filenames):
		print f
		feat = get_features(root, f)
		if feat!=None:
			vids.write(f)
			vids.write('\n')
			X.append(list(feat))
			

	X = np.array(X)

	
	#min_max_scaler = preprocessing.MinMaxScaler()
	#standard_scaler = preprocessing.StandardScaler(with_mean=False)

	#X = min_max_scaler.fit_transform(X)
	#X = standard_scaler.fit_transform(X)
	#X = preprocessing.normalize(X)

	mean0 = np.mean(X[:,0])	
	std0 = np.std(X[:,0])
	mean1 = np.mean(X[:,1])	
	std1 = np.std(X[:,1])
	mean2 = np.mean(X[:,2])	
	std2 = np.std(X[:,2])


	#scaler = mean0 / mean1

	#X[:,0] *= 
	#X[:,1] *= scaler
	#X[:,2] *= 0.014

	print mean0
	print std0
	print mean1
	print std1

	out=0
	for i, x in enumerate(X):
		if x[0]>(mean0 + std0*8):
			print i,x
			out+=1		
		
		if x[1]>(mean1 + std1*8):
			print i,x
			out+=1		

		if x[2]>(mean2 + std2*8):
			print i,x
			out+=1		

	print ''
	print out
	print ''

	min_max_scaler = preprocessing.MinMaxScaler()

	X = min_max_scaler.fit_transform(X)

	return X


if __name__ == '__main__':

	X = get_input('../Anshul/')
	#print 'X ', X
	#plt.scatter(X[:,0],X[:,1])	
	#plt.show()
