
#Mark Ericson January 11, 2021
#Points on a circle

from PolyLine import PolyLine
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2

Radius = Width/4

Frame = 0
HorAngle = 0
VerAngle = 0

X1 = []
Y1 = []
Z1 = []


def setup():
    
    size(Width,Height,P3D)
    background(255)
    smooth(100)
    frameRate(60)

def draw():
    global Radius, CenterX, CenterY, X1, Y1, Z1, HorAngle, VerAngle, Frame
    
    translate(CenterX,CenterY)


    background(255)   
    noFill()
    

    HorAngle +=1
    

    
    x = cos(radians(HorAngle))* Radius
    y = sin(radians(HorAngle))* Radius
    z = Frame
    stroke(50)
    strokeWeight(.75)
    X1.append(x)
    Y1.append(y)
    Z1.append(z)
    
    fill(0)
    textSize(20)
    text(str((int(x),int(y))),x,y)
    noFill()
    
    line(0,0,x,y)
    line(0,0,x,0)
    line(x,0,x,y)
    
    stroke(0)
    strokeWeight(1)
    q = PolyLine(X1,Y1,Z1)
    
    if HorAngle == 720.0:
        
        noLoop()
    



    
    
    
    
    
    
    
    
    
    
    
