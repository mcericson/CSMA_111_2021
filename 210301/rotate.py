import rhinoscriptsyntax as rs
import math

import CaptureView
from CaptureView import GetCaptureView
reload(CaptureView)


Count = 0 
for i in range(360):
    rs.Sleep(.01)
    Count+=1
    rs.RotateView(direction = 0,angle = math.radians(Count))
    
    #GetCaptureView(2,("Animate" + str(i)),"Animation")