#student name date
#project description

import os
from PolyLine import PolyLine

#Global Variables
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2

Radius = Width/3

MakeMovie = True

x1 = []
y1 = []
z1 = []

HorAngle = 0
VerAngle = 0

file_name = os.path.basename(__file__)

def setup():
    #drawing setup
    size(Width,Height,P3D)
    background(255)
    smooth(100)

def draw():
    background(255)
    global CenterX,CenterY, Width, Height, Radius, HorAngle, x1,y1,z1
    translate(CenterX,CenterY)
    
    HorAngle += 1
    # calculating the points on a circle
    x = cos(radians(HorAngle))*Radius
    y = sin(radians(HorAngle))*Radius
    
    x1.append(x)
    y1.append(y)
    z1.append(0)
    
    stroke(12,59,101)
    strokeWeight(1)
    PolyLine(x1,y1,z1)
    
    # # strokeWeight(.5)
    # # stroke(100)
    # # line(0,0,x,y)
    # # line(0,0,x,0)
    # # line(x,y,x,0)
    
    # textSize(20)
    # fill(0)
    
    x2 = int(x)
    y2 = int(y)
    text(str((x2,y2)),x,y)
    

    
    if MakeMovie == True:

        saveFrame("anim/" + "frame"+ "-####.png")
    
    
    
    #condition to end drawing and save image
    if HorAngle >= 360*4:
            save(str("images/" + str(file_name) + str(minute))+ ".jpg")       
        
            noLoop()
    
