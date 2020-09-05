# If the person chooses the number out of two envelopes which is greater than the number
# contained in second evnvelope, then the person wins.
# x is a list of numbers ranging from 0.5 to n - 0.5. We have to guess a value of x.
# The value that we choose is our guess which we hope would divide the interval  
# between y and z. The greater the distance between y and z, more is the chance of winning.
# If number chosen is y,then swapping is done, otherwise number chosen is z, which is a
# win. However, for cases represented by w and q, number chosen is more than random guess
# so no swap takes place, which gives us the probability of 0.5

import random
import numpy as np
trial = 10000
n = 100 # total numbers
i = 0
w = 0 # x<y<z # Probability of winning is 0.5 based on decision tree
e = 0 # y<x<z # Probability of winning is 1. 
q = 0 # y<z<x # Probability of winning is 0.5

# y is always less than z
z = random.choice(range(2,100))
y = random.choice(range(1,z))
for i in range(trial):
      
    x = random.choice(np.arange(1/2,n-1/2,1).tolist())
    r = random.choice([z,y]) # Chosen number from envelope can be y or z
    
    # Swapping is done only if r < x
    if r < x:
        No = z + y - r
    else:
        No = r


    # winning times
    if x < y and No > y:
        w += 1
    elif y < x < z and No > y:
        e += 1
    elif x > z and No > y:
        q += 1
     
Prob = (w + e + q)/trial
print("Probability of win",round(Prob,3))
print("Theoretical probability of win", round(0.5+(z-y)/(2*n),3))

