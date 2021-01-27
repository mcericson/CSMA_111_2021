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

MakeMovie = False

#Global Variables

Rotation = 0
Rotation2 = 0

X1 = []
Y1 = []
Z1 = []



file_name = os.path.basename(__file__)

def setup():
    #drawing setup
    size(Width,Height,P3D)
    ortho()
    background(255)
    smooth(100)
    frameRate(30)
    

def draw():
    background(255)
    global CenterX, CenterY, Radius,X1,Y1,Z1, HorAngle2,Rotation,Rotation2
    #Add change to global horizontal angle
    
    translate(CenterX,CenterY)

    Rotation += 1
    Rotation2 += 2
    
    rotateX(radians(Rotation))
    
    #rotateX(radians(Rotation))
    
    #find point on circle
    stroke(0)
    strokeWeight(.75)
    CircPoints = TrigCirc(10,.5,Rotation,Radius,0,0,0)
    
    x = CircPoints[0]
    y = CircPoints[1]
    z = CircPoints[2]
    
    FullSphere = degrees(CircPoints[4])
    
    PolyLine(X1,Y1,Z1)
    stroke(50)
    strokeWeight(.5)
    Triangle(0,0,0,x,y,z)

    if MakeMovie == True:

        saveFrame("anim/" + "frame"+ "-####.png")
    
    #condition to end drawing and save image
    if FullSphere >= 360*4:
            save("images/" + str(file_name) + str(second()) + ".jpg" ) 
        
            noLoop()
    
