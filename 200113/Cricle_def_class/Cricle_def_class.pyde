#Mark Ericson
#creating a circle definition
#1.13.21

import os
from PolyLine import PolyLine
from TrigCirc import TrigCirc
from Triangle import Triangle

#Globale Variables
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2

Radius = Width/5



#Global Variables

HorAngle = 0
HorAngle2 = 0
HorAngle3 = 0

Add = 0
CouVerAngle = 0

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
    global CenterX, CenterY, HorAngle, VerAngle, Radius,X1,Y1,Z1, HorAngle2, HorAngle3, Add
    #Add change to global horizontal angle
    
    translate(CenterX,CenterY)

    Add += 1
    
    if HorAngle >= radians(360):
 
        HorAngle += radians(1)
        HorAngle2 += radians(2)
        HorAngle3 = radians(60 + Add)
        
    else:

        HorAngle += radians(1)
        HorAngle2 += radians(2)
        HorAngle3 += radians(3)
        
    
    #find point on circle
    CircPoints = TrigCirc(HorAngle,Radius,0,0)
    
    x= CircPoints[0]
    y= CircPoints[1]
    z= CircPoints[2]
    
    CircPoints2 = TrigCirc(HorAngle2,Radius/6,x,y)
    
    x2= CircPoints2[0]
    y2= CircPoints2[1]
    z2= CircPoints2[2]
    
    CircPoints3 = TrigCirc(HorAngle3,Radius/6,x2,y2)
    
    x3= CircPoints3[0]
    y3= CircPoints3[1]
    z3= CircPoints3[2]
    
    
    CircPoints4 = TrigCirc(HorAngle2,Radius/4,x3,y3)
    
    x4= CircPoints4[0]
    y4= CircPoints4[1]
    z4= CircPoints4[2]
    
    
    
    #append points to list
    X1.append(x4)
    Y1.append(y4)
    Z1.append(z4)
    
    #draw polyline through list of points
    stroke(0)
    strokeWeight(.75)
    PolyLine(X1,Y1,Z1)
    
    #draw triangle
    stroke(50)
    strokeWeight(.5)
    Triangle(0,0,x,y)
    Triangle(x,y,x2,y2)
    Triangle(x2,y2,x3,y3)
    Triangle(x3,y3,x4,y4)
    
    #add text to point
    
    textSize(10)
    fill(0)
    text(str(HorAngle),x3,y3)
    noFill()
  
    
    
    print Add
    
    
    

    #condition to end drawing and save image
    if HorAngle >= radians(360*6):
            save("images/" + str(file_name) + str(second()) + ".jpg" ) 
        
            noLoop()
    
