import cv2 
import numpy as np
import random



#funcion que detecta interseccion entre objetos

def checkIntersection (selectDots,shapeDots):
	
	
	if len(shapeDots) == 3 and len(selectDots) != 0:
		x1 = shapeDots[0]-shapeDots[2]
		x2 = shapeDots[0]+shapeDots[2]
		y1 = shapeDots[1]-shapeDots[2] 
		y2 = shapeDots[1]+shapeDots[2]
		
		if  selectDots[0]<x2 and selectDots[0] >x1 and selectDots[1]<y2 and selectDots[1]>y1:
			return True	
			
	elif len(shapeDots) == 4 and len(selectDots) != 0:
		x1 = shapeDots[0]
		x2 = shapeDots[1]
		y1 = shapeDots[2]
		y2 = shapeDots[3]
		
		if  selectDots[0]<x2 and selectDots[0] >x1 and selectDots[1]<y2 and selectDots[1]>y1:
			return True	
	
	else :
		return False
		
		
#generar posiciones aleatorias

def generateRandomPositions():
	
	#coordenadas en x
	firstX = 340/2
	secondX = (340 + firstX)/4
	
	#coordenadas en y
	firstY = 220/2
	secondY = (220+firstY)/4
	
	order = { 1: (firstX,firstY) , 2: (firstX,secondY) , 3: (secondX,firstY) , 4: (secondX,secondY)}
	
	lista = []
	while len(lista) < 4:
		rand = random.randint(1,4)
		if len(lista) == 0:
			lista.append(order[rand])
		elif buscarCoordenadas(lista,order[rand]) == False:
			lista.append(order[rand])
			
	return lista
	
#buscar 
def buscarCoordenadas(lista,coordenada):
	
	for i in range (len(lista)):
		if lista[i][0] == coordenada[0]:
			if lista[i][1] == coordenada[1]:
				return True
	return False
	
#generarShapes
def generarShapes(circles,rectangles,randomPositions,MAX):
	shapes = []
	for i in range(len(randomPositions)):
		if len(circles)<MAX:
			circles.append({0:randomPositions[i]})
			continue
		elif len(rectangles)<MAX:
			rectangles.append({1:randomPositions[i]})
			continue
			
def mostrarShapes(circles,rectangles,img):
	for circle in circles:
			cv2.circle(img,circle[0], 10, (255,255,255), -1)
	for rectangle in rectangles:
			cv2.rectangle(img,rectangle[1],(rectangle[1][0]+10,rectangle[1][1]+10),(0,255,0),8)
	
		

"""
print randomPositions
print circles
print rectangles
"""

"""
cont=0
cont1=0
"""

#define las fronteras
lowerBound = np.array([170,70,50])
upperBound = np.array([180,255,255])

#lowerBound=np.array([33,80,40])
#upperBound=np.array([102,255,255])

#captura la imagen
cam = cv2.VideoCapture(0)
#ont = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)

# se aplica un cerrado y un abierto para que se borren los falsos positivos
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

circles = []
rectangles = []
randomPositions = []
contadores = []


randomPositions = generateRandomPositions()
generarShapes(circles,rectangles,randomPositions,2)
print circles

selector=[]
while True:
	
	

	ret,img = cam.read()

	img = cv2.resize(img,(340,220))
	imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	#crea la mascara
	mask = cv2.inRange(imgHSV,lowerBound,upperBound)

	maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
	maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

	#actualuiza la mascara y obtiene los contornos
	maskFinal=maskClose
	extra, conts, h = cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	#cv2.drawContours(img,conts,-1,(255,0,0),3)


	#recorre todos los contornos y les da un numero
	
	for i in range(len(conts)):
		selector=[]
		x,y,w,h=cv2.boundingRect(conts[i])
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
		selector.append(x)
		selector.append(y)
		selector.append(x+w)
		selector.append(y+h)
		
		#cv2.cv.PutText(cv2.cv.fromarray(img), str(i+1),(x,y+h),font,(0,255,255))
		
	print len(selector)
	
	mostrarShapes(circles,rectangles,img)
	  
	"""
	if cont<1:
		cv2.circle(img,(170,110), 10, (255,0,0), -1)
	if cont1<1:
		cv2.rectangle(img,(85,110),(95,120),(0,255,0),8)
	
	
	if checkIntersection(selector,[170,110,10]):
		cont = cont+1
	if checkIntersection(selector,[85,110,95,120]):
		cont1 = cont1+1
	"""
	
	
	
	cv2.imshow("mask",mask)
	cv2.imshow("cam",img)
	cv2.imshow("maskOpen",maskOpen)
	cv2.imshow("maskClose",maskClose)

	cv2.waitKey(10)



	
	
	
