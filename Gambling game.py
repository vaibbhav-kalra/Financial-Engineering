import random
A = [2,6,7]
B = [1,5,9]
C = [3,4,8]
#hm={'A':[2,6,7], 'B' : [1,5,9], 'C' : [3,4,8]}
First = A
Second= B
N = 1000
a=[];b=[]
for i in range(N):
    a.append(random.choice(First))
    b.append(random.choice(Second))
    
count=0    
for i in range(N):
    if a[i] > b[i]:
        count += 1

print("Probability of A beating B in one roll", count/N)

#%%
import random
import pandas as pd
A = [2,6,7]
B = [1,5,9]
C = [3,4,8]
a = pd.DataFrame(); b = pd.DataFrame(); a_sum=pd.DataFrame();b_sum=pd.DataFrame()
N = 1000
Die_Rolls = -1 # -1 for 1 roll, -2 for 2 rolls and so on...
rolls = Die_Rolls 
while rolls != 0:
    rolls += 1
    for i in range(N):
        a.at[rolls,i] = random.choice(A)
        b.at[rolls,i] = random.choice(B)

a_sum = pd.DataFrame(a.sum(axis = 0, skipna = True))
b_sum = pd.DataFrame(b.sum(axis = 0, skipna = True))
    
count=0    
for i in range(N):
    if a_sum.at[i,0] > b_sum.at[i,0]:
        count += 1

print("Probability of A beating B in " + str(-Die_Rolls) + " rolls is " + str(count/N))
print("Probability of B beating A in " + str(-Die_Rolls) + " rolls is " + str(1-(count/N)))

