
#This function draws the point on circle based on sin and cos.
#Mark Ericson 1.13.21

from PolyLine import PolyLine
def TrigCirc(HorAngle,VerAngle,Rotation,Radius,CenterX,CenterY,CenterZ,Orient):
    X1 = []
    Y1 = []
    Z1 = []
    for i in range(int(Rotation)):
        Hor = radians(HorAngle*i)
        Ver = radians(VerAngle*i)
        
        if Orient == "ThreeD":
        
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) + CenterY
            z = cos(Ver)*Radius+  CenterZ 
        
        if Orient == "Top":
        
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) + CenterY
            z = 0 +  CenterZ 
        
        if Orient == "Front":
            
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = cos(Ver)*Radius+  CenterZ 
            z = 0 + CenterY
            
        if Orient == "Oblique":
            
            x = cos(Hor)*Radius*sin(Ver)+ CenterX
            y = sin(Hor)*Radius*sin(Ver) - cos(Ver)*Radius*.375 + CenterY
            z = 0 +  CenterZ
        
        
        
               
        
        
        
        X1.append(x)
        Y1.append(y)
        Z1.append(z)
    
    PolyLine(X1,Y1,Z1)
    return(x,y,z,Hor,Ver)
    
