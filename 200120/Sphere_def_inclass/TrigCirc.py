
#This function draws the point on circle based on sin and cos.
#Mark Ericson 1.13.21

from PolyLine import PolyLine

def TrigCirc(HorAngle,VerAngle,Rotation,Radius,CenterX,CenterY,CenterZ):
    
    X1 = []
    Y1 = []
    Z1 = []
    
    for i in range(int(Rotation)):
        
        Hor = radians(HorAngle*i)
        Ver = radians(VerAngle*i)
            
    
        x = cos(Hor)*Radius*sin(Ver) + CenterX
        y = sin(Hor)*Radius*sin(Ver) + CenterY
        z = cos(Ver)*Radius + CenterZ
        
        X1.append(x)
        Y1.append(y)
        Z1.append(z)
    
    PolyLine(X1,Y1,Z1)
    
    
    return(x,y,z)
    
