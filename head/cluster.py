import numpy as np
import sklearn.cluster
import get_features

import matplotlib.pyplot as plt


folder = '../TED/'

X = get_features.get_input(folder)

np.savetxt('data.txt',X)

db = sklearn.cluster.KMeans(n_clusters=3).fit(X)
#db = sklearn.cluster.DBSCAN(eps=0.9).fit(X)

means = db.cluster_centers_

print means
print 


X1 = []
X2 = []
X3 = []
X4 = []
X5 = []



labels = db.labels_
f1 = open('labels0.txt','w')
f2 = open('labels1.txt','w')
f3 = open('labels2.txt','w')
f4 = open('labels3.txt','w')
f5 = open('labels4.txt','w')
for i, l1 in enumerate(labels):

        if l1==0:
                f1.write(str(i))
		X1.append(X[i])
                f1.write('\n')

        elif l1==1:
                f2.write(str(i))
		X2.append(X[i])
                f2.write('\n')

        elif l1==2:
                f3.write(str(i))
		X3.append(X[i])
                f3.write('\n')

        elif l1==3:
                f4.write(str(i))
		X4.append(X[i])
                f4.write('\n')

        elif l1==4:
                f5.write(str(i))
		X5.append(X[i])
                f5.write('\n')



print np.argmax(X,0)




X1 = np.array(X1)
X2 = np.array(X2)
X3 = np.array(X3)
X4 = np.array(X4)
X5 = np.array(X5)

X1_norm = np.linalg.norm(X1, axis=1)
print np.argmin(X1_norm)

X2_norm = np.linalg.norm(X2, axis=1)
print np.argmin(X2_norm)
'''
X3_norm = np.linalg.norm(X3, axis=1)
print np.argmin(X3_norm)

X4_norm = np.linalg.norm(X4, axis=1)
print np.argmin(X4_norm)

X5_norm = np.linalg.norm(X5, axis=1)
print np.argmin(X5_norm)
'''


plt.title('Head Movement (TED)')
plt.xlabel('std deviation')
plt.ylabel('speed')
a = plt.scatter(X1[:,0],X1[:,1],c='r')
b = plt.scatter(X2[:,0],X2[:,1],c='g')
c = plt.scatter(X3[:,0],X3[:,1],c='b')
#plt.scatter(X4[:,0],X4[:,1],c='y')
#plt.scatter(X5[:,0],X5[:,1],c='k')

#plt.legend((a,b),('Cluster1', 'Cluster2'))
plt.legend((a,b,c),('Cluster1', 'Cluster2', 'Cluster3'))
plt.show()

print ""
print ""
