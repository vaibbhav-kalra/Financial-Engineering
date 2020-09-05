P1 = [[13,1,7],[4,3,6],[-1,2,8]] # max value of each column
P2 = [[3,4,3],[1,3,2],[9,8,-1]] # max value of each row
#%%
P1 = [[1,0],[0,2]] # max value of each column
P2 = [[2,0],[0,1]] # max value of each row
#%%
import pandas as pd

P1 = pd.DataFrame(P1)
P2 = pd.DataFrame(P2)

# Best response approach for player 1
P3 = pd.DataFrame()
for j in range(len(P1[0])):
    for i in range(len(P1)):
        if max(P1.loc[:,j]) == P1.loc[i,j]:
            P3.loc[i,j] = 'True'
        else:
            P3.loc[i,j] = 'False'

# Best response approach for player 2
P4 = pd.DataFrame()
for j in range(len(P2[0])):
    for i in range(len(P2)):
        if max(P2.loc[i,:]) == P2.loc[i,j]:
            P4.loc[i,j] = 'True'
        else:
            P4.loc[i,j] = 'False'

# Finding pure strategy Nash Equilibrium
for j in range(len(P1[0])):
    for i in range(len(P1)):
        if P3.loc[i,j] == P4.loc[i,j] == 'True':
            print("Nash Equilibrium is")
            print(P1.loc[i,j])
            print(P2.loc[i,j])

