def retrieved_matrix(var_type, input_file):
    source_file = open(input_file, 'r')
    source = source_file.read()
    source_file.close()
    matrix_string = []
    for line in source.split('\n'):
        items = line.split(' ')
        matrix_string.append(items)
    output_matrix = []
    for lineitem in matrix_string:
        line = []
        for item in lineitem:
            if item !='' and var_type == "double":
                line.append(float(item))
            elif item !='' and var_type == "int":
                line.append(int(item))
        output_matrix.append(line)
    return output_matrix


def get_coef(input_file):
    source_file = open(input_file, 'r')
    source = source_file.read()
    source_file.close()
    coef_string = source.split('\n')
    coef = []
    for item in coef_string:
        coef.append(float(item))
    return coef


def dgemm_calculate(A, B, C, alpha, beta):
    newC = []
    for i in range(0, len(A)):
        C_line = []
        for j in range(0, len(C[0])):
            c = 0
            for r in range(0, len(A[0])):
                c = c + alpha * A[i][r] * B[r][j]
            c = c + beta * C[i][j]
            C_line.append(c)
        newC.append(C_line)
    return newC


def write_matrix_to_file(matrix, output_file):
    output = open(output_file, 'w')
    for i in range (0, len(matrix)):
        for j in range(0, len(matrix[0])):
            output.write(str(matrix[i][j]))
            output.write(" ")
        output.write('\n')


fileA = r"C:\Users\Victoria\Documents\ITMO_Course\Python\ITMO2022_Python\Files_Practice2\MatrixA.txt"
fileB = r"C:\Users\Victoria\Documents\ITMO_Course\Python\ITMO2022_Python\Files_Practice2\MatrixB.txt"
fileC = r"C:\Users\Victoria\Documents\ITMO_Course\Python\ITMO2022_Python\Files_Practice2\MatrixC.txt"
fileCoef = r"C:\Users\Victoria\Documents\ITMO_Course\Python\ITMO2022_Python\Files_Practice2\Coef.txt"
fileNewC = r"C:\Users\Victoria\Documents\ITMO_Course\Python\ITMO2022_Python\Files_Practice2\MatrixC_new_1.txt"
coefficients = get_coef(fileCoef)
M = int(coefficients[0])
N = int(coefficients[1])
K = int(coefficients[2])
alpha = coefficients[3]
beta = coefficients[4]
matrixA = retrieved_matrix("double", fileA)
matrixB = retrieved_matrix("double", fileB)
matrixC = retrieved_matrix("double", fileC)
matrixNewC = dgemm_calculate(matrixA, matrixB, matrixC, alpha, beta)
write_matrix_to_file(matrixNewC, fileNewC)