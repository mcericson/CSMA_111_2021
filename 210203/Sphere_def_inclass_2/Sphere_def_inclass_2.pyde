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

HorAngle = 0
HorAngle2 = 0
HorAngle3 = 0

Add = 0
CouVerAngle = 0

#oblique list
Xobl = []
Yobl = []
Zobl = []

#top list
Xtop = []
Ytop = []
Ztop = []

#front list
Xfront = []
Yfront = []
Zfront = []


Rotation = 0
Rotation2 = 0

file_name = os.path.basename(__file__)

def setup():
    #drawing setup
    size(Width,Height,P3D)
    background(255)
    frameRate(30)
    smooth(100)
    

def draw():
    background(255)
    global CenterX, CenterY, Radius,Rotation, Xobl,Yobl,Zobl, Xtop,Ytop,Ztop,X,front,Yfront,Zfront,Rotation2
    #Add change to global horizontal angle
    
    #Grow the number of rotations
    Rotation  += 1
    Rotation2 += 6
    
    #Center of Drawings on Sheet
    CyObl = -Height/3.25
    CyTop = 0
    CyFront = Height/3.25
    
    HorAngle = -20
    VerAngle = -.05
    
    translate(CenterX,CenterY)
    
    #rotateX(radians(Rotation))
    
    #find point on circle
    #first cycle
    #def TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ)
    noStroke()
    CircPoints = TrigCirc(HorAngle,VerAngle,Radius,Rotation,0,CyObl,0,"Oblique")
    CircPoints2 = TrigCirc(HorAngle,VerAngle,Radius,Rotation,0,CyTop,0,"Top")
    CircPoints3 = TrigCirc(HorAngle,VerAngle,Radius,Rotation,0,0,CyFront,"Front")
    
    #oblique
    x= CircPoints[0]
    y= CircPoints[1]
    z= CircPoints[2]
    #top
    xt= CircPoints2[0]
    yt= CircPoints2[1]
    zt= CircPoints2[2]
    #front
    xf= CircPoints3[0]
    yf= CircPoints3[1]
    zf= CircPoints3[2]
    
    
    #second cycle
    #def TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ)
    noStroke()

    CircPointsOut = TrigCirc(-HorAngle,VerAngle,Radius/6,Rotation2,x,y,z,"Oblique")
    CircPoints2Out = TrigCirc(-HorAngle,VerAngle,Radius/6,Rotation2,xt,yt,zt,"Top")
    CircPoints3Out = TrigCirc(-HorAngle,VerAngle,Radius/6,Rotation2,xf,0,yf,"Front")
    
    #oblique
    x2= CircPointsOut[0]
    y2= CircPointsOut[1]
    z2= CircPointsOut[2]
    #top
    xt2= CircPoints2Out[0]
    yt2= CircPoints2Out[1]
    zt2= CircPoints2Out[2]
    #front
    xf2= CircPoints3Out[0]
    yf2= CircPoints3Out[1]
    zf2= CircPoints3Out[2]


    #make polyline list for three views
    Xobl.append(x2)
    Yobl.append(y2)
    Zobl.append(z2)
    
    Xtop.append(xt2)
    Ytop.append(yt2)
    Ztop.append(zt2)
    
    Xfront.append(xf2)
    Yfront.append(yf2)
    Zfront.append(zf2)
    
    
    #draw polyline through list of outer rotation points
    stroke(0)
    strokeWeight(.5)
    PolyLine(Xobl,Yobl,Zobl)
    PolyLine(Xtop,Ytop,Ztop)
    PolyLine(Xfront,Yfront,Zfront)
    
    #draw triangle
    stroke(50)
    strokeWeight(.3)
    #oblique
    Triangle(0,CyObl,0,x,y,z)
    #top
    Triangle(0,CyTop,0,xt,yt,zt)
    #front
    Triangle(0,CyFront,0,xf,yf,zf)
    
    line(x,y,xf,yf)
    
    FullSphere = degrees(CircPoints[4]) 

    
    #add text to point
    
    textSize(10)
    fill(0)
    noFill()
  
    
    

    if MakeMovie == True:
        saveFrame("anim/" + "frame" + "-####.png")
    
    
    if abs(FullSphere) >= 90.0:
        
        noLoop()
    
    print FullSphere


    
