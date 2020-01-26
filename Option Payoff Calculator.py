import matplotlib.pyplot as plt
print("Enter LC1,LC2,LC3 for Long call, LC4,LC5,LC6 for Short call, LC7,LC8,LC9 for "
      "Long put,LC10,LC11,LC12 for Short put")
Option = []
Op = ''
S = [i for i in range(10,200)]
K1 = [0];K2 = [0];K3 = [0] # Call
CP1 = [0];CP2 = [0];CP3 = [0] # Call
payoff1=[0]*len(S);payoff2=[0]*len(S);payoff3=[0]*len(S) # Call
K4 = [0];K5 = [0];K6 = [0] # S Call
CP4 = [0];CP5 = [0];CP6 = [0] # S Call
payoff4=[0]*len(S);payoff5=[0]*len(S);payoff6=[0]*len(S) # S Call
K7 = [0];K8 = [0];K9 = [0] # Put
CP7 = [0];CP8 = [0];CP9 = [0] # Put
payoff7=[0]*len(S);payoff8=[0]*len(S);payoff9=[0]*len(S) # Put
K10 = [0];K11 = [0];K12 = [0] # S Put
CP10 = [0];CP11 = [0];CP12 = [0] # S Put
payoff10=[0]*len(S);payoff11=[0]*len(S);payoff12=[0]*len(S) # S Put
payoff13=[0]*len(S)

while(Op != 'False'):
    Op = input("Enter type of option: ") 
    if(Op != 'False'):
        Option.append(Op)

# Long Call
if('LC1' in Option):
    CP1 = int(input("LC1 Prem: "))
    K1 = int(input("LC1 Strike: "))
if('LC2' in Option):
    CP2 = int(input("LC2 Prem: "))
    K2 = int(input("LC2 Strike: "))
if('LC3' in Option):
    CP3 = int(input("LC3 Prem: "))
    K3 = int(input("LC3 Strike: "))
    
# Short Call
if('LC4' in Option):
    CP4 = int(input("LC4 Prem: "))
    K4 = int(input("LC4 Strike: "))
if('LC5' in Option):
    CP5 = int(input("LC5 Prem: "))
    K5 = int(input("LC5 Strike: "))
if('LC6' in Option):
    CP6 = int(input("LC6 Prem: "))
    K6 = int(input("LC6 Strike: "))

# Long Put
if('LC7' in Option):
    CP7 = int(input("LC7 Prem: "))
    K7 = int(input("LC7 Strike: "))
if('LC8' in Option):
    CP8 = int(input("LC8 Prem: "))
    K8 = int(input("LC8 Strike: "))
if('LC9' in Option):
    CP9 = int(input("LC9 Prem: "))
    K9 = int(input("LC9 Strike: "))
        
# Short Put
if('LC10' in Option):
    CP10 = int(input("LC10 Prem: "))
    K10 = int(input("LC10 Strike: "))
if('LC11' in Option):
    CP11 = int(input("LC11 Prem: "))
    K11 = int(input("LC11 Strike: "))
if('LC12' in Option):
    CP12 = int(input("LC12 Prem: "))
    K12 = int(input("LC12 Strike: "))      

# Long Call
j=0
if('LC1' in Option):
    while(j != len(S)):
        if K1<S[j]:
            payoff1[j] = max(S[j]-K1,0)-CP1
        else:
            payoff1[j] = -CP1
        j=j+1
j=0
if('LC2' in Option):
    while(j != len(S)):
        if K2<S[j]:
            payoff2[j] = max(S[j]-K2,0)-CP2
        else:
            payoff2[j] = -CP2
        j=j+1
j=0
if('LC3' in Option):
    while(j != len(S)):
        if K3<S[j]:
            payoff3[j] = max(S[j]-K3,0)-CP3
        else:
            payoff3[j] = -CP3
        j=j+1

  
# Short Call
j=0
if('LC4' in Option):
    while(j != len(S)):
        if K4<S[j]:
            payoff4[j] = -max(S[j]-K4,0)+CP4
        else:
            payoff4[j] = CP4
        j=j+1
j=0
if('LC5' in Option):
    while(j != len(S)):
        if K5<S[j]:
            payoff5[j] = -max(S[j]-K5,0)+CP5
        else:
            payoff5[j] = CP5
        j=j+1
j=0
if('LC6' in Option):
    while(j != len(S)):
        if K6<S[j]:
            payoff6[j] = -max(S[j]-K6,0)+CP6
        else:
            payoff6[j] = CP6
        j=j+1

# Long Put
j=0
if('LC7' in Option):
    while(j != len(S)):
        if K7>S[j]:
            payoff7[j] = max(K7-S[j],0)-CP7
        else:
            payoff7[j] = -CP7
        j=j+1
j=0
if('LC8' in Option):
    while(j != len(S)):
        if K8>S[j]:
            payoff8[j] = max(K8-S[j],0)-CP8
        else:
            payoff8[j] = -CP8
        j=j+1
j=0
if('LC9' in Option):
    while(j != len(S)):
        if K9>S[j]:
            payoff9[j] = max(K9-S[j],0)-CP9
        else:
            payoff9[j] = -CP9
        j=j+1
        
        
# Short Put
j=0
if('LC10' in Option):
    while(j != len(S)):
        if K10>S[j]:
            payoff10[j] = -max(K10-S[j],0)+CP10
        else:
            payoff10[j] = CP10
        j=j+1
j=0
if('LC11' in Option):
    while(j != len(S)):
        if K11>S[j]:
            payoff11[j] = -max(K11-S[j],0)+CP11
        else:
            payoff11[j] = CP11
        j=j+1
j=0
if('LC12' in Option):
    while(j != len(S)):
        if K12>S[j]:
            payoff12[j] = -max(K12-S[j],0)+CP12
        else:
            payoff12[j] = CP12
        j=j+1

for i in range(len(S)):
    payoff13[i] = payoff1[i]+payoff2[i]+payoff3[i]+payoff4[i]+payoff5[i]+payoff6[i]\
                  +payoff7[i]+payoff8[i]+payoff9[i]+payoff10[i]+payoff11[i]+payoff12[i]

plt.scatter(S,payoff13)
plt.show
