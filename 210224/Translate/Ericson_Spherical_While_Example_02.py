#mark ericson
#This program draws an object generated from spherical motion


#import custom modules
import Spherical
from Spherical import TrigCirc
from imp import reload
reload(Spherical)
import CaptureView
from CaptureView import GetCaptureView
reload(CaptureView)

#import relevant libraries
import rhinoscriptsyntax as rs
import math
import Rhino as rh


#refresh the file by deleting all geometry
delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)

#Program Variables
HorAngle = 20
VerAngle = .025
Radius   = 100
height = 2

Stop = 0

Rotation1 = 0
Rotation2 = 0
Rotation3 = 0

H = 1

pts = []
while H > Stop:
    
    Rotation1 += 1
    Rotation2 += 6
    Rotation3 += 8

    
    pt1 = TrigCirc(HorAngle,VerAngle,Radius,Rotation1,0,0,0,"ThreeD")
    pt2 = TrigCirc(HorAngle,VerAngle,Radius/3,Rotation2,pt1[0],pt1[1],pt1[2],"ThreeD")
    pt3 = TrigCirc(HorAngle,VerAngle,Radius/5,Rotation3,pt2[0],pt2[1],pt2[2],"ThreeD")
    pt = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    pts.append(pt)
    H += pt3[2]
Rail = rs.AddPolyline(pts)

#appearance
rs.ObjectPrintWidth(Rail,.2)
rs.ObjectColor(Rail,(255,100,100))

vert = rs.AddPoint(pt3[0],pt3[1],pt3[2]+ height)
Path = rs.AddLine(pt,vert)
Surf = rs.ExtrudeCurve(Rail,Path)

