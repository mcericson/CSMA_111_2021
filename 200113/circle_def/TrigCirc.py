#this function defines a point on a circle

def TrigCirc(HorAngle,RadiusX,RadiusY,CX,CY):
    
    x = cos(radians(HorAngle))* RadiusX + CX
    y = sin(radians(HorAngle))* RadiusY + CY
    z = 0
    

    return(x,y,z)
