#Mark Ericson
#The program makes an object from spherical coordinates

#This updates the custom modules
import Spherical
from Spherical import TrigCirc
from imp import reload
reload(Spherical)

#Import relevant libraries
import rhinoscriptsyntax as rs
import math
import random

Radius = 200
step = .02

delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)

pts = []

#TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient)
for i in range(1,2000,1):
    
    rotation1  = 1*i
    rotation2  = 5*i
    rotation3  = 7*1
    p = random.randint(10,40)
    pt1 = TrigCirc(10,step,Radius,rotation1,0,0,0,"ThreeD")
    pt2 = TrigCirc(-20,step,Radius/3,rotation2,pt1[0],pt1[1],pt1[2],"ThreeD")
    pt3 = TrigCirc(10,step,Radius/5,rotation3 ,pt2[0],pt2[1],pt2[2],"ThreeD")

    pt = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    pts.append(pt)
origin = rs.AddPoint(0,0,pt3[2])
Rail = rs.AddPolyline(pts)
Vert = rs.AddPoint((pt3[0],pt3[1],pt3[2]+2))
Path = rs.AddLine(pt,origin)
VPath = rs.AddLine(pt,Vert)
Flat = rs.ExtrudeCurve(Rail,Path)
surfaces = rs.ExplodePolysurfaces(Flat)

for i in surfaces:
    rs.ExtrudeSurface(i,VPath)
