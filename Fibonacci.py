#Fibonacci Sequence
n = 5#Fibonacci sequence till which number required
ppval = 0#Storing prev. prev value
pval = 1#Storing prev value
print(ppval)
print(pval)
count = 0
for i in range(1,n):#Calculating series
    Fib = pval + ppval
    ppval = pval#Reassigning prev value to prev prev value
    pval = Fib#Reassigning Fibboncci value in above step to prev value
    count = count + 1
    print (Fib)
print("No. of operations: ",count)
import matplotlib.pyplot as plt
B = [5, 10, 25, 50, 75, 100]#Input Size
C = [6, 9, 24, 49, 74, 99]#No. of Operations
plt.scatter(B,C)
plt.xlabel("Input Size")
plt.ylabel("No. of Operations")
