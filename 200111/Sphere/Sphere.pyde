
#Mark Ericson January 11, 2021
#Points on a circle

from PolyLine import PolyLine

#set up variables for drawing size
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2
Radius = Width/4

#create empty global variables to store values in

Frame = 0
HorAngle = 0
VerAngle = 0

#creat empty list to fill later

X1 = []
Y1 = []
Z1 = []

#processings set up function. needed to start a drawing
def setup():
    
    size(Width,Height,P3D)
    smooth(100)
    frameRate(60)
#processings draw loop. A continuous refresh in frames per secon
def draw():
    global Radius, CenterX, CenterY, X1, Y1, Z1, HorAngle, VerAngle, Frame
    
    Frame += radians(1)
    
    translate(CenterX,CenterY)
    rotateX(Frame)

    #keeps the background refreshing.  
    background(255)   
    noFill()
    
    #add value to the global variables
    HorAngle += radians(10)
    VerAngle += radians(.1)

    #create a spherical coordinate
    x = cos(HorAngle) * sin(VerAngle) * Radius
    y = sin(HorAngle) * sin(VerAngle) * Radius
    z = cos(VerAngle) *Radius
    
    stroke(0)
    strokeWeight(.5)
    
    #triangel on the Z axis
    line(0,0,0,x,y,z)
    line(0,0,0,x,y,0)
    line(x,y,0,x,y,z)
    
    #circle on xy plane
    r2= dist(0,0,x,y)
    circle(0,0,r2*2)
    
    #triangle on xy plane
    line(0,0,x,y)
    line(0,0,x,0)
    line(x,0,x,y)
    
    #append spherical coordinate to list
    X1.append(x)
    Y1.append(y)
    Z1.append(z)
    
    #draw Polyline
    stroke(12,59,101)
    strokeWeight(.5)
    PolyLine(X1,Y1,Z1)
    
    # label the spherical coordinate
    Label = str((int(x),int(y),int(z)))
    
    fill(0)
    textSize(10)
    text(Label,x,y,z)
  
   #end drawing when condition reached
    if VerAngle >= radians(180*2):
        
        noLoop()
