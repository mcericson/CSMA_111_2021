
#This function draws the point on circle based on sin and cos.
#Mark Ericson 1.13.21


def TrigCirc(HorAngle,Radius,CenterX,CenterY):
    
    x = cos(HorAngle)*Radius + CenterX
    y = sin(HorAngle)*Radius + CenterY
    z = 0
    
    if HorAngle >= abs(360):
        
        TrigCirc(HorAngle,Radius, CenterX, CenterY)
    
    
    return(x,y,z)
    
