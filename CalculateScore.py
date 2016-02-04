import numpy as np
import math
import Queue as Q

# use fully connected topology

def EuclidianDistance(ref, que):
	a = np.array((ref.x, ref.y))
	b = np.array((que.x, que.y))
	e = np.linalg.norm(a-b)
	return e

#Calcurate world centre
def Centre(seq):
	x=0
	y=0
	for i in range(len(seq)):
		x+=seq[i].x
		y+=seq[i].y
	
	return [x/len(seq), y/len(seq)]

def CosSimilarity(a,b):
	return  (np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b)))

def Angle(a, b, c):
	v = a-b
	w = c-b
	t = round(CosSimilarity(v,w),10)
	return math.acos(t)

def Topology(reference, query):
	#find topology of 2 images (priority is distance)
	
	ref = len(reference)	
	que = len(query)

	refCentre = Centre(reference)
	queCentre = Centre(query)

	#Make angle table of 2 topologies
	refAng = [[0 for col in range(ref)] for row in range(ref)]
	queAng = [[0 for col in range(que)] for row in range(que)]
	
	totalScore =0
	for i in range(ref):
		for j in range(ref):
			if i==j : continue
			r1 = np.array((reference[i].x, reference[i].y))
			r2 = np.array((reference[j].x, reference[j].y))
			r_a = math.degrees(Angle(refCentre, r1, r2))
			refAng[i][j] = refAng[j][i] = r_a

			q1 = np.array((query[i].x, query[i].y))
			q2 = np.array((query[j].x, query[j].y))
			q_a = math.degrees(Angle(queCentre, q1, q2))
			queAng[i][j] = queAng[j][i] = q_a
		totalScore+=(CosSimilarity(refAng[i],queAng[i])+1)/2

	return totalScore*100.0/(len(reference))


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

def Distance(reference, query):
	
	ref = len(reference)	
	que = len(query)
	refDist = [[0 for col in range(ref)] for row in range(ref)]
	queDist = [[0 for col in range(que)] for row in range(que)]
	totalScore = 0
	totalConnect = ref*(ref-1)/2

	for i in range(ref):
		for j in range(i):
			r_d = EuclidianDistance(reference[i],reference[j])
			q_d = EuclidianDistance(query[i], query[j])
			t = q_d/r_d
			if t>1 : t=r_d/q_d
			totalScore+=100.0*t/totalConnect

	return totalScore



#Topology, Rotation, Scale
#aT(x) + bR(x) + cS(x)
def Calcurate(reference, query):
	totalScore = 0
	topologyScore = Topology(reference, query)
	rotationScore = Rotation(reference, query)
	distanceScore = Distance(reference, query)
	print topologyScore 
	print rotationScore
	print distanceScore
	totalScore = topologyScore+rotationScore+distanceScore

	return totalScore
