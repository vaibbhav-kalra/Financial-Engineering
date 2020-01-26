import random
Coin = [0,1]
i = random.choice(Coin) # 0 for Heads
l=10
n = [0]*l
for j in range(l):
    count = 1
    while (i != 0):
        i = random.choice(Coin)
        count = count + 1
    i = random.choice(Coin)
    n[j] = count
    
#print(count)
P = 0.7 # Prob for heads
x = 2
d = 1
# P[X > x+d | X > x] = P[X > d]
D=0
for i in range(l):
    if n[i]>d:
        D = D+1
X=0
for i in range(l):
    if n[i]>x:
        X = X+1
U=0
for i in range(l):
    if n[i]>(x+d):
        U = U+1
print('x+d is ',U);print('x is ',X);print('d is ',D);
