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
    HorAngle += radians(1)
    
    #move the drawing to CenterX,CenterY
    translate(CenterX,CenterY)
    
    #construct coordinates on the circle
    x = cos(HorAngle)* Radius 
    y = sin(HorAngle)* Radius 
    z = 0
    
    #append coordinates to list
    X1.append(x)
    Y1.append(y)
    Z1.append(z)
    
    #draw triangle
    stroke(100)
    strokeWeight(.5)
    radius = line(0,0,x,y)
    xline =  line(0,0,x,0)
    yline =  line(x,0,x,y)
    
    textSize(20)
    fill(0)
    text(str((x,y)),x,y)
    
    
    #draw polyline
    stroke(0,0,255)
    strokeWeight(1)
    PolyLine(X1,Y1,Z1)
    
    #condition to end drawing and save image
    if HorAngle >= radians(360):
            save("images/" + str(file_name) + str(second()) + ".jpg" ) 
        
            noLoop()
    
