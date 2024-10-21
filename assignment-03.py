'''   Write a Python program to compute following computation on matrix:
          a) Addition of two matrices
          b) Subtraction of two matrices
          c) Multiplication of two matrices
          d) Transpose of a matrix '''

print(__doc__)

row1 = int(input("Enter the rows for matrix 1:"))
col1 = int(input("Enter the columns for matrix 1:"))
row2 = int(input("Enter the rows for matrix 2:"))
col2 = int(input("Enter the columns for matrix 2:"))

def display(row,col):
    matrix = []
    for i in range(row):
        row_values = []
        for j in range(col):
            element = int(input(f"Enter the element at [{i+1}][{j+1}] : "))
            row_values.append(element)
        matrix.append(row_values)
    return matrix

def addition(mat_a , mat_b):
    mat_sum = []
    if(row1 == row2 and col1 == col2):
        for i in range(row1):
            sum_rows = []
            for j in range(row2):
                m = mat_a[i][j] + mat_b[i][j]
                sum_rows.append(m)
            mat_sum.append(sum_rows)
        return mat_sum
    else:
        print("Addition is not possible since the matices aren't of the same order")

def multiplication(m1,m2):
    mul = []
    if(col1 == row2):
        for i in range(row1):
            row_val = []
            for j in range(col2):
                ele_sum = 0
                for k in range (row2):
                    product = m1[i][k] + m2[k][j]
                    ele_sum += product
                row_val.append(ele_sum)
            mul.append(row_val)
        return mul
    else:
        print("Multiplication is not possible since the matices aren't of the same order")
     

def transpose(matrix,row,col):
    for i in range(row):        
        for j in range(col): 
            matrix[i][j] = matrix[j][i]
    for r in matrix:
        print(r)

m1 = display(row1,col1)
print(m1,"\n")

m2 = display(row2,col2)
print(m2,"\n")

print("The addition matrix is:")
print(addition(m1,m2),"\n")

print("The multiplication matrix is:")
print(multiplication(m1,m2),"\n")

print("The transpose matrix is:")
print(transpose(m1,row1,col1))