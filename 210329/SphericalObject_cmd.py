import rhinoscriptsyntax as rs

import Rhino 
import System
import scriptcontext as sc

from math import sin
from math import radians
from math import cos

#custom modules

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
            z = cos(Ver)*Radius + CenterZ          



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


    t = float(ColorPercentage)


    R3 = float(R + Rdiff*t)
    G3 = float(G + Gdiff*t)
    B3 = float(B + Bdiff*t)

    Color = rs.CreateColor(R3,G3,B3)
    return (Color)

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
    



__commandname__ = "SphericalObject"

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
    #mark ericson
    #This program draws an object generated from spherical motion


    #set Unit System to Inches
    rs.UnitSystem(8)





    #Program Variables
    Clean = rs.GetString("Delete all objects in your file to start clean y/n?")


    #Main Program
    #############################################################################################################################################
    #Clean the file by deleting all objects
    
    #create an empty list to fill with points on the sphere
    Points = []
    Points2 = []


    if Clean == "y":
        DelSet = rs.AllObjects(True)
        rs.DeleteObjects(DelSet)
        
        Stop = int(rs.GetReal("How many points would you like to make?"))
        RValue1 = int(rs.GetReal("How many  first rotations would you like to make?"))
        RValue2 = int(rs.GetReal("How many  second rotations would you like to make?"))
        RValue3 = int(rs.GetReal("How many  third rotations would you like to make?"))
        Sides = (rs.GetReal("How many sides would you like to have"))
        HorAngle = 360/Sides
        VerAngle = .02
        

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

    
        Vert = rs.AddPoint(pt3[0],pt3[1],pt3[2]+Height)
        Path = rs.AddLine(pts,Vert)
        Surf = rs.ExtrudeCurve(Rail,Path)

        #explode surfaces to list
        SurfSet = rs.ExplodePolysurfaces(Surf)

        #create center 
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
        print(ColorInterval)

        #build a list of color scalars that caps at 1.0sp
        for i in range(len(SurfSet)):
            Col += float(ColorInterval/255.000)
            Cv.append(Col)
            print(Cv)
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

    #turn off ground plan, zoom extents, and set view type to rendered
        rs.ZoomExtents()
        views = rs.ViewNames()
        rs.Command("-GroundPlane ShowPanel No Options On=No Enter Enter")
        for view in views:
            rs.ViewDisplayMode(view,'Rendered')

        CaptureView =rs.GetString("Do you think we should take a picture of this thing and save an obj y/n?")
        if CaptureView == 'y':
            Name = rs.GetString("What Should we call it?")
            Ready = rs.GetString("Set your current viewport to the view you want and make it a square. Ready? y/n")
            if Ready == 'y':
                GetCaptureView(2, str(Name) + "_" + str(int(Red)) + "_" + str(int(Green))+ "_" + str(int(Blue)), "Class_Example")

            SaveObj(Solids,Name,"Class_Example")
            
            WriteTxt([str(Name),"Stop_" + str(Stop) ,"RValue1_" + str(RValue1) ,"RValue2_" + str(RValue2),
                    "RValue3_" + str(RValue3), "Sides_" + str(Sides) , "VerAngle_" + str(VerAngle) , "Radius_" + str(Radius),
                     "Height" + str(Height)  ,"Red_" + str(Red) , "Green_"+ str(Green) , "Blue_" + str(Blue)],
                    Name,"Class_Example")
        else:
            pass
    
    
    #Exit Program and print warning to user
    else:
        print("This command requires a blank file. Please save your work and open a blank template or allow the command to delete everything in your file.")


#Uncomment the RunCommand to test the program from python or run it as a python script.  Otherwise the command must be call from Rhino directly.
#RunCommand(True)



