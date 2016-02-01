import numpy as np
import Queue as Q

# use Kruskal's algorithm for making topology
# use Priority queue for kruskal's algorithm

def EuclidianDistance(ref, que):
	a = np.array((ref.x, ref.y))
	b = np.array((que.x, que.y))
	e = np.linalg.norm(a-b)
	return e

def Topology(reference, query):
	#find topology of 2 images (priority is distance)
	
	#make referernce image Priority queue
	refQ =  Q.PriorityQueue()
	
	ref = len(reference)	
	for i in range(ref):
		for j in range(i):
			dist = EuclidianDistance(reference[i],reference[j])
			refQ.put((dist, [i, j])) #(distance, [shape #, shape#])
	
	#use check list to prevent from making cycle
	check = [0 for i in range(ref)]
	n=0
	refTop = [[0 for col in range(ref)] for row in range(ref)]
	
	#make Topology table from reference Priority queue
	while n<ref-1:
		tmp = refQ.get()
		x = tmp[1][0]
		y = tmp[1][1]
		if check[x]==1 and check[y]==1 : continue
		else:
			refTop[x][y] = tmp[0]
			refTop[y][x] = tmp[0]
			check[x]=1
			check[y]=1
			n+=1
	
	#make query image Priority queue
	queQ =  Q.PriorityQueue()

	que = len(query)
	for i in range(que):
		for j in range(i):
			dist = EuclidianDistance(query[i], query[j])
			queQ.put((dist, [i,j]))
	
	#use check list to prevent from making cycle
	check = [0 for i in range(que)]
	n=0
	queTop = [[0 for col in range(que)] for row in range(que)]

	#make Topology table from query Priority queue
	while n<que-1:
		tmp = queQ.get()
		x=tmp[1][0]
		y=tmp[1][1]
		if check[x]==1 and check[y]==1 : continue
		else :
			queTop[x][y]=tmp[0]
			queTop[y][x]=tmp[0]
			check[x]=1
			check[y]=1
			n+=1

#Topology, Rotation, Overlap
#aT(x) + bR(x) + cO(x)
def Calcurate(reference, query):
	totalScore = 0
	topologyScore = Topology(reference, query)

	
	totalScore = topologyScore
