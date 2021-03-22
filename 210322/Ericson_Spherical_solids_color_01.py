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

import LinearColorGradient
from LinearColorGradient import LinearColor
reload(LinearColorGradient)

#import relevant libraries
import rhinoscriptsyntax as rs
import math
import Rhino as rh

Solid = True
CaptureView = False

#refresh the file by deleting all geometry
delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)

rs.UnitSystem(8)

#TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient)

#create an empty list to fill with points on the sphere
Points = []
Points2 = []


#Program Variables

Stop = 3000
RValue1 = 1
RValue2 = 5
RValue3 = 7

HorAngle = -10
VerAngle = .01

Radius = 100
Height = 1

#create loop that runs the TrigCirc function a certain number of times to generate points on the surface of a sphere

for i in range(1,Stop,1):
    
    rotation1 = RValue1*i
    rotation2 = RValue2*i
    rotation3 = RValue3*i
    
    #creat rotations
    pt1 = TrigCirc(-HorAngle,VerAngle,Radius,rotation1,0,0,0,"ThreeD")
    pt2 = TrigCirc(HorAngle,VerAngle,Radius/5,rotation2,pt1[0],pt1[1],pt1[2],"ThreeD")
    pt3 = TrigCirc(HorAngle/2,VerAngle,Radius/7,rotation3,pt2[0],pt2[1],pt2[2],"ThreeD")
    
    #point on the second cycle to extrude to
    pts2 = rs.AddPoint(pt2[0],pt2[1],pt3[2])
    
    #pt on the third cycle to extrude from
    pts = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    
    #list of points on third cycle
    Points.append(pts)
    
    #list of points on second cycle
    Points2.append(pts2)

#add polyline to document
Rail = rs.AddPolyline(Points)

if Solid == True:
    Vert = rs.AddPoint(pt3[0],pt3[1],pt3[2]+Height)
    Path = rs.AddLine(pts,Vert)
    Surf = rs.ExtrudeCurve(Rail,Path)

    #explode surfaces to list
    SurfSet = rs.ExplodePolysurfaces(Surf)

    #creat center 
    Origin = rs.AddPoint(pt2[0],pt2[1],pt2[2])

    #create a list of paths for extrusions
    Paths = []
    for i in range(len(Points)):
        Path2 = rs.AddLine(Points[i],Points2[i])
        Paths.append(Path2)

    Cv = []
    colors = []
    Col = 0

    #color interval per solid
    ColorInterval = 255/(len(SurfSet))

    #build a list of color scalars that caps at 1.0
    for i in range(len(SurfSet)):
        Col += ColorInterval/255
        Cv.append(Col)
        color = LinearColor(255,255,255,12,59,101,Cv[i])
        colors.append((color[0],color[1],color[2]))
    
#extrude surfaces towards center.   
    for i in range(len(SurfSet)):
    
        Solid = rs.ExtrudeSurface(SurfSet[i],Paths[i])
        Mat = rs.AddMaterialToObject(Solid)
        rs.MaterialColor(Mat,colors[i])

#select object by type
    CurvesAll = rs.ObjectsByType(4,True,0)
    PointsAll = rs.ObjectsByType(1,True,0)


    rs.HideObjects(CurvesAll)
    rs.HideObjects(PointsAll)
    rs.HideObjects(Surf)
    rs.HideObjects(SurfSet)

    rs.ZoomExtents()

    views = rs.ViewNames()

    for view in views:
        rs.ViewDisplayMode(view,'Rendered')
    
if CaptureView == True:
    
    GetCaptureView(2,"Spherical_02_" + str(RValue1) +"_"+ str(RValue2) +"_"+ str(RValue3)+str(color), "Class_Example")




