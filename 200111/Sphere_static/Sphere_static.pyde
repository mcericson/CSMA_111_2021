
#Mark Ericson January 11, 2021
#Points on a circle


add_library('peasycam')
import os
from PolyLine import PolyLine

file_name = os.path.basename(__file__)

#set up variables for drawing size
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2
Radius = Width/4

Static = True
Cam = False

#create empty global variables to store values in

Frame = 0

if Static == True:
    HorAngle = radians(145)
    VerAngle = radians(30)
    
else:
    
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
    frameRate(120)

    if Cam == True:
    
        cam = PeasyCam(this, 500)
        cam.setMinimumDistance(500)
        cam.setMinimumDistance(2000)
    
#processings draw loop. A continuous refresh in frames per secon
def draw():
    global Radius, CenterX, CenterY, X1, Y1, Z1, HorAngle, VerAngle, Frame
    
    Frame += radians(1)
    
    translate(CenterX,CenterY)
    rotateX(radians(45))
    rotateZ(radians(30))
    




    #keeps the background refreshing.  
    background(255)   
    noFill()
    
    #add value to the global variables
    
    if Static == True:
        pass
        
    else:
        
        HorAngle += radians(10)
        VerAngle += radians(.1)

    #create a spherical coordinate
    x = cos(HorAngle) * sin(VerAngle) * Radius
    y = sin(HorAngle) * sin(VerAngle) * Radius
    z = cos(VerAngle) *Radius
    
    stroke(0)
    strokeWeight(.5)
    
    #triangel on the Z axis
    strokeWeight(1.5)
    line(0,0,0,x,y,z)
    line(0,0,0,x,y,0)
    line(x,y,0,x,y,z)
    
    #circle on xy plane
    strokeWeight(.75)
    r2= dist(0,0,x,y)
    circle(0,0,r2*2)
    
    #circle on point
    pushMatrix()
    stroke(255,0,0)
    strokeWeight(1)
    translate(0,0,z)
    circle(0,0,r2*2)
    popMatrix()
    
    #triangle on xy plane
    stroke(0)
    strokeWeight(1)
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
    Label = "P = str((int(x),int(y),int(z)))"
    
    fill(0)
    textSize(Radius/10)

    text("P",x-2,y,z+10)
    strokeWeight(1)
    textSize(Radius/10)
    text("x",0,Radius)
    text("y",Radius,0)
    text("Z",0,0,Radius)

    
    noFill()
    #xyz axis
    stroke(0)
    strokeWeight(.75)
    xAxis = line(0,0,0,Radius)
    yAxis = line(0,0,Radius,0)
    zAxis = line(0,0,0,0,0,Radius)
    
    q = dist(0,0,0,x,y,z)
    circle(0,0,Radius*2)

    rotateZ(HorAngle)
    rotateX(radians(90))
    stroke(255,0,0)
    strokeWeight(1)
    circle(0,0,Radius*2)
    
    #Draw Great Circles
    if Static == True:
        
        save("images/" + str(file_name) + str(second())+ ".jpg")   
        stroke(100)
        strokeWeight(.4)
        for i in range(0,360,20):
            rotateY(radians(i))
            circle(0,0,Radius*2)
        noLoop()
    else:
        pass


    

    
 
    

   
   #end drawing when condition reached
    if VerAngle >= radians(200):
        save("images/" + str(file_name) + str(second())+ ".jpg")       
        
        noLoop()
        
    
