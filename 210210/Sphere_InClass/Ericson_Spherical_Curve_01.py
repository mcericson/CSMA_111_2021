#Mark Ericson
#The program makes an object from spherical coordinates

#This updates the custom modules
import Spherical
from Spherical import TrigCirc
from imp import reload
reload(Spherical)

#Import relevant libraries
import rhinoscriptsyntax as rs
import math
import random


delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)


#TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient)
for i in range(1,180,1):
    p = random.randint(10,40)
    pt = TrigCirc(10,.5,100,i,0,0,0,"ThreeD")
    
    pts = rs.AddPoint(pt[0],pt[1],pt[2])
    rs.AddSphere(pts,p)