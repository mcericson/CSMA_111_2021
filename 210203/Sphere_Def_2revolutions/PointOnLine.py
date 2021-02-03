def PointOnLine (x1,y1,z1,x2,y2,z2,scalar):
    
    #finds the point on a line bases on a scalar
    x3 = float(scalar*(x1 + x2))
    y3 = float(scalar*(y1 + y2))
    z3 = float(scalar*(z1 + z2))
    

    
    return(x3,y3,z3)
