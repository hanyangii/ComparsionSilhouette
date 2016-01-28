#Drawing shapes function. It operate with label
# 1=circle, 2=triangle, 3=square, 4=rectangle
import matplotlib.pyplot as plt
import math
import numpy as np

#Method for drawing shapes
def DrawShape(image, colour):
	print image
	
	#Circle
	if image.label ==1:
		shape = plt.Circle((image.x, image.y), radius = 3, fc=colour)
	
	#Triangle
	elif image.label == 2:
		x=image.x
		y=image.y

		#Equilateral triangle without centre coordinate
		points=np.array(([-1.5*math.sqrt(3),0,1.5*math.sqrt(3)],
						 [-1.5,3,-1.5]))
		angle = math.radians(image.theta)
		
		#roatation matrix
		rotationMatrix = np.array(([math.cos(angle), -math.sin(angle)], 
						  		   [math.sin(angle), math.cos(angle)]))
		
		#Finding rotated coordinate
		points =  np.dot(rotationMatrix,points)	
		
		rotatePoints = points.T
		
		#Move to original centre
		for i in range(len(rotatePoints)):
			rotatePoints[i] = rotatePoints[i]+[x,y]

		shape = plt.Polygon(rotatePoints, fc=colour)
	
	#Square
	elif image.label == 3:
		shape = plt.Rectangle((image.x, image.y),3*math.sqrt(2),3*math.sqrt(2),angle=image.theta,fc=colour)
	
	#Rectangle
	elif image.label == 4:
		shape = plt.Rectangle((image.x, image.y),9*math.sqrt(2),3*math.sqrt(2),angle=image.theta,fc=colour)
	
	return shape
	

def DrawImage(images, imageNum, colour):
	plt.axes()

	#Drawing each shape
	for i in range(imageNum):
		shape = DrawShape(images[i], colour)
		plt.gca().add_patch(shape)

	plt.axis([-20,20,-20,20])
	return plt
