#Problem:  Create a Grid of Points and Draw Orthogonal lines throug the grid. 


import rhinoscriptsyntax as rs
import random

def ChunkList(List,size):
    for i in range(0,len(List),size):
        yield List[i:i +size]
def FlipMatrix(Matrix):
    NList = list(zip(*Matrix[::-1]))
    NList2= []
    for i in NList:
        NList2.append(list(i))
    return(NList2)



GridX = 5
GridY = 20

if GridX == GridY:
    GridShort = GridX

if GridX != GridY:
    GridShort = GridY


Points = []
for value in range(GridX):
    X = value
    for value in range(GridY):
        Y = value
        Z = random.randint(0,2)
        Points.append(rs.AddPoint(X,Y,Z))

NPoints = list(ChunkList(Points,GridShort))
ULines = []
for i in NPoints:
    U  = rs.AddPolyline(i)
    ULines.append(U)

List2 = FlipMatrix(NPoints)

VLines = []
for i in List2:
    V = rs.AddPolyline(i)
    VLines.append(V)

Q = rs.AddNetworkSrf((ULines+VLines),continuity=10)

