import numpy as np

def compareDistance(ref, que):
	a = np.array((ref.x, ref.y))
	b = np.array((que.x, que.y))
	e = np.linalg.norm(a-b)
	return e

def Distance(reference, query):
	totalScore = 0

	for i in range(len(reference)):
		if i == len(reference)-1: j=0
		else : j=i+1
		totalScore+=(compareDistance(reference[i], reference[j])-compareDistance(query[i], query[j]))/compareDistance(reference[i], reference[j])
	
	totalScore*=100
	print totalScore
	return totalScore

def Calcurate(reference, query):
	Score = 0
	DistanceScore = Distance(reference, query)

	Score+=DistanceScore
