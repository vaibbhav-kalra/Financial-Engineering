# Polynomial Multiplication
A = [5,0,10,6]
B = [1,2,4]
m = len(A)
n = len(B)
sum = [0]*(m+n-1)
for i in range(m):
    for j in range(n):
        sum[i+j] += A[i] * B[j]

def Polynomial(poly, n): 
    for i in range(n): 
        print(poly[i], end = ""); 
        if (i != 0): 
            print("x^", i, end = ""); 
        if (i != n - 1): 
            print(" + ", end = ""); 

Polynomial(A,m)
print("\n")
Polynomial(B,n)
print("\n")
Polynomial(sum,m+n-1)