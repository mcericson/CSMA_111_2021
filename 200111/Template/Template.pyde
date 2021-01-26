#student name date
#project description

import os
from PolyLine import PolyLine

Variables
Width   = 1000
Height  = 1000
CenterX = Width/2
Centery = Height/2

Radius = Width/3


#Global Variables

HorAngle = 0
VerAngle = 0

file_name = os.path.basename(__file__)

def setup():
    #drawing setup
    size(Width,Height,P3D)
    background(255)
    smooth(100)

def draw():
    
    
    
    #condition to end drawing and save image
    if HorAngle >= radians(360):
            save(str("images/" + str(file_name) + str(minute))+ ".jpg")       
        
        noLoop()
    
