# Mark Ericson 2.08.21
#This program creates single curve from a set of moving spherical coordinates

#This portion of the program imports our custom modules.  They must be reloaded everytime a change is made.
import TrigCircle
from TrigCircle import TrigCirc
from imp import reload
reload(TrigCircle)

#This imports rhinoscript and allows access to all of rhinos tools.
import rhinoscriptsyntax as rs
import math


delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)



#create an empty list to store spheres and points respectively 
Spheres = [] 
Points =  []

#create a for loop to generate i number of points about a sphere and then do things with those points.
for i in range(1,180,1):
    pts = TrigCirc(10,.5,100,i,0,0,0,"ThreeD")
    pt = rs.AddPoint(pts[0],pts[1],pts[2])
    Points.append(pt)


rs.AddPolyline(Points)



rs.ZoomExtents()
rs.CreatePreviewImage("Sphere.png")


