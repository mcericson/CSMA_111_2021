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
import Rhino as rh


#refresh the file by deleting all geometry
delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)


#TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient)

#create an empty list to fill with points on the sphere
Points = []


#Program Variables

Stop = 100

RValue1 = 1
RValue2 = 5
RValue3 = 7

HorAngle = 20
VerAngle = .05

Radius = 100
Height = 5

#create loop that runs the TrigCirc function a certain number of times to generate points on the surface of a sphere

for i in range(1,Stop,1):
    
    rotation1 = RValue1*i
    rotation2 = RValue2*i
    rotation3 = RValue3*i

    pt1 = TrigCirc(-HorAngle,VerAngle,Radius,rotation1,0,0,0,"ThreeD")
    pt2 = TrigCirc(HorAngle/10,VerAngle,Radius/3,rotation2,pt1[0],pt1[1],pt1[2],"ThreeD")
    pt3 = TrigCirc(HorAngle/20,VerAngle,Radius/5,rotation3,pt2[0],pt2[1],pt2[2],"ThreeD")
    
    pts = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    Points.append(pts)

#add polyline to document
Rail = rs.AddPolyline(Points)
Vert = rs.AddPoint(pt3[0],pt3[1],pt3[2]+Height)
Path = rs.AddLine(pts,Vert)
Surf = rs.ExtrudeCurve(Rail,Path)
PlCenter = rs.AddPoint(0,0,pt3[2])

Paths = []
for i in range(len(Points)):
    Path1 = rs.AddLine(Points[i],PlCenter)
    Paths.append(Path1)



SurfSet = rs.ExplodePolysurfaces(Surf)

for i in range(len(SurfSet)):
    rs.ExtrudeSurface(SurfSet[i],Paths[i])

views = rs.ViewNames()
for view in views:
    rs.ViewDisplayMode(view, 'Rendered')

rs.ZoomExtents()



