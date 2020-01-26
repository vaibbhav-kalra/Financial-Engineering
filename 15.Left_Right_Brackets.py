# Checking Left and Right brackets
#from time import process_time
#times = list()
stack= [] #Empty stack
A = input("Enter a string : ") #Asking user to enter a word
n = len(A) #Specifying length of word and size of stack
count = 0
def push(integer): #Defining push function
    if len(stack) == n:
        print("stack is full")
    else:
        stack.append(integer)
        
for i in range(n):
 #   start = process_time()
    if A[i] == '(':
        push(i)
    elif A[i] == ')':
        del stack[-1]
    #end = process_time()
#times.append(end-start)
        
if len(stack) == 0:
    print("# Left Brackets = # Right Brackets")
else:
    print("# Left Brackets != # Right Brackets")