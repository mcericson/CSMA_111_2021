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

def GetCaptureView(Scale,FileName,NewFolder):

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


    color = rs.CreateColor(R3,G3,B3)
    return (color)
    
def SaveObj(Objects,FileName,NewFolder):
    rs.SelectObjects(Objects)
    
    folder = System.Environment.SpecialFolder.Desktop
    path = System.Environment.GetFolderPath(folder)
    #convert foldername and file name sto string
    FName = str(NewFolder)
    File = str(FileName)
    #combine foldername and desktop path
    Dir = System.IO.Path.Combine(path,FName)
    NFolder = System.IO.Directory.CreateDirectory(Dir)
    Dir = System.IO.Path.Combine(Dir,FileName +".obj")
    cmd = "_-Export " + Dir + " _Enter PolygonDensity=1 _Enter"
    rs.Command(cmd)

def WriteTxt(Strings,FileName,FolderName):
    FName = str(FolderName)
    File = str(FileName)
    #combine foldername and desktop path
    folder = System.Environment.SpecialFolder.Desktop
    path = System.Environment.GetFolderPath(folder)
    Dir = System.IO.Path.Combine(path,FName)
    NFolder = System.IO.Directory.CreateDirectory(Dir)
    Dir = System.IO.Path.Combine(Dir,File +".txt")
    myText = open(Dir,"w") 

   
    myString = '\n'.join(Strings)
    myText.write(myString)
    myText.close()



__commandname__ = "RoundThing"

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
    Solid = True
    
    
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
    
        Stop = int(rs.GetReal("How many points would you like to make?", minimum=2, maximum=1000))
    
        RValue1 = int(rs.GetReal("How many first rotations would you like to make?"))
        RValue2 = int(rs.GetReal("How many second rotations would you like to make?"))
        RValue3 = int(rs.GetReal("How many third rotations would you like to make?"))
    
        Sides = int(rs.GetReal("How many sides would you like the first sphere to have?",minimum=3,maximum=30))
        
        HorAngle = 360/Sides
        VerAngle = .01
    
        Radius = rs.GetReal("What radius would you like to use?",minimum=1)
        
        Red   = rs.GetReal("On a scale of 0 - 255, how much do you like red?",minimum = 0, maximum = 255)
        Green = rs.GetReal("On a scale of 0 - 255, how much do you like green?",minimum = 0, maximum = 255)
        Blue  = rs.GetReal("On a scale of 0 - 255, how much do you like blue?",minimum = 0, maximum = 255)
    
    
        Height = rs.GetReal("How thick would you like each step to be?")
    
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
        ColorInterval = float(255.000/(len(SurfSet)))
    
        #build a list of color scalars that caps at 1.0
        for i in range(len(SurfSet)):
            Col += float(ColorInterval/255.000)
            Cv.append(Col)
            color = LinearColor(255,255,255,Red,Green,Blue,Cv[i])
            colors.append(color)
        
        #extrude surfaces towards center.
        Solids = []
        for i in range(len(SurfSet)):
            Solid = rs.ExtrudeSurface(SurfSet[i],Paths[i])
            Mat = rs.AddMaterialToObject(Solid)
            rs.MaterialColor(Mat,colors[i])
            Solids.append(Solid)
        
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
                
                
        #this sets up the instructions for generating an image
        
        CaptureView = rs.GetString("Do you want to take a picture of this round thing? y/n")
        
        if CaptureView == "y":
            FileName  = rs.GetString("What would you like to call this object?")
            NewFolder = FileName
            Ready = rs.GetString("Please be sure your viewport is current and set to an 800 x 800 pixel size. Ready y/n?")
            
            if Ready == "y":
                rs.ZoomExtents()
                rs.Command("-GroundPlane ShowPanel No Options On=No Enter Enter")
    
                GetCaptureView(2,FileName + str(RValue1) +"_"+ str(RValue2) +"_"+ str(RValue3)+str(color),NewFolder)
                
                #WriteTxt(Strings,Filename,Foldername)
                WriteTxt(["File_Name_" + str(FileName),"Stop_" + str(Stop), "Rotations1_" + str(RValue1),"Rotations2_" + str(RValue2),
                "Rotations3_" + str(RValue3), "Sides_" + str(Sides), "Radius_" + str(Radius),
                "Red_" + str(Red),"Green_" + str(Green), "Blue_" + str(Blue),"Height_" + str(Height)],FileName,NewFolder)
            else: 
                pass
        else:
            pass
        SaveObject = rs.GetString("Do you want to export an .obj file of this object y/n?")
        
        if SaveObject == "y":
            SaveObj(Solids,FileName,NewFolder)
        
        
        
        print ("Done. All information is now saved to " + str(NewFolder) + " on your desktop")
    else:
        print("This command requires a blank file.  Please either open a blank file or allow the program to delete all objects")

