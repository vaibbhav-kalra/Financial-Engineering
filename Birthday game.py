import random
import matplotlib.pyplot as plt
import numpy as np

M = 23
q = []
for b in range(1000):
    a=[] # getting birthdays for M number of people
    for x in range(M):
        a.append(random.randint(1,366))

    duplicates = [] # getting the number of people's with same birthdays
    for i in a:
        if a.count(i) > 1:
            duplicates.append(i)

    w = [] # getting the unique number of people with same birthdays
    for i in duplicates:
        if i not in w:
            w.append(i)
    q.append(len(w)) # counting the unique number of peoples in each trial
    
count = np.count_nonzero(q)    
    
P = round(count/1000,2) # Prob of people having same birthdays
Q = round(1-P,2) # Prob of people not having same birthdays

M = [10,20,23,50,70]
p = [0.12,0.41,0.51,0.98,1.0]
q = [0.88,0.59,0.59,0.02,0.0]

ax = plt.subplot(111)
plt.xlim(0,120)
plt.plot(M,p,label='Same birthday', marker='o')
plt.plot(M,q,label='No Same birthday', marker='x')
plt.xlabel('M = Number of people')
plt.ylabel('p = Probability of match')
plt.title('Birthday Game')
ax.legend()
plt.show()

