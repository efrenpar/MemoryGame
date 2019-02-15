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
            x1 = coord[0]+60
            y1 = coord[1]+60
            cv2.rectangle(img,(coord),(x1,y1),(255,0,0),-1)

        
	@staticmethod
	def check_odd(cards):
		pass

class Table():
    def __init__(self):
        self.img = None
        self.cards = {}
        self.dim = {"rows": 3,"cols": 4}
        self.pares = {}
        self.posicion = {}
	
    def initialize_odds(self):
        cont =0
        self.pares = {1:0,2:0,3:0,4:0,5:0,6:0}
        for i in range (0,self.dim['rows']):
            for j in range(0,self.dim['cols']):
                while(cont==0):
                    rand = random.randint(1,6)
                    if self.pares[rand] < 2:
                        self.posicion[(i,j)] = rand
                        self.pares[rand] = self.pares[rand]+1
                        cont=1
                    else:
                        cont=1
                cont=0
                
                
                
            
            
        
        

    def initialize_table(self,sizeX,sizeY):
        cont=0
        for i in range(0,self.dim['cols']):
            coordX = (sizeX/self.dim['cols'])*i
            for j in range (0,self.dim['rows']):
                cont = cont+1
                carta = Card()
                carta.x = i
                carta.y = j
                coordY = (sizeY/self.dim['rows'])*j
                carta.coords = (coordX,coordY)
                #print self.posicion[(i,j)]
                #carta.value = self.posicion[(i,j)]
                self.cards[(i,j)]=carta 
