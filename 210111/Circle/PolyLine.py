def PolyLine(PointsX,PointsY,PointsZ):
    
    EPX1=[]
    EPY1=[]
    EPZ1=[]
    
    EPX2=[]
    EPY2=[]
    EPZ2=[]
    
    for h in range(len(PointsX)):
        PointsX1 = PointsX[h-h]
        PointsY1 = PointsY[h-h]
        PointsZ1 = PointsZ[h-h]

    for i in range(len(PointsX)):
        PointsX2 = PointsX[i]
        PointsY2 = PointsY[i]
        PointsZ2 = PointsZ[i]
        line(PointsX2,PointsY2,PointsZ2,PointsX1,PointsY1,PointsZ1)
        # EPX1.append(PointsX1)
        # EPY1.append(PointsY1)
        # EPZ1.append(PointsZ1)
        # EPX2.append(PointsX[i])
        # EPY2.append(PointsY[i])
        # EPZ2.append(PointsZ[i])
        PointsX1 = PointsX2
        PointsY1 = PointsY2
        PointsZ1 = PointsZ2

    return(EPX1,EPY1,EPZ1,EPX2,EPY2,EPZ2)
