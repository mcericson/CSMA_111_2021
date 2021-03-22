
import CaptureView
from CaptureView import GetCaptureView
from imp import reload
reload(CaptureView)

import rhinoscriptsyntax as rs
from math import radians

import time

time.localtime()
count = 0
while count < 360:
    count+=1
    rs.Sleep(1)
    
    if count < 50:
        rs.RotateView(direction = 1, angle = radians(-20))
    
    else:
        rs.RotateView(direction = 1, angle = radians(-20))
        rs.RotateView(direction = 2, angle = radians(-20))
    
    GetCaptureView(1,str("%04d"%count),"Animate13")


