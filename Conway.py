import random
import sys, pygame
import time

pygame.init()
black = 0, 0, 0
white = 255,255,255

clock = pygame.time.Clock()

Width, Height = 800+1, 800+1
screen = pygame.display.set_mode([Width, Height])
block = 8


Map = []
for y in range(int(Height/block)):
	MapX = []
	for x in range(int(Width/block)):
		MapX.append(random.randint(0,1))
	Map.append(MapX)


def UpdateLife():
	NewMap = []
	for PopulateY in range(len(Map)):
		Add = []
		for PopulateX in range(len(Map[0])):
			Add.append(0)
		NewMap.append(Add)

	for Y in range(len(Map)):
		for X in range(len(Map[Y])):
			Sum = 0
			Alive = False
			for i in [-1,0,1]:
				for i2 in [-1,0,1]:
					if Y+i != -1 and Y+i != len(Map):
						if X+i2 != -1 and X+i2 != len(Map[0]):
							if i == 0 and i2 == 0:
								if Map[Y+i][X+i2] == 1:
									Alive = True
								else:
									Alive = False
							elif Map[Y+i][X+i2] == 1:
								Sum += 1		
			if Sum == 3 and Alive == False:
				NewMap[Y][X] = 1
			elif (Sum == 3 or Sum == 2) and Alive == True:
				NewMap[Y][X] = 1
			elif Sum > 3 and Alive == True:
				NewMap[Y][X] = 0
			elif Sum < 2 and Alive == True:
				NewMap[Y][X] = 0

	for Y in range(len(Map)):
		for X in range(len(Map[Y])):
			Map[Y][X] = NewMap[Y][X]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #Make Map
    	#Horizontal-
    XOri = 0
    XFin = Width
    Y = 0
    YOri = 0
    YFin = Height
    X = 0
    	#-Vertical
    screen.fill(black)
    clock.tick(60)
    
    while (Y < Height):
    	pygame.draw.line(screen,(128,128,128),[XOri, Y], [XFin, Y],1) 
    	pygame.draw.line(screen,(128,128,128),[X, YOri], [X, YFin],1)
    	Y += block
    	X += block
	

    for Y in range(len(Map)):
    	for X in range(len(Map[Y])):
    		if Map[Y][X] == 1:
    			pygame.draw.rect(screen,white, pygame.Rect(X*block,Y*block, block,block))
    
    UpdateLife()
    pygame.display.flip()
    pygame.display.update()




