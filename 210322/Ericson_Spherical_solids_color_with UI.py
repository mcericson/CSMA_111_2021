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

Stop = int(rs.GetReal("How many points would you like to make?"))
RValue1 = int(rs.GetReal("How many  first rotations would you like to make?"))
RValue2 = int(rs.GetReal("How many  second rotations would you like to make?"))
RValue3 = int(rs.GetReal("How many  third rotations would you like to make?"))

HorAngle = 360/(rs.GetReal("How many sides would you like to have"))
VerAngle = .01

Radius = rs.GetReal("What radius would you like to use?")
Height = rs.GetReal("How thick would you like the steps to be?")

Red = rs.GetReal("On a scale of 0 to 255, how much do you like red?")
Green = rs.GetReal("On a scale of 0 to 255, how much do you like green?")
Blue = rs.GetReal("On a scale of 0 to 255, how much do you like blue?")


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
        color = LinearColor(255,255,255,Red,Green,Blue,Cv[i])
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

CaptureView =rs.GetString("Do you think we should take a picture of this thing y/n?")
if CaptureView == 'y':
    Name = rs.GetString("What Should we call it?")
    Ready = rs.GetString("Set your current viewport to the view you want and make it a square. Ready? y/n")
    if Ready == 'y':
        GetCaptureView(2, str(Name)+ str(RValue1) +"_"+ str(RValue2) +"_"+ str(RValue3)+str(color), "Class_Example")





