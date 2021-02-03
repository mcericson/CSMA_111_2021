#Mark Ericson
#creating a circle definition
#1.13.21

import os
from PointOnLine import PointOnLine
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

scalar = 0
scalar2 = 1
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
    
    global CenterX, CenterY, Radius,Rotation, scalar2,Xobl,Yobl,Zobl, Xtop,Ytop,Ztop,X,front,Yfront,Zfront,Rotation2, scalar
    #Add change to global horizontal angle
    
    #def PointOnLine (x1,y1,z1,x2,y2,z2,scalar):
    scalar +=.001 
    scalar2 -=.001 
     
    Color1 = PointOnLine(0,255,0,255,0,255,scalar)
    Color3 = PointOnLine(255,0,255,0,255,0,scalar2)
    print (Color1)
    print (Color3)
    
    Color2 = color(Color1[0], Color1[1], Color1[2])
    Color4 = color(Color3[0], Color3[1], Color3[2])
    background(Color4)
    #Grow the number of rotations
    Rotation  += 1
    Rotation2 += 6
    
    #create variable color scale
    
    
    
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
    stroke(Color2)
    strokeWeight(.5)
    PolyLine(Xobl,Yobl,Zobl)
    PolyLine(Xtop,Ytop,Ztop)
    PolyLine(Xfront,Yfront,Zfront)
    
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


    
