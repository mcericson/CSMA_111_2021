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

Radius = Width/8

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
    
    #Drawing Y centers on window
    CyObl = -Height/3
    CyTop = 0 
    CyFront = Height/3 #place in the CenterZ paramter
    HorAngle = 90k66
    VerAngle = .5

    
    #find point on circle
    stroke(0)
    strokeWeight(.75)
    
    CircPoints = TrigCirc(HorAngle,VerAngle,Rotation,Radius,0,CyObl,0,"Oblique")
    CircPoints2 = TrigCirc(HorAngle,VerAngle,Rotation,Radius,0,CyTop,0,"Top")
    CircPoints3 = TrigCirc(HorAngle,VerAngle,Rotation,Radius,0,0,CyFront,"Front")
    
    #Oblique
    xo = CircPoints[0]
    yo = CircPoints[1]
    zo = CircPoints[2]
    
    #top
    x = CircPoints2[0]
    y = CircPoints2[1]
    z = CircPoints2[2]
    
    #front
    xf = CircPoints3[0]
    yf = CircPoints3[1]
    zf = CircPoints3[2]
    
    FullSphere = degrees(CircPoints2[4])
    
    PolyLine(X1,Y1,Z1)
    stroke(50)
    strokeWeight(.5)
    #oblique
    Triangle(0,CyObl,0,xo,yo,zo)
    #top
    Triangle(0,CyTop,0,x,y,z)
    #front
    Triangle(0,CyFront,0,xf,yf,zf)
    
    #lines between drawings
    
    stroke(100)
    strokeWeight(.5)
    line(xo,yo,zo,x,y,z)
    line(xf,yf,zf,x,y,z)

    if MakeMovie == True:

        saveFrame("anim/" + "frame"+ "-####.png")
    
    #condition to end drawing and save image
    if FullSphere >= 360*.5:
            save("images/" + str(file_name) + str(second()) + ".jpg" ) 
        
            noLoop()
    
