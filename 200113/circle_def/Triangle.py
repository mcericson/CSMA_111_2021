#this function draws a the triangle used to plot the point on a sphere
#Provide the center fo the circle in CenterX, CenterY
#Provdie the point on the circle in RadiusX, Radius Y

def Triangle(CenterX,CenterY,RadiusX,RadiusY):
    
    line(CenterX,CenterY,RadiusX,RadiusY)
    line(CenterX,CenterY,RadiusX,CenterY)
    line(RadiusX,CenterY,RadiusX,RadiusY)
