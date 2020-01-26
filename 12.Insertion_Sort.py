# Insertion Sort
A = [4, 3, 1, 5, 2]
n = len(A)
for i in range(1,n): # Selecting elements to compare one by one starting from 2nd element
    temp = A[i]
    j = i - 1
    while j >= 0 and temp < A[j]: # Shifting the values higher than temp to the left
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = temp # Putting the lower temp value in the space created by shifting