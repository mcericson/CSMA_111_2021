#This function locates a point on a line with its two endpoints and a scalar
#mark ericson 1.27.21

def LinearInterp(x1,y1,z1,x2,y2,z2,scalar):
    
    #finds point on a line
    x3 = float((x1 + x2)*scalar)
    y3 = float((y1 + y2)*scalar)
    z3 = float((z1 + z2)*scalar)
    
    
    
    return(color(x3,y3,z3))
