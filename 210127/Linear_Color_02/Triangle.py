#draw the triangle inside the unit circle


def Triangle(CenterX,CenterY,CenterZ,RadiusX,RadiusY,RadiusZ):
    
    line(CenterX,CenterY,CenterZ,RadiusX,RadiusY,RadiusZ)
    line(CenterX,CenterY,CenterZ,RadiusX,RadiusY,CenterZ)
    line(RadiusX,RadiusY,RadiusZ,RadiusX,RadiusY,CenterZ)
