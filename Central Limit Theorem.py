import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt
A = np.random.randint(1, 100, (1000, 999))
B = pd.DataFrame(A)
C=[0]*len(A)
for i in range(len(A[0])+1):
    a = round(np.mean(B.iloc[i])) # column wise
    b = round(np.std(B.iloc[i]))
    #print("Mean is: ",a,"Std Dev is: ",b)
    C[i] = round(np.mean(B.iloc[i]))

#for i in range

counter=collections.Counter(B[2])
plt.bar(counter.keys(),counter.values())
plt.show()
counter1 = collections.Counter(C)
plt.bar(counter1.keys(),counter1.values())
plt.show()