#write a program to calculate resistance
#of a circuit containing resistors in both
#parallel and series

import numpy as np
#Resistances in each separate cable
R = np.array([[100,20,35],[50],[150,75]],dtype = object)
Rtots = np.array([]) # array for total resistances accros the 3 cables
temp = 0 # temporary value to keep track of sum of resistances across the cables
for i in range(len(R)): #loop for iterating across each array in R
    for n in R[i]: #loop for summing each array in R
        temp = temp + n
    Rtots = np.append(Rtots,temp)#appends the sum of resistances to Rtots
    temp = 0#resets the value of temp to 0 - avoids false values
Rtotp = 0  #constant for storing the sum of resistances in parallel
for n in Rtots: #loop for summing the resistances in parallel
    Rtotp = Rtotp + 1/n
    
Rtotp = 1/Rtotp # flips from 1/R to R

print("%5.3f" % Rtotp + " Ohms") #outputs the total resistance of the circuit

