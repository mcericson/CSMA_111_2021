#mark ericson
#This program draws an object generated from spherical motion


#import custom modules
import Spherical
from Spherical import TrigCirc
from imp import reload
reload(Spherical)

#import relevant libraries
import rhinoscriptsyntax as rs
import math


#refresh the file by deleting all geometry
delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)


#TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient)

#create an empty list to fill with points on the sphere
Points = []

#create loop that runs the TrigCirc function a certain number of times to generate points on the surface of a sphere.
for i in range(1,180,1):
    
    rotation1 = 1*i
    rotation2 = 5*i
    rotation3 = 7*i

    pt1 = TrigCirc(20,.1,100,rotation1,0,0,0,"ThreeD")
    pt2 = TrigCirc(20,.1,100/3,rotation2,pt1[0],pt1[1],pt1[2],"ThreeD")
    pt3 = TrigCirc(20,.1,100/5,rotation3,pt2[0],pt2[1],pt2[2],"ThreeD")
    
    pts = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    Points.append(pts)

#add polyline to document
Rail = rs.AddPolyline(Points)