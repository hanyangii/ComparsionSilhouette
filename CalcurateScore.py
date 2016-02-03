import numpy as np
import math
import Queue as Q

# use fully connected topology

def EuclidianDistance(ref, que):
	a = np.array((ref.x, ref.y))
	b = np.array((que.x, que.y))
	e = np.linalg.norm(a-b)
	return e

def Topology(reference, query):
	#find topology of 2 images (priority is distance)
	
	ref = len(reference)	
	que = len(query)
	refTop = [[0 for col in range(ref)] for row in range(ref)]
	queTop = [[0 for col in range(que)] for row in range(que)]

	for i in range(ref):
		for j in range(i):
			refDist = EuclidianDistance(reference[i],reference[j])
			refTop[i][j]=refDist
			refTop[j][i]=refDist
			queDist = EuclidianDistance(query[i], query[j])
			queTop[i][j]=queDist
			queTop[j][i]=queDist

def CosSimilarity(a,b):
	return  (np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b)))

#Need pair matching!!!!!!!!
#Compare vectors of each shapes by consine similarity
def Rotation(reference, query):
	totalScore = 0.0

	#Calcurate modulo operator
	circleNum = 0
	for i in range(len(reference)):
		if reference[i].label == 1 : 
			circleNum+=1
			continue
		elif reference[i].label==2:
			reference[i].theta = reference[i].theta%120
			query[i].theta = query[i].theta%120
		elif reference[i].label == 3:
			reference[i].theta = reference[i].theta%90
			query[i].theta = query[i].theta%90
		elif reference[i].label==4:
			reference[i].theta = reference[i].theta%180
			query[i].theta = query[i].theta%180
		
		# make vector of theta
		a = np.array((math.cos(reference[i].theta), math.sin(reference[i].theta)))
		b = np.array((math.cos(query[i].theta), math.sin(query[i].theta)))
		totalScore += (CosSimilarity(a,b)+1)/2
	
	return totalScore*100.0/(len(reference)-circleNum)

#Topology, Rotation, Overlap
#aT(x) + bR(x) + cO(x)
def Calcurate(reference, query):
	totalScore = 0
	topologyScore = Topology(reference, query)
	rotationScore = Rotation(reference, query)
	print rotationScore
	totalScore = topologyScore
