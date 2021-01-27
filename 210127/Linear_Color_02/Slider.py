
value = 0

def Slider():
    
    global value

    
    if keyPressed:
            
        if key == 'w':
            
            value += .011
            
        if key == 's':
            
            value -= .011
            
        return(value)
                
    if not keyPressed:
        
        value = value
        
        return (value)
