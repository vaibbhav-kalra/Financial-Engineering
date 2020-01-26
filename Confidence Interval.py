import numpy as np
import random

def seq(start, end, n):
    Seq = []
    for i in range(n):
        Seq.append(random.randint(start,end))
    return Seq

S = seq(1,100,100)
S1 = np.array(S)
C1 = np.array(np.random.choice(S,size=20,replace=False))
C2 = np.array(np.random.choice(S,size=40,replace=False))
C3 = np.array(np.random.choice(S,size=60,replace=False))
C4 = np.array(np.random.choice(S,size=80,replace=False))
C5 = np.array(np.random.choice(S,size=90,replace=False))
C6 = np.array(np.random.choice(S,size=100,replace=False))

e = .5 # epsilon
u = np.mean(S1) # Mu
x1 = np.mean(C1);x2 = np.mean(C2);x3 = np.mean(C3);x4 = np.mean(C4);x5 = np.mean(C5);x6 = np.mean(C6)

#lower=u-e; upper=u+e
#C=[x1,x2,x3,x4,x5,x6]

L=[0]*6;
lower=[x1-e,x2-e,x3-e,x4-e,x5-e,x6-e];upper=[x1+e,x2+e,x3+e,x4+e,x5+e,x6+e]
for i in range(6):
    if u<=upper[i] and u>=lower[i]: # checking if both conditions are true and false
                                    # not subtracting
        L[i] = 'Yes'
    else:
        L[i] = 'No'