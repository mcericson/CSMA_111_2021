def setup():

    size(1000,1000)
    

def draw():
    background(255)
    cx = 1000/2
    cy = 1000/2
    translate(cx,cy)
    noFill()
    
    List1 = []
    for i in range(0,1000,10):
        
        List1.append(i)
    
    print List1
    
    for i in List1:
        circle(0,0,i)
        
    noLoop()


        
