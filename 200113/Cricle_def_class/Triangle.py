#draw the triangle inside the unit circle


def Triangle(CenterX,CenterY,RadiusX,RadiusY):
    
    line(CenterX,CenterY,RadiusX,RadiusY)
    line(CenterX,CenterY,RadiusX,CenterY)
    line(RadiusX,RadiusY,RadiusX,CenterY)
