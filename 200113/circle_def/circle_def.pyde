
#Mark Ericson January 13, 2021
#Points on a circle

import os

#bring in drawing modules
from TrigCirc import TrigCirc
from PolyLine import PolyLine
from Triangle import Triangle 


#Global variables
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2

Radius = Width/4

Frame = 0
HorAngle = 0
HorAngle2 = 0
HorAngle3 = 0
VerAngle = 0

#empty list in which to store x,y and z coordinate of polyline
X1 = []
Y1 = []
Z1 = []

#this gets the file name 
file_name = os.path.basename(__file__)

#the set-up of the drawing
def setup():
    
    size(Width,Height,P3D)
    background(255)
    smooth(100)
    frameRate(30)

#Processing's built in loop.  Everything inside the loop resets each time it runs. 
#its metric is frames per second.

def draw():
    global Radius, CenterX, CenterY, X1, Y1, Z1, HorAngle, VerAngle, Frame,HorAngle2,HorAngle3
    
    translate(CenterX,CenterY)
    background(255)   
    noFill()
    
    #create increments and add them to the global value.  
    #each value will increase by the increment with every refresh or frame.
    #this means that increment of 1 at 60 frames per second will reach the value of 60 after 1 second.
    
    HorAngle +=  2
    if HorAngle >= 360:
        HorAngle2 += -5 +1
    else:
        HorAngle2 += -5    
        HorAngle3 += -7
    
    #draw the circles
    Circ = TrigCirc(HorAngle,Radius,Radius,0,0)
    
    #retrieve the coordinates from the function
 
    x = Circ[0]
    y = Circ[1]
    z = Circ[2]
    
    Circ2 = TrigCirc(HorAngle2,Radius/4,Radius/4,x,y)
    
    x1 = Circ2[0]
    y1 = Circ2[1]
    z1 = Circ2[2]
    
    Circ3 = TrigCirc(HorAngle3,Radius/4,Radius/4,x1,y1)
    
    x2 = Circ3[0]
    y2 = Circ3[1]
    z2 = Circ3[2]
    
    
    #append the coordinates to the empty lists setup in globals
    X1.append(x2)
    Y1.append(y2)
    Z1.append(z2)
    
    #draw the triangles
    stroke(50)
    strokeWeight(.5)
    
    Rotation1 = Triangle(0,0,x,y)

    Rotation2 = Triangle(x,y,x1,y1)

    Rotation3 = Triangle(x1,y1,x2,y2)

    #draw the new curve
    stroke(0)
    strokeWeight(1)
    PolyLine(X1,Y1,Z1)
    
    #label the point
    fill(0)
    textSize(20)
    text(str(int(HorAngle/360)),x,y)
    noFill()
    
    
   #end drawing when condition reached
    if HorAngle >= 720*2:
        #saves and image of the drawing with a unique timestamp
        save("images/" + str(file_name) + str(second())+ ".jpg")       
        
        noLoop()
        
    



    
    
    
    
    
    
    
    
    
    
    
