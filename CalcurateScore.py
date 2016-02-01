import numpy as np

def EuclidianDistance(ref, que):
	a = np.array((ref.x, ref.y))
	b = np.array((que.x, que.y))
	e = np.linalg.norm(a-b)
	return e

def Topology(reference, query):
	#find topology of 2 images (priority is distance)
	
	#make distance table of images
	ref = len(reference)
	refDist=[[0 for col in range(ref)] for row in range(ref)]
	
	for i in range(ref):
		for j in range(ref):
			if i == j : refDist[i][j]=0
			else : refDist[i][j] = EuclidianDistance(reference[i],reference[j])

	que = len(query)
	queDist = [[0 for col in range(que)] for row in range(que)]

	for i in range(que):
		for j in range(que):
			if i == j : queDist[i][j] = 0
			else : queDist[i][j] = EuclidianDistance(query[i],query[j])

	#make Topology table

	refTop = [[0 for col in range(ref)] for row in range(que)]
	queTop = [[0 for col in range(ref)] for row in range(que)]



#Topology, Rotation, Overlap
#aT(x) + bR(x) + cO(x)
def Calcurate(reference, query):
	totalScore = 0
	topologyScore = Topology(reference, query)

	
	totalScore = topologyScore
