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

#oblique list center
Xoblc = []
Yoblc = []
Zoblc = []

#top list
Xtop = []
Ytop = []
Ztop = []

#top list center
Xtopc = []
Ytopc = []
Ztopc = []

#front list
Xfront = []
Yfront = []
Zfront = []

#front listc
Xfrontc = []
Yfrontc = []
Zfrontc = []


Rotation = 0
Rotation2 = 0
Rotation3 = 0

file_name = os.path.basename(__file__)

def setup():
    #drawing setup
    size(Width,Height,P3D)
    background(255)
    frameRate(30)
    smooth(100)
    

def draw():
    background(255)
    global CenterX, CenterY, Radius,Rotation, Xobl,Yobl,Zobl, Xtop,Ytop,Ztop,Xfront,Yfront,Zfront,Rotation2,Rotation3,Xoblc,Yoblc,Zoblc, Xtopc,Ytopc,Ztopc,Xfrontc,Yfrontc,Zfrontc
    #Add change to global horizontal angle
    
    #Grow the number of rotations
    Rotation  += 1
    Rotation2 += 6
    Rotation3 += 6
    
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
    
    CircPoints4Out = TrigCirc(HorAngle,VerAngle,Radius/8,Rotation3,x,y,z,"Oblique")
    CircPoints5Out = TrigCirc(HorAngle,VerAngle,Radius/8,Rotation3,xt,yt,zt,"Top")
    CircPoints6Out = TrigCirc(HorAngle,VerAngle,Radius/8,Rotation3,xf,0,yf,"Front")
    
    #oblique
    x3= CircPoints4Out[0]
    y3= CircPoints4Out[1]
    z3= CircPoints4Out[2]
    #top
    xt3= CircPoints5Out[0]
    yt3= CircPoints5Out[1]
    zt3= CircPoints5Out[2]
    #front
    xf3= CircPoints6Out[0]
    yf3= CircPoints6Out[1]
    zf3= CircPoints6Out[2]
    
    


    #make polyline list for three views
    Xobl.append(x3)
    Yobl.append(y3)
    Zobl.append(z3)
    #add cycle one to drawing
    Xoblc.append(x)
    Yoblc.append(y)
    Zoblc.append(z)
    
    Xtop.append(xt3)
    Ytop.append(yt3)
    Ztop.append(zt3)
    
    Xfront.append(xf3)
    Yfront.append(yf3)
    Zfront.append(zf3)
    
    
    #draw polyline through list of outer rotation points
    stroke(0)
    strokeWeight(.5)
    PolyLine(Xobl,Yobl,Zobl)
    PolyLine(Xtop,Ytop,Ztop)
    PolyLine(Xfront,Yfront,Zfront)
    
    stroke(255,0,255)
    #cycle 1 
    PolyLine(Xoblc,Yoblc,Zoblc)
    
    #draw triangle
    stroke(50)
    strokeWeight(.3)
    #oblique
    Triangle(0,CyObl,0,x,y,z)
    Triangle(x,y,z,x2,y2,z2)
    #top
    Triangle(0,CyTop,0,xt,yt,zt)
    Triangle(xt,yt,zt,xt2,yt2,zt2)
    #front
    Triangle(0,CyFront,0,xf,yf,zf)
    Triangle(xf,yf,zf,xf2,yf2,zf2)
    
    line(x,y,xf,yf)
    
    Coordinates = str((int(x),int(y)))
    textSize(5)
    text(Coordinates, x,y)
    
    
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


    
