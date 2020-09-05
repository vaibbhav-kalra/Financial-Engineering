import random

P1 = 1/2 # win 1st game
P2 = 2/3 # win game immediately after a win
P3 = 1/3 # win game immediately after a loss

A = [0,1] # 0 for losing a game and 1 for winning a game

N = 10 # Trials
G = 3 # Games

sample_points = []; G1=[]; G2=[]; G3=[]

# Creating Tree of games (outer loop for trial and inner loop for games)
for i in range(N):
    Game1 = random.choice([0,1])
    Game2 = random.choice([0,1])
    Game3 = random.choice([0,1])
    
    G1.append(Game1)
    G2.append(Game2)
    G3.append(Game3)
            
    sample_points.extend([Game1, Game2, Game3])
    
sample = []; game=[];intersection=[]

# Finding sets of game and sample
i = 0
while i < len(sample_points):
    if sample_points[i] + sample_points[i+1] + sample_points[i+2] >= 2:
        n1 = sample_points[i] ; n2 = sample_points[i+1] ; n3 = sample_points[i+2]
        sample.append(n1);sample.append(n2);sample.append(n3)
    if sample_points[i] == 1:
        q1 = sample_points[i] ; q2 = sample_points[i+1] ; q3 = sample_points[i+2]
        game.append(q1);game.append(q2);game.append(q3)
    i = i+G

# Intersection between game and sample
for i in range(0, len(game)-G, G):
    for j in range(0, len(sample)-G, G):
        if game[i:i+G] == sample[j:j+G]:
            intersection.extend(sample[j:j+G])
        del sample[j:j+G]
            
#%%
# Probability calculation
Prob = 0
for j in range(0, len(game)-G, G):
    p = P1
    for i in range(G-1):
        if game[i] == 1 and game[i+1] == 1:
            p *= P2
        elif game[i] == 0 and game[i+1] == 1:
            p *= P3
        elif game[i] == 1 and game[i+1] == 0:
            p *= (1-P2)
        else:
            p *= (1-P3)
    Prob += p
#%%
Probi = 0
for j in range(0, len(intersection)-G, G):
    p = P1
    for i in range(G-1):
        if intersection[i] == 1 and intersection[i+1] == 1:
            p *= P2
        elif intersection[i] == 0 and intersection[i+1] == 1:
            p *= P3
        elif intersection[i] == 1 and intersection[i+1] == 0:
            p *= (1-P2)
        else:
            p *= (1-P3)
    Probi += p




#%% working
        
import random

P1 = 1/2 # win 1st game
P2 = 2/3 # win game immediately after a win
P3 = 1/3 # win game immediately after a loss

A = [0,1] # 0 for losing a game and 1 for winning a game

N = 10 # Trials
G = 3 # Games

sample_points = []; G1=[]; G2=[]; G3=[]

# Creating Tree of games (outer loop for trial and inner loop for games)
for i in range(N):
    for j in range(G):
        Game1 = random.choice([0,1])
        sample_points.append(Game1)
        
sample = []; game=[];intersection=[]

# Finding sets of game and sample
i = 0
while i < len(sample_points):
    if sum(sample_points[i:i+G]) >= 2:
        sample.extend(sample_points[i:i+G])
        
    if sample_points[i] == 1:
        game.extend(sample_points[i:i+G])
        
    i = i+G

for i in range(0, len(game)-G, G):
    for j in range(0, len(sample)-G, G):
        if game[i:i+G] == sample[j:j+G]:
            intersection.extend(sample[j:j+G])
            del sample[j:j+G]
#%% Final version
import pandas as pd
import numpy as np
import random
P1 = 1/2 # win 1st game
P2 = 2/3 # win game immediately after a win
P3 = 1/3 # win game immediately after a loss

trials = 1000
games = 3
data = pd.DataFrame() # simulating win/lose in 3 games over n trials        
for i in range(trials):
    for j in range(games):
        data.loc[i,j] = random.choice([0,1])

sample = pd.DataFrame() # segregating those that represent series win
for i in range(trials):
    for j in range(games):
        if ((data.loc[i,:]).sum()) >= 2:
            sample.loc[i,j] = data.loc[i,j]
            
game = pd.DataFrame() # segregating those that represent that first game is won
for i in range(trials):
    for j in range(games):
        if (data.loc[i,0]) == 1:
            game.loc[i,j] = data.loc[i,j]

intersection = pd.DataFrame()
intersection = sample[sample.astype(str).sum(1).isin(game.astype(str).sum(1))]
intersection.reset_index(inplace = True, drop = True) 

w = 0
game_prob = 0
for i in range(len(game)):
    w = P1
    for j in range(1,games):
        if game.iloc[i,j] == 1 and game.iloc[i,j-1] == 1:
            w = w*P2
        elif game.iloc[i,j] == 0 and game.iloc[i,j-1] == 1:
            w = w*(1-P2)
        elif game.iloc[i,j] == 1 and game.iloc[i,j-1] == 0:
            w = w*P3
        elif game.iloc[i,j] == 0 and game.iloc[i,j-1] == 0:
            w = w*(1-P3)
    game_prob += w
    w = 0
           
w = 0
inter_prob = 0
for i in range(len(intersection)):
    w = P1
    for j in range(1,games):
        if intersection.iloc[i,j] == 1 and intersection.iloc[i,j-1] == 1:
            w = w*P2
        elif intersection.iloc[i,j] == 0 and intersection.iloc[i,j-1] == 1:
            w = w*(1-P2)
        elif intersection.iloc[i,j] == 1 and intersection.iloc[i,j-1] == 0:
            w = w*P3
        elif intersection.iloc[i,j] == 0 and intersection.iloc[i,j-1] == 0:
            w = w*(1-P3)
    inter_prob += w
    w = 0
     
print("Probability of winning is ",inter_prob/game_prob)           

            
                     