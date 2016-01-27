#Drawing shapes function. It operate with label
# 1=circle, 2=triangle, 3=square, 4=rectangle
import matplotlib.pyplot as plt
import math

def DrawShape(image):
	print image
	if image.label ==1:
		shape = plt.Circle((image.x, image.y), radius = 3, fc='y')
	elif image.label == 2:
		x=image.x
		y=image.y
		points=[[x-2*math.sqrt(3),y-math.sqrt(3)],[x,y+3],[x+2*math.sqrt(3),y-math.sqrt(3)]]
		shape = plt.Polygon(points, angle=image.theta)
	elif image.label == 3:
		shape = plt.Rectangle((image.x, image.y),3*math.sqrt(2),3*math.sqrt(2),angle=image.theta,fc='r')
	elif image.label == 4:
		shape = plt.Rectangle((image.x, image.y),9*math.sqrt(2),3*math.sqrt(2),angle=image.theta,fc='green')
	
	return shape
	

def DrawReference(images, imageNum):
	plt.axes()
	for i in range(imageNum):
		shape = DrawShape(images[i])
		plt.gca().add_patch(shape)
	plt.axis([0,30,0,30])
	plt.show()
