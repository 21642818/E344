import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

def calibrate(time, amplitude):
        
    plt.scatter(time, amplitude)
    plt.show()
    print(len(amplitude))

    ######################################
    # Enter calibration code here:
    ######################################

    count = 0
    bHigh = False
    beat = []

    for x in range(len(amplitude)) :
        if ((amplitude[x] > 4.9) and (bHigh == False)) :
            count += 1
            beat.append(time[x])
            bHigh = True
        if ((amplitude[x] < 0.5) and (bHigh == True)) :
            bHigh = False

    firstCount = beat[0]
    lastCount = beat[count-1]
    
    print(firstCount)
    print(lastCount)
    print(count)

    tempBPM = 60*(count-1)/(lastCount - firstCount)
    print(tempBPM)

    #bpm = 1.048621882*tempBPM-5.679729809       
    #bpm = 99.573394*np.log(tempBPM)-354.5555183 
    #bpm = (-0.001029331*pow(tempBPM,2))+(1.258161062*tempBPM)-15.40784797 
    bpm = round(1.016707587*tempBPM)-1.861021767   
        
    ######################################
        
    return bpm
        
