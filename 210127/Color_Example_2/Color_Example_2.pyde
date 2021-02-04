
#imports

from PointOnLine import PointOnLine
from Slider import Slider

#Global Variables
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2

scalar = 0
scalar2 = 1







file_name = os.path.basename(__file__)


def setup():
    
    size(Width,Height,P3D)
    smooth(100)
    
def draw():
    
    global CenterX, CenterY, scalar, scalar2
    
    background(255)
    
    #move origin to center of viewport
    translate(CenterX,CenterY)
    
    #rotate the viewport about the x axis
    rotateX(radians(45))
    
    scalar  +=.001
    scalar2 -=.01
    
    Color = PointOnLine(100,0,255,0,0,255,scalar)
    
    Color2 = PointOnLine(100,0,255,0,0,255,scalar2)
    
    print Color
    
    print Color2
    
    ColorS1 = color(Color[0],Color[1],Color[2])
    
    ColorS2 = color(Color2[0],Color2[1],Color2[2])


    
    noFill()
    stroke(ColorS2)
    sphere(300)
    fill(ColorS1)
    stroke(255)
    sphere(100)
    

    #noLoop()
