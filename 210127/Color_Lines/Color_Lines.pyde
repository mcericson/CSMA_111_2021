#imports

from LinearInterp import LinearInterp

#Variables
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2


#Global Variables



file_name = os.path.basename(__file__)


def setup():
    
    size(Width,Height,P2D)
    

def draw():
    background(255)
    C = []
    scalar = []
    for i in range(0,Height,1):
        scalar.append(float(i)/Height)
        Color = LinearInterp(12,59,101,255,255,255,scalar[i])
        C.append(Color)

    for i in range(0,Height,1):
        stroke(C[i])
        strokeWeight(1)
        line(0,i,Width,i)
    
    print 
