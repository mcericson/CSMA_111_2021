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
HorAngle2 = 0
VerAngle = 0

#empty list to store points on circle
x1 = []
y1 = []
z1 = []

file_name = os.path.basename(__file__)

def setup():
    #drawing setup
    size(Width,Height,P3D)
    background(255)
    smooth(100)

def draw():
    background(255)
    global CenterX,CenterY,HorAngle, x1,y1,z1,HorAngle2
    
    R = Height/4
    HorAngle  += 1
    HorAngle2 -= 8
    translate(CenterX,CenterY)
    
    x = cos(radians(HorAngle))*R
    y = sin(radians(HorAngle))*R 
    
    xb = cos(radians(HorAngle2))*R/4 + x
    yb = sin(radians(HorAngle2))*R/4 + y
    strokeWeight(.5)
    stroke(50)
    circle(0,0,R*2)
    circle(x,y,R/2)
    line(0,0,x,y)
    line(x,y,xb,yb)
    
    x1.append(xb)
    y1.append(yb)
    z1.append(0)
    strokeWeight(.75)
    stroke(0)
    PolyLine(x1,y1,z1)
    
    
    
    #condition to end drawing and save image
    if HorAngle >= 360:
        save(str("images/" + str(file_name) + str(minute))+ ".jpg")       
        
        noLoop()
    
