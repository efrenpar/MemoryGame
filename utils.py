import cv2
import numpy as np
import random 

class Card():
    def __init__(self):
        self.is_closed = True
        self.value = 0
        self.x = 0
        self.y = 0
        self.coords = None
    

    def toggle_card(self):
        if self.is_closed:
            self.is_closed = False
        else:
            self.is_closed = True
    
    def cover_draw(self,img,coord):
        if self.is_closed:
            x = coord[0]-20 
            y = coord[1]-20
            x1 = coord[0]+20 
            y1 = coord[1]+20
            cv2.rectangle(img,(x,y),(x1,y1),(255,0,0),-1)
            
    def shape_view(self,img):
        dicType = {1:(255,0,0),2:(255,255,0),3:(0,255,0),4:(255,255,255),5:(102,51,0),6:(102,0,102)}
        print self.value
        if self.value !=0:
            color = dicType[self.value]
            cv2.circle(img,self.coords,20,color,-1)
        
    
    def check_odd(selector,pressed,tabla):
        if pressed == 4 and len(selector)!=0:
            if selector[0] == self.coords[0] and selector[1] == self.coords[1]:
                valor=tabla.posicion[(self.x,self.y)] 
                if tabla.pares[valor]>0:
                    tabla.pares[valor] = tabla.pares[valor]-1
                    self.is_closed = False
                

class Table():
    def __init__(self):
        self.img = None
        self.cards = {}
        self.dim = {"rows": 3,"cols": 4}
        self.pares = {1:0,2:0,3:0,4:0,5:0,6:0}
        self.posicion = {(0,0):0,(0,1):0,(0,2):0,(0,3):0,(1,0):0,(1,1):0,(1,2):0,(1,3):0,(2,0):0,(2,1):0,(2,2):0,(2,3):0}
        
	
    def initialize_odds(self):
        cont =0
        for i in range (0,self.dim['rows']):
            for j in range(0,self.dim['cols']):
                print('pares que deberian haber:',(i,j))
                while(cont==0):
                    rand = random.randint(1,6)
                    print ('aleatorio',rand)
                    if self.pares[rand] < 2:
                        print ('pares que hay',(i,j))
                        self.pares[rand] = self.pares[rand]+1
                        print('valor de cada par existente',self.pares[rand])
                        self.posicion[(i,j)] = rand 
                        cont=1
                    else:
                        cont=1
                print self.posicion
                cont=0
                
                
            
            
        
        

    def initialize_table(self,sizeX,sizeY):
        for i in range(0,self.dim['rows']):
            coordX = ((sizeX/self.dim['rows'])*i)+10
            for j in range (0,self.dim['cols']):
                carta = Card()
                carta.x = i
                carta.y = j
                coordY = ((sizeY/self.dim['cols'])*j)+10
                carta.coords = (coordX,coordY)
                #print self.posicion[(i,j)]
                carta.value = self.posicion[(i,j)]
                self.cards[(i,j)]=carta
                
    
            
