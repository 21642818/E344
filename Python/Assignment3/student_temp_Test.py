import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

def calibrate(time, amplitude):

    #plt.scatter(time, amplitude)
    #plt.show()
    #print(len(amplitude))

    ######################################
    # Enter calibration code here:
    ######################################

    #highVolt = 3.8485329151153564
    #midVolt  = 2.0256764888763428
    #lowVolt  = 0.19708225146335182
    
    print(mean(amplitude[len(amplitude)-20:len(amplitude)]))
    Vout_mean = mean(amplitude[len(amplitude)-20:len(amplitude)])

    #temperature = round(((42 - 34)/(highVolt - lowVolt))*(Vout_mean - midVolt) + 38)
    temperature = round(2.187472844*Vout_mean+33.56888666)      

    #Vgnd = 2.2
    #Voffset = 1.541913
    #Vso38 = 1.38
    #alpha = 0.02
    #G = 22.69563

    #temperature = (Vout_mean-Vgnd)/(alpha*G) + (Voffset-Vso38)/alpha + 38
        
    ######################################
        
    return temperature
        
