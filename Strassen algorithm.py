a = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
b = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

def blank(p, q): # create a matrix filled with 0's
    matrix = [[0 for row in range(p)] for col in range(q)]
    return matrix

def multiply(a, b): # multiply the two matrices
    p_matrix = blank(len(a), len(b[0]))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                p_matrix[i][j] += a[i][k]*b[k][j]
    return p_matrix

# Splitting of matrices into 4 parts
def split_matrix(a): 
    matrix_length = len(a)
    mid = matrix_length // 2
    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]
    top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    bot_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]

    return top_left, top_right, bot_left, bot_right

# Defining function for adding matrices
def add(a, b):
    d = []
    for i in range(len(a)):
        c = []
        for j in range(len(a[0])):
            c.append(a[i][j] + b[i][j])
        d.append(c)
    return d

# Defining function for subtracting matrices
def sub(a, b):
    d = []
    for i in range(len(a)):
        c = []
        for j in range(len(a[0])):
            c.append(a[i][j] - b[i][j])
        d.append(c)
    return d

# Applying Strassen's algorithm
def strassen(a, b, q):
    # base case: 1x1 matrix
    if q == 1:
        d = [[0]]
        d[0][0] = a[0][0] * b[0][0]
        return d
    else:
        #split matrices into quarters
        a11, a12, a21, a22 = split_matrix(a)
        b11, b12, b21, b22 = split_matrix(b)
        
        # p1 = (a11+a22) * (b11+b22)
        p1 = strassen(add(a11,a22), add(b11,b22), q/2)
        # p2 = (a21+a22) * b11
        p2 = strassen(add(a21,a22), b11, q/2)
        # p3 = a11 * (b12-b22)
        p3 = strassen(a11, sub(b12,b22), q/2)
        # p4 = a22 * (b12-b11)
        p4 = strassen(a22, sub(b21,b11), q/2)
        # p5 = (a11+a12) * b22
        p5 = strassen(add(a11,a12), b22, q/2)
        # p6 = (a21-a11) * (b11+b12)
        p6 = strassen(sub(a21,a11), add(b11,b12), q/2)
        # p7 = (a12-a22) * (b21+b22)
        p7 = strassen(sub(a12,a22), add(b21,b22), q/2)

        # c11 = p1 + p4 - p5 + p7
        c11 = add(sub(add(p1, p4), p5), p7)
        # c12 = p3 + p5
        c12 = add(p3, p5)
        # c21 = p2 + p4
        c21 = add(p2, p4)
        # c22 = p1 + p3 - p2 + p6
        c22 = add(sub(add(p1, p3), p2), p6)

        c = blank(len(c11)*2,len(c11)*2)
        for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j]                   = c11[i][j]
                c[i][j+len(c11)]          = c12[i][j]
                c[i+len(c11)][j]          = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]
        return c

print ("Matrix Multiplication:")
print (strassen(a, b, 4))