def LinearColor (x1,y1,z1,x2,y2,z2,scalar):
    
    #finds the point on a line bases on a scalar
    r = float(scalar*(x1 + x2))
    g = float(scalar*(y1 + y2))
    b = float(scalar*(z1 + z2))
    

    
    return(r,g,b)
