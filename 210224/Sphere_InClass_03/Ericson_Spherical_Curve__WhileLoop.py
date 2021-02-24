#Mark Ericson
#The program makes an object from spherical coordinates

#This updates the custom modules
import Spherical
from Spherical import TrigCirc
from imp import reload
reload(Spherical)


import Rhino as rh

#Import relevant libraries
import rhinoscriptsyntax as rs
import math
import random


delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)

#establish empty list to store pt and polyline
pts = []
Lines = []

Rotation1 = 0
Rotation2 = 0
Rotation3 = 0
Radius = 100

HorAngle = -20
VerAngle = .025

Stop = 1200

Origin = rs.AddPoint(0,0,0)

#create a while loop to update the function 
while Rotation1 <= Stop:

    Rotation1 += 1
    Rotation2 += 6
    Rotation3 += 8
    
    #set the update time for the function
    rs.Sleep(.01)
   
   #create 3 cycles of rotation
    pt1 = TrigCirc(HorAngle,VerAngle,Radius,Rotation1,0,0,0,"ThreeD")
    pt2 = TrigCirc(HorAngle/2,VerAngle,Radius/3,Rotation2,pt1[0],pt1[1],pt1[2],"ThreeD")
    pt3 = TrigCirc(-HorAngle,VerAngle,Radius/5,Rotation3,pt2[0],pt2[1],pt2[2],"ThreeD")
    pt = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    pts.append(pt)

#creat geometry with pts created in the while loop
Rail = rs.AddPolyline(pts)
rs.ObjectPrintWidth(Rail,.2)

rs.ObjectColor(Rail,(12,59,101))
rs.ObjectPrintWidth(Rail,.2)
Vert = rs.AddPoint((pt3[0],pt3[1],pt3[2]+2))
Path = rs.AddLine(pt,Vert)
rs.ExtrudeCurve(Rail,Path)

print("Done")


