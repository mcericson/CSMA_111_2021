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

Radius = Width/10

MakeMovie = False

#Global Variables

Rotation = 0
Rotation2 = 0

XO = []
YO = []
ZO = []

XT = []
YT = []
ZT = []

XF = []
YF = []
ZF = []



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
    global CenterX, CenterY, Radius, HorAngle2,Rotation,Rotation2, XO,YO,ZO,XT,YT,ZT,XF,Y5,ZF
    #Add change to global horizontal angle
    
    translate(CenterX,CenterY)

    Rotation += 1
    Rotation2 += 12
    
    
    #Drawing Y centers on window
    CyObl = -Height/3.5
    CyTop = 0 
    CyFront = Height/3.5 #place in the CenterZ paramter
    HorAngle = 20
    VerAngle = .05

    
    #find point on circle
    stroke(0)
    strokeWeight(.75)
    noStroke()
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
    
    
    #SECOND CYCLE
    CircPoints = TrigCirc(HorAngle*-1,VerAngle,Rotation2,Radius/6,xo,yo,zo,"Oblique")
    CircPoints2 = TrigCirc(HorAngle*-1,VerAngle,Rotation2,Radius/6,x,y,z,"Top")
    CircPoints3 = TrigCirc(HorAngle*-1,VerAngle,Rotation2,Radius/6,xf,0,yf,"Front")
    
    #Oblique
    xo2 = CircPoints[0]
    yo2 = CircPoints[1]
    zo2 = CircPoints[2]
    
    #top
    x2 = CircPoints2[0]
    y2 = CircPoints2[1]
    z2 = CircPoints2[2]
    
    #front
    xf2 = CircPoints3[0]
    yf2 = CircPoints3[1]
    zf2 = CircPoints3[2]
    
    stroke(12,59,101)
    strokeWeight(.5)
    XO.append(xo2)
    YO.append(yo2)
    ZO.append(zo2)
    
    XT.append(x2)
    YT.append(y2)
    ZT.append(z2)
    
    XF.append(xf2)
    YF.append(yf2)
    ZF.append(zf2)
    
    
    
    
    
    PolyLine(XO,YO,ZO)
    PolyLine(XT,YT,ZT)
    PolyLine(XF,YF,ZF)
    stroke(50)
    strokeWeight(.5)
    #oblique
    Triangle(0,CyObl,0,xo,yo,zo)
    #top
    Triangle(0,CyTop,0,x,y,z)
    #front
    Triangle(0,CyFront,0,xf,yf,zf)
    
    
    #oblique2
    Triangle(xo2,yo2,zo2,xo,yo,zo)
    #top2
    Triangle(x,y,z,x2,y2,z2)
    #front2
    Triangle(xf,yf,zf,xf2,yf2,zf2)
    
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
    
