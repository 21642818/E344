import numpy as np
#import matplotlib.pyplot as plt
from statistics import mean

def calibrate(time, amplitude):

    ######################################
    # Enter calibration code here:
    ######################################

    count = 0
    bHigh = False
    beat = []

    # Beat count
    for x in range(len(amplitude)) :
        if ((amplitude[x] > 4) and (bHigh == False)) :
            count += 1
            beat.append(time[x])
            bHigh = True
        if ((amplitude[x] < 1) and (bHigh == True)) :
            bHigh = False

    firstCount = beat[0]
    lastCount = beat[count-1]

    tempBPM = 60*(count-1)/(lastCount - firstCount)

    #BPM error calibration (parabolic error function)
    bpm = round(1.016707587*tempBPM)-1.861021767  
        
    ######################################
        
    return bpm
        
