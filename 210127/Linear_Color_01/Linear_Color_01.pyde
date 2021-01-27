#Variables
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2



Radius = 255*2


#Global Variables

from Triangle import Triangle
from PointOnLine import PointOnLine

file_name = os.path.basename(__file__)


def setup():
    
    size(Width,Height,P3D)
    smooth(100)
def draw():
    global Radius
  
    #move the orgin to CenterX CenterY
    translate(CenterX,CenterY)
    #rotate the working space about the x axis
    rotateX(45)
    
    Angle = 0
    x1,y1,z1 = 0,0,0
    
    x2 = (cos(radians(Angle)))*255
    y2 = (sin(radians(Angle)))*255
    z2 = 255
    
    #find the point on a line between 2 points and a scalar
    c = PointOnLine(x1,y1,z1,x2,y2,z2,2)
    
    background(c[0],c[1],c[2])
    
  
    noFill()
    stroke(255)
    ellipse(0,0,Radius,Radius)
    
    x1,y1,z1 = 0,0,0
    

    
    Triangle(x1,y1,z1,x2,y2,z2)
    

    
    translate(c[0],c[1],c[2])
    sphere(5)
