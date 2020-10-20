import numpy as np
#import matplotlib.pyplot as plt
from statistics import mean

def calibrate(time, amplitude):

    ######################################
    # Enter calibration code here:
    ######################################
    
    #mean voltage out
    Vout_mean = mean(amplitude[len(amplitude)-20:len(amplitude)])

    #linear temperature calibration
    temperature = round(2.187472844*Vout_mean+33.56888666)      
        
    ######################################
        
    return temperature
        
