#Palindrome
Word = input()#Asking useer to enter a word
n = len(Word)#Specifying length of word
count = 0
count1 = 0
for i in range(n):
    if Word[i] == Word[n-i-1]: #Comparing each letter with all the other letters in reverse order
        count = count + 1
        count1 = count1 + 1
    
if count == n: #If no. of letters counted matched with other letters, printing Palindrome
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")

print("No. of operations: ",count1)
import matplotlib.pyplot as plt
B = [4, 8, 11, 14]#Input Size
C = [4, 8, 11, 14]#No. of Operations
plt.scatter(B,C)
plt.xlabel("Input Size")
plt.ylabel("No. of Operations")