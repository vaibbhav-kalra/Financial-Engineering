# Global Alignment
import numpy as np
Set = [1,2,3,4]
#defining DNA characters as 1,2,3,4
dict = {1:'A', 2:'T', 3:'G', 4:'C'}
#creating random DNA sequence
import random
def seq(start, end, n):
    Seq = []
    for i in range(n):
        Seq.append(random.randint(start,end))
    return Seq
Seq1 = seq(1,4,5)
Seq3 = Seq1 [:]
Seq2 = Seq3.remove(random.choice(Seq1))
#Seq1=[1,2,3,3,4,1,2,4]
#Seq3=[2,3,1,1,4,3,2,2]
#Assigning values to Mismatch, Gap and Match
Mismatch = -1
Match = 2 
Gap = -1
# Global Alignment Matrix
m = len(Seq1)
n = len(Seq3)
C = np.array([[0 for j in range(n+1)] for i in range (m+1)]) # Creating a zero matrix
for i in range(0,m+1):
    C[i][0] = i * Gap
for i in range(0,n+1):
    C[0][i] = i * Gap    
for i in range(0,m):
    for j in range(0,n):
        if Seq1[i] == Seq3[j]:
            C[i+1][j+1] = C[i][j] + Match
        else:
            C[i+1][j+1] = max(C[i][j] + Mismatch, C[i+1][j] + Gap, C[i][j+1] + Gap)

# Defining the path and matching of both the sequences            
s1 = ""
s2 = ""
i = len(Seq1)
j = len(Seq3)
D = np.array([[0 for j in range(n+1)] for i in range (m+1)])
while (not(i == -1 or j == -1)):
    if (C[i][j] == C[i-1][j-1] + Match): 
        s1 = dict[Seq1[i-1]] + s1
        s2 = dict[Seq3[j-1]] + s2
        D[i][j] += 1
        i=i-1
        j=j-1
    elif (C[i][j] == C[i-1][j-1] + Mismatch):
        s1 = dict[Seq1[i-1]] + s1
        s2 = dict[Seq3[j-1]] + s2
        D[i][j] += 1
        i=i-1
        j=j-1
    elif (C[i][j] == C[i][j-1] + Gap):
        s1 = dict[Seq1[i-1]] + s1
        s2 = '-' + s2
        D[i][j] += 1
        i=i-1   
    elif (C[i][j] == C[i-1][j] + Gap):
        s1 = '-' + s1
        s2 = dict[Seq3[j-1]] + s2
        D[i][j] += 1
        j=j-1

