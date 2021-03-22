#mark ericson
#This program draws an object generated from spherical motion


#import custom modules
import Spherical3D
from Spherical3D import TrigCirc
from imp import reload
reload(Spherical3D)

import CaptureView_jpg
from CaptureView_jpg import GetCaptureView
reload(CaptureView_jpg)

import LinearColorGradient
from LinearColorGradient import LinearColor
reload(LinearColorGradient)

#import relevant libraries
import rhinoscriptsyntax as rs
import math
import Rhino as rh

#Save Drawing

Capture = False


#refresh the file by deleting all geometry
delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)


#TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient)

#create an empty list to fill with points on the sphere
Points  = []
PointsI = []


#Program Variables

Stop = 1000

RValue1 = 1
RValue2 = 3
RValue3 = 9

HorAngle = -20
VerAngle = .02

Radius = 100
Height = 5

#create loop that runs the TrigCirc function a certain number of times to generate points on the surface of a sphere

for i in range(1,Stop,1):
    
    rotation1 = RValue1*i
    rotation2 = RValue2*i
    rotation3 = RValue3*i

    pt1 = TrigCirc(-HorAngle,VerAngle,Radius,rotation1,0,0,0,"ThreeD")
    pt2 = TrigCirc(HorAngle/3,VerAngle,Radius/3,rotation2,pt1[0],pt1[1],pt1[2],"ThreeD")
    pt3 = TrigCirc(HorAngle/2,VerAngle,Radius/5,rotation3,pt2[0],pt2[1],pt2[2],"ThreeD")
    
    ptsI = rs.AddPoint(pt2[0],pt2[1],pt2[2])
    pts = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    Points.append(pts)
    
    #create list of points to generate extrusion path
    PointsI.append(ptsI)

#add polyline to document
Rail = rs.AddPolyline(Points)
Vert = rs.AddPoint(pt3[0],pt3[1],pt3[2]+Height)
Path = rs.AddLine(pts,Vert)
Surf = rs.ExtrudeCurve(Rail,Path)
#explode surfaces to list
SurfSet = rs.ExplodePolysurfaces(Surf)
#creat center 
Origin = rs.AddPoint(pt2[0],pt2[1],pt3[2])

#create a list of paths for extrusions
Paths = []
for i in range(len(Points)):
    
    Path1 = rs.AddLine(Points[i],PointsI[i])
    Paths.append(Path1)

#empty list to store colors and values
ColorVal = []
Colors = []
Col = 0

#color interval per solid
ColorInterval = 255/(len(SurfSet))

for i in range(len(SurfSet)):
    Col += ColorInterval/255
    ColorVal.append(Col)
    color = LinearColor(255,255,255,255,0,0,ColorVal[i])
    Colors.append(color)


#extrude surfaces towards cener.
for i in range(len(SurfSet)):
    
    Solid = rs.ExtrudeSurface(SurfSet[i],Paths[i])
    Mat = rs.AddMaterialToObject(Solid)
    rs.MaterialColor(Mat,Colors[i])

CurvesAll = rs.ObjectsByType(4,True,0)
PointsAll = rs.ObjectsByType(1,True,0)

rs.HideObjects(CurvesAll)
rs.HideObjects(PointsAll)

rs.HideObjects(Surf)
rs.HideObjects(SurfSet)

views = rs.ViewNames()

for view in views:
    rs.ViewDisplayMode(view,'Rendered')
    
rs.ZoomExtents()

if Capture == True:
    
    GetCaptureView(2,"Spherical" + "_" + str(RValue1) + "_" + str(RValue2) + "_" + str(RValue3),"210224")

