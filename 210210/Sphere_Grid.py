import rhinoscriptsyntax as rs
import math
import Rhino as rh
import random 


delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)

#create an empty list for points and spheres respectively 
points = []
spheres = []
#create a loop to create a grid
for i in range(0,100,20):
    for j in range(0,100,20):
        p = random.randint(1,20)
        pt = rs.AddPoint(i,j,p)
        s = rs.AddSphere(pt,p)
        spheres.append(s)
#union the spheres together and assign them a color)
Mass = rs.BooleanUnion(spheres)for i in Mass:
    Mat = rs.AddMaterialToObject(i)
    rs.MaterialColor(Mat,(12,59,101))


rs.ZoomExtents()
rs.CreatePreviewImage("test.png")


