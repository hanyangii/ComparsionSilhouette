#This is main skeleton of ComparisonShillhouette program
from DrawShape import *
import matplotlib.pyplot as plt

class Image:
	def __init__(self, label, x, y, theta):
		self.label=label
		self.x=x
		self.y=y
		self.theta=theta
	
	def __repr__(self):
		return '<{} {} {} {}>'.format(self.label,self.x,self.y,self.theta)

#read input file
inputFile = open("reference.txt",'r')

images = []
referenceNum = int(inputFile.readline())

for i in range(referenceNum):
	line = inputFile.readline()
	if not line: break
	line = line.split(' ')
	image = Image(int(line[0]),float(line[1]),float(line[2]),float(line[3]))
	images.append(image)

DrawReference(images, referenceNum)
