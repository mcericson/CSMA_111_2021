
#Mark Ericson
#A program to create a grid of random spheres
#2.10.21

import rhinoscriptsyntax as rs
import random

#refresh file by removing all geometry
delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)

points = []
spheres = []
for i in range(0,100,20):
    for j in range(0,100,20):
        p = random.randint(0,20)
        pt = rs.AddPoint(i,j,p)
        Sphere = rs.AddSphere(pt,p)
        spheres.append(Sphere)
        points.append(pt)
        
Mass = rs.BooleanUnion(spheres)

for i in Mass:
    Mat = rs.AddMaterialToObject(i)
    rs.MaterialColor(Mat,(12,59,101))
    
rs.ZoomExtents()
rs.CreatePreviewImage("Ericson.jpg")