# Selection Sort
A = [4, 3, 1, 5, 2]
n = len(A)
for i in range(1,n):
    temp = A[i]
    for j in range(0,i):
        if temp < A[j]:
            s = A[i]
            A[i] = A[j]
            A[j] = s
            