#This is main skeleton of ComparisonShillhouette program
from DrawShape import *
from CalcurateScore import *
import matplotlib.pyplot as plt

class Shape:
	def __init__(self, label, x, y, theta):
		self.label=label
		self.x=x
		self.y=y
		self.theta=theta
	
	def __repr__(self):
		return '<{} {} {} {}>'.format(self.label,self.x,self.y,self.theta)

#read reference image
referenceFile = open("reference.txt",'r')

referenceImage = []
referenceNum = int(referenceFile.readline())

for i in range(referenceNum):
	referenceLine = referenceFile.readline()
	if not referenceLine: break
	referenceLine = referenceLine.split(' ')
	image = Shape(int(referenceLine[0]),float(referenceLine[1]),float(referenceLine[2]),float(referenceLine[3]))
	referenceImage.append(image)

referencePlt = DrawImage(referenceImage,referenceNum,'red')

#input query image
queryFile = open("query.txt",'r')

queryImage = []
queryNum = int(queryFile.readline())

for i in range(queryNum):
	queryLine = queryFile.readline()
	if not queryLine: break
	queryLine = queryLine.split(' ')
	image = Shape(int(queryLine[0]),float(queryLine[1]),float(queryLine[2]),float(queryLine[3]))
	queryImage.append(image)


queryPlt = DrawImage(queryImage, queryNum,'blue')

referencePlt.show()
queryPlt.show()

#fig, mainPlot = plt.subplots(1,2,sharex=True,sharey=True)
#print referencePlt
#print mainPlot
#mainPlot[0,1].plt(referencePlt)

#Calcurate Score
totalScore=Calcurate(referenceImage, queryImage)
print totalScore
