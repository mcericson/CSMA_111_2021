import rhinoscriptsyntax as rs
import Rhino 
import System
import os

import scriptcontext as sc


center = rs.AddPoint(0,0,0)

circle = rs.AddCircle(center,100)

def CaptureView(Scale,FileName,FileType):
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
            
            #folder = rs.WorkingFolder()
            folder = System.Environment.SpecialFolder.Desktop

            path = System.Environment.GetFolderPath(folder)

            path2 = System.IO.Directory.CreateDirectory("/image")

            filename = System.IO.Path.Combine(path, "/image" , str(FileName) + str(FileType));
            bitmap.Save(filename, System.Drawing.Imaging.ImageFormat.Png);

CaptureView(2,"Test",".jpeg")