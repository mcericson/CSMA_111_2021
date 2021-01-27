#draw the triangle inside the unit circle


def Triangle(CenterX,CenterY,CenterZ,RadiusX,RadiusY,RadiusZ):
    
    line(CenterX,CenterY,CenterZ,RadiusX,RadiusY,RadiusZ)
    line(CenterX,CenterY,CenterZ,RadiusX,CenterY,CenterZ)
    line(RadiusX,RadiusY,RadiusZ,RadiusX,CenterY,CenterZ)
