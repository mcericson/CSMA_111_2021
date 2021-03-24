#mark ericson
#This program draws an object generated from spherical motion

#import relevant libraries
import rhinoscriptsyntax as rs
import math

import Rhino 
import System
import scriptcontext as sc

from math import radians
from math import cos
from math import sin



#custom modules
def TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient):
    

    #loop to create points on sphere
    for i in range(Rotation):
        
        Hor = radians(HorAngle*i)
        Ver = radians(VerAngle*i)
        
        if Orient == "ThreeD":
        
    
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) + CenterY
            z = cos(Ver)*Radius + CenterZ
            
        if Orient == "Top":
            
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) + CenterY
            z = 0 + CenterZ
            
        if Orient == "Front":
        
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = cos(Ver)*Radius + CenterZ
            z = 0 + CenterY
            
        if Orient == "Oblique":
        
    
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) - cos(Ver)*Radius*.9 + CenterZ + CenterY
            z = 0 + CenterZ           



    return(x,y,z)

def CaptureView(Scale,FileName,NewFolder):

    view = sc.doc.Views.ActiveView;
    if view:
        view_capture = Rhino.Display.ViewCapture()
        view_capture.Width = view.ActiveViewport.Size.Width*Scale
        view_capture.Height = view.ActiveViewport.Size.Height*Scale
        view_capture.ScaleScreenItems = False
        view_capture.DrawAxes = False
        view_capture.DrawGrid = False
        view_capture.DrawGridAxes = False
        view_capture.TransparentBackground = False
        bitmap = view_capture.CaptureToBitmap(view)
        if bitmap:
            #locate the desktop and get path
            folder = System.Environment.SpecialFolder.Desktop
            path = System.Environment.GetFolderPath(folder)
            #convert foldername and file name sto string
            FName = str(NewFolder)
            File = str(FileName)
            #combine foldername and desktop path
            Dir = System.IO.Path.Combine(path,FName)
            #creat path to the new folder
            NFolder = System.IO.Directory.CreateDirectory(Dir)
            Dir = System.IO.Path.Combine(Dir,FileName +".png")
            print (Dir)
            #save the file
            bitmap.Save(Dir, System.Drawing.Imaging.ImageFormat.Png);

def LinearColor(R,G,B,R2,G2,B2,ColorPercentage):
    
    #This function defines linear color gradient by treating R,G,B as coordinates on a 3D line.
    #The base color that will be altered by the percentage should be entered in the second R2,G2,B2 valu
    
    Rdiff = R2 - R
    Gdiff = G2 - G
    Bdiff = B2 - B


    t = ColorPercentage


    R3 = float(R + Rdiff*t)
    G3 = float(G + Gdiff*t)
    B3 = float(B + Bdiff*t)



    return (R3,G3,B3)



Solid = True
CaptureView = False

#refresh the file by deleting all geometry

DeleteObjects = rs.GetString("Delete all objects in your file to start clean y/n")

if DeleteObjects == "y":

    delSet = rs.AllObjects(True)
    rs.DeleteObjects(delSet)

    rs.UnitSystem(8)

    #TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient)

    #create an empty list to fill with points on the sphere
    Points = []
    Points2 = []


    #Program Variables

    Stop = int(rs.GetReal("How many points would you like to make?"))

    RValue1 = int(rs.GetReal("How many first rotations would you like to make?"))
    RValue2 = int(rs.GetReal("How many second rotations would you like to make?"))
    RValue3 = int(rs.GetReal("How many third rotations would you like to make?"))

    Sides = int(rs.GetReal("How many sides would you like the first sphere to have?"))
    HorAngle = 360/Sides
    VerAngle = .01

    Radius = rs.GetReal("What radius would you like to use?")
    Height = rs.GetReal("How thick woul you like each step to be?")

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

else:
    print("This command requires a blank file.  Please either open a blank file or allow the program to delete all objects")


