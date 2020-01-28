# Referred to Into to Algorithms book by CLRS
import sys
import matplotlib.pyplot as plt
from time import perf_counter

p = [5,4,6,2,7] # Defining dimensions of each matrices

def parens(s, i, j): # Defining function for paranthesis using k matrix, 
                     #dimensions of matrices, no. of matrices
    res = ''
    if i == j:
        return "A"+str(j)
    else:
        res += "("
        res += parens(s, i, s[i][j]) 
        res += parens(s, s[i][j]+1, j)
        res +=  ")"
        return res
    
n = len(p)-1 # Total number of matrices
t1_start = perf_counter()
m = [[0 for column in range(n+1)] for row in range(n+1)] # Number of multiplications matrix
s= [[0 for column in range(n+1)] for row in range(n+1)] # k matrix

for i in range(1, n+1): # total number of dimensions of the matrices
    m[i][i] = 0 # Diagonal entries in m(i,j) are zero
for l in range(2, n+1): # For calculating multiplications for m[i,j] matrix (leaving first row for calculation)
    
    for i in range(1, n-l+2): #(leaving first column for calculation)
        j = i+l-1
        m[i][j] = sys.maxsize # Setting all values except diagonals as infinity
        for k in range(i, j):
            q = m[i][k]+ m[k+1][j]+ p[i-1]*p[k]*p[j] # No. of multiplications
            if q<m[i][j]:
                m[i][j] = q
                s[i][j] = k
        
t1_stop = perf_counter()   
#print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)
             
print("Matrix m[i,j]: ", m)
print("\n")
print("Matrix of k's: ", s)
print("\n")
print ('No.of multiplications： ', m[1][len(p)-1])
print ('Solution: ', parens(s, 1, len(p)-1))

# no. of multiplications as a function of n
n=[4,5,6,7,8,9]
mult=[158,280,434,484,554,670]
#[5,4,6,2,7][5,4,6,2,7,4][5,4,6,2,7,4,7][5,4,6,2,7,4,7,2][5,4,6,2,7,4,7,2,5]
plt.plot(n,mult)
plt.xlabel('n')
plt.ylabel('No of multiplications')
plt.show()
# time complexity
n=[4,5,6,7,8]
diff1 = [0.00018280000040249433,0.0006307000003289431,0.0005258000001049368,0.0007494000001315726,0.0011297999990347307]
plt.plot(n,diff1)
plt.xlabel('n')
plt.ylabel('Time complexity')
plt.show()

















#b = time.time()
#print ('Total run time is:{0:.2f}'.format( time.time()-b))
#now = datetime.now()
#end_time = now.strftime("%H:%M:%S")
#end_time1 = now.hour * 3600 + now.minute * 60 + now.second
#print("Current Time =", end_time)
