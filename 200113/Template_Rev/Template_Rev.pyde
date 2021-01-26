#student name date
#project description

import os
from PolyLine import PolyLine

#Variables
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2

Radius = Width/3


#Global Variables

HorAngle = 0
VerAngle = 0

X1 = []
Y1 = []
Z1 = []



file_name = os.path.basename(__file__)

def setup():
    #drawing setup
    size(Width,Height,P3D)
    background(255)
    smooth(100)

def draw():
    background(255)
    global CenterX, CenterY, HorAngle, VerAngle, Radius,X1,Y1,Z1
    #Add change to global horizontal angle

    #condition to end drawing and save image
    if HorAngle >= radians(360):
            save("images/" + str(file_name) + str(second()) + ".jpg" ) 
        
            noLoop()
    
