#Method 1
n = 5#Factorial of
fact = 1#Initialisation
count = 0
for i in range(1,n+1):#Multiplication
    fact = fact * i
    count = count + 1
print("Factorial of " + str(n) + " is :" +str(fact))
print("No. of operations: ", count)

#Method 2
fact1 = n
count = 0
for i in range(2,n):
    fact1 = fact1 * i
    count = count + 1
print ("Factorial of " + str(n) + " is :" +str(fact1))
print("No. of operations: ", count)

#Method 3 (Best)
i = 2
fact3 = 1
count = 0
while (i <= n):
    fact3 = fact3 * i
    i = i+1
    count = count + 1
print("Factorial of " + str(n) + " is :" +str(fact3))
print("No. of operations: ", count)

B = [2, 5, 7, 11, 15]
C = [1, 4, 6, 10, 14]
import matplotlib.pyplot as plt
plt.scatter(B,C)
plt.xlabel("Input Size")
plt.ylabel("No. of Operations")