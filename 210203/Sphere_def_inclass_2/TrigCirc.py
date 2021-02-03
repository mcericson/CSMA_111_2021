
#This function draws the point on circle based on sin and cos.
#Mark Ericson 1.13.21

from Triangle import Triangle
from PolyLine import PolyLine

def TrigCirc(HorAngle,VerAngle,Radius,Rotation,CenterX,CenterY,CenterZ,Orient):
    
    #create empty list for polylin
    X1 = []
    Y1 = []
    Z1 = []
    
    #loop to create points on sphere
    for i in range(Rotation):
        
        Hor = radians(HorAngle*i)
        Ver = radians(VerAngle*i)
        
        if Orient == "ThreeD":
        
    
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) + CenterY
            z = cos(Ver)*Radius + CenterZ
            
        if Orient == "Top":
            
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) + CenterY
            z = 0 + CenterZ
            
        if Orient == "Front":
        
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = cos(Ver)*Radius + CenterZ
            z = 0 + CenterY
            
        if Orient == "Oblique":
        
    
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) - cos(Ver)*Radius*.9 + CenterZ + CenterY
            z = 0 + CenterZ           
            
            
        
        #append spherical coordinates to lists
        X1.append(x)
        Y1.append(y)
        Z1.append(z)
  
    
    #draw polyline 
    noStroke() 
    PolyLine(X1,Y1,Z1)
    
    stroke(50)
    strokeWeight(.3)

    Triangle(CenterX,CenterY,CenterZ,x,y,z)

    return(x,y,z,Hor,Ver)
    
