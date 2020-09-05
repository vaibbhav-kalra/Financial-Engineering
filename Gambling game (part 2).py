import random
import pandas as pd
trials = 10000
players = 4 # includes host

# Amount set apart by players
a=[]
for i in range(players-1):
    a.append(int(input("Enter amount: ")))

toss = pd.DataFrame()

# Getting tosses made by players
for i in range(trials):
    for j in range(players):
        toss.at[i,j] = random.choice(['H','T'])
        
# Calculating wins of players
prize_pool = sum(a)
win = pd.DataFrame()

for j in range(players-1):
    for i in range(trials):
        if toss.at[i,j] == toss.iloc[i,-1]:
            win.at[i,j] = 1
        else:
            win.at[i,j] = 0

win['sum'] = win.sum(axis=1)

# Calculating gain of players
prize = pd.DataFrame()

for j in range(players-1):
    for i in range(trials):
        if win.iloc[i,-1] == 0:
            prize.at[i,j] = -a[j]
        elif win.iloc[i,j] != 0:
            prize.at[i,j] = (prize_pool/win.iloc[i,-1])-a[j]
        else:
            prize.at[i,j] = -a[j]
            
print("Total gains of players: ", prize.sum(axis = 0, skipna = True))

outcome = pow(2,trials)
##Expected_Gain = Total_Gain/outcome



