import copy
import typing


# In case of not using copy package of a standard library
def copy_matrix(matrix: list) -> list:
    rows = len(matrix)
    cols = len(matrix[0])

    matrix_copy = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            matrix_copy[i][j] = matrix[i][j]

    return matrix_copy


# Creates a matrix filled with zeros. Params are rows and columns length.
def zeros_matrix(rows: int, cols: int) -> list:
    matrix = []
    while len(matrix) < rows:
        matrix.append([])
        while len(matrix[-1]) < cols:
            matrix[-1].append(0.0)

    return matrix


# Creates and returns an identity matrix
def identity_matrix(n: int) -> list:
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1.0

    return I


# Sum of matrix
def matrix_sum(x: list, y: list) -> list:
  new_matrix = []

  for index_x, item_x in enumerate(x):
      new_matrix.append([])
      for index, _ in enumerate(item_x):
          new_matrix[index_x].append(y[index_x][index] + x[index_x][index])

  return new_matrix


# Subtraction of matrix
def matrix_sub(x: list, y: list) -> list:
    new_matrix = []

    for index_x, item_x in enumerate(x):
        new_matrix.append([])
        for index, _ in enumerate(item_x):
            new_matrix[index_x].append(y[index_x][index] - x[index_x][index])

    return new_matrix


# Multiplication of matrix
def matrix_mult(x: list, y: list) -> list:
    new_matrix = []

    # Cycle implementation
    # for u in range(len(x)):
    #     new_matrix.append([])
    #     for o in range(len(y[0])):
    #         for p in range(len(y)):
    #             new_matrix[u].append(x[u][p] * y[p][o])

    # A List Comprehension iterator solution
    new_matrix = [[
      sum(f * g for f, g in zip(x_row, y_col)) for y_col in zip(*y)
    ] for x_row in x]

    return new_matrix


# Other version determinant
# def determinant(matrix: list) -> float:
#     indices = list(range(len(matrix)))
    
#     if len(matrix) == 2 and len(matrix[0]) == 2:
#         val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
#         return val

#     total = 0

#     for fc in indices:
#         sub_matrix_copy = copy_matrix(matrix)
#         sub_matrix_copy = sub_matrix_copy[1:]
#         height = len(matrix)

#         for i in range(height):
#             sub_matrix_copy[i] = sub_matrix_copy[i][0:fc] + sub_matrix_copy[i][fc+1:]

#         sign = (-1) ** (fc % 2)
#         sub_det = determinant(sub_matrix_copy)
#         total += matrix[0][fc] * sign * sub_det

#     return total


# Determinant of matrix
def determinant(matrix: list) -> typing.Tuple[float, str]:
    # Establish n parameter and copy matrix
    n = len(matrix)
    CM = copy.deepcopy(matrix)
 
    # Row ops on matrix to get in upper triangle form
    for fd in range(n): # fd stands for focus diagonal
        for i in range(fd+1,n): # only use rows below fd row
            if CM[fd][fd] == 0: # if diagonal is zero - change to ~zero
                CM[fd][fd] == 1.0e-18
            # cr stands for "current row"
            try:
                crScaler = CM[i][fd] / CM[fd][fd] 

                # cr - crScaler * fdRow, one element at a time
                for j in range(n): 
                    CM[i][j] = CM[i][j] - crScaler * CM[fd][j]

            except ZeroDivisionError as e:
                err = f"Error {e} in calculating determinant for matrix:\n {matrix}"
                print(err)
                return None, err
     
    # Once CM is in upper triangle form -> product of diagonals is determinant
    product = 1.0
    for i in range(n):
        product *= CM[i][i] 
 
    return product, None


# Inversion of matrix
def inversion(matrix: list) -> typing.Tuple[list, str]:
    detr, err = determinant(matrix)
    if detr == 0:
        err = f'''
        Cannot do inverse operation because determinan of matrix(
            {matrix}
        ) is 0 and the matrix is a 'Singular Matrix'!
        '''
        print(err)
        return None, err
    elif err != None:
        return None, err
 
    # Make copies of A & I, AM & IM, to use for row ops
    n = len(matrix)
    AM = copy.deepcopy(matrix)
    I = identity_matrix(n)
    IM = copy.deepcopy(I)
 
    # Perform row operations
    indices = list(range(n)) # to allow flexible row referencing
    for fd in range(n): # fd stands for focus diagonal
        try:
            fdScaler = 1.0 / AM[fd][fd]
        except ZeroDivisionError as e:
                return None, f"Error {e} in calculating determinant for matrix:\n"
        # scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]: 
            # skip row with fd in it.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): 
                # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
 
    return IM, None


# Division of matrix
def matrix_div(x: list, y: list) -> list:

    inverted_x, err = inversion(x)
    if err != None:
        print(f"Cannot do division operation, got error in inversion: {err}")
        return None

    mult_result = matrix_mult(y, inverted_x)

    return mult_result


# Transposition of matrix
def transposition(matrix: list) -> list:
    return [[matrix[v][c] for v in range(len(matrix))] 
            for c in range(len(matrix[0]))]



EXIT_KEY = 'exit'
EXIT_DESCRIPTION = 'exit command exits program'
SHOW_KEY = 'show'
SHOW_DESCRIPTION = 'Showing matrix1 or matrix2'
SUM_KEY = 'sum'
SUM_DESCRIPTION = 'Sum of matrix1 and matrix2'
SUB_KEY = 'sub'
SUB_DESCRIPTION = 'Subtraction of matrix1 and matrix2'
MULT_KEY = 'mult'
MULT_DESCRIPTION = 'Multiplication of matrix1 and matrix2'
DETR_KEY = 'detr'
DETR_DESCRIPTION = 'Determinant of matrix'
INVERSE_KEY = 'invrs'
INVERSE_DESCRIPTION = 'Inversion of matrix'
DIV_KEY = 'div'
DIV_DESCRIPTION = 'Division of matrix1 and matrix2'
TRANSPOSITION_KEY = 'trns' 
TRANSPOSITION_DESCRIPTINO = 'Transposition of matrix'
HELP_KEY = 'help'
HELP_DESCRIPTION = 'help command shows the help message with the information about all commands'


# Function for output help info
def help_func() -> None:
    print("Commands that can be entered")
    for key, desc in [
                (EXIT_KEY, EXIT_DESCRIPTION), (SHOW_KEY, SHOW_DESCRIPTION),
                (SUM_KEY, SUM_DESCRIPTION), (SUB_KEY, SUB_DESCRIPTION), 
                (MULT_KEY, MULT_DESCRIPTION), (DETR_KEY, DETR_DESCRIPTION),
                (INVERSE_KEY, INVERSE_DESCRIPTION), (DIV_KEY, DIV_DESCRIPTION),
                (TRANSPOSITION_KEY, TRANSPOSITION_DESCRIPTINO), (HELP_KEY, HELP_DESCRIPTION)
    ]:
        print(f"Input key: {key} Description: {desc}")


# For entering matrix from keyboard
def input_matrix(matrixNumber: int) ->  typing.Tuple[list, int, int]:
    try:
        print(f"Enter the order(row and column) separated with space(' ') of matrix {matrixNumber}:")
        m, n = list(map(int, input().split()))
    except ValueError:
        print("You should enter two integer values - one for amount of rows and one for columns")
        exit(0)
    except KeyboardInterrupt:
          print("\nExiting program via Key Interruption")
          exit(0)

    print("Please enter row values separated with space(' ')")
    print("All value that are bigger then the amount of columns you entered will be trimmed")
    matrix = []
    for i in range(m):
        print("Enter row", i + 1, "values:")
        row = list(map(int, input().split()))
        r_l = len(row)
        if r_l > n:
            row = row[:n]
        elif r_l < n:
            [row.append(0) for _ in range(n - r_l)]

        matrix.append(row)

    return matrix, m, n


def main():

    matrix1, m1, n1 = input_matrix(1)
    matrix2, m2, n2 = input_matrix(2)

    print(f'Your matrix input:\n matrix1:\n\n {matrix1} \n\n matrix2:\n\n {matrix2}\n')

    print("Below are all operations that can be perform:")
    help_func()


    while True:
        try:
            input_key = input("Please Input key of operation: ").strip().lower()
        except KeyboardInterrupt:
            print("\nExiting program via Key Interruption")
            exit(0)


        if input_key == EXIT_KEY:
            print("Exit program")
            exit(0)


        elif input_key == SHOW_KEY:
            matrix_to_show = input("Enter matrix for show(output) 'm1' or 'm2': ").strip()
            if matrix_to_show == 'm1':
                print(matrix1)
            elif matrix_to_show == 'm2':
                print(matrix2)
            else:
                print("Unknown value - try again and choose matrix1 -> 'm1' or  matrix2 -> 'm2'")


        elif input_key == SUM_KEY:
            if m1 != m2 and n1 != n2:
                print('''
                Cannot do sum operation with not equal order matrices
                ''')
                continue
            print("Sum of matrix1 and matrix2: ", matrix_sum(matrix1, matrix2))


        elif input_key == SUB_KEY:
            if m1 != m2 and n1 != n2:
                print('''
                Cannot do subtraction operation with not equal order matrices
                ''')
                continue
            print("Subtraction of matrix1 and matrix2: ", matrix_sub(matrix1, matrix2))


        elif input_key == MULT_KEY:
            if m1 != n2 or m2 != n2:
                print('''
                Cannot do multiplication operation because columns of matrix1
                should be equal to rows of matrix2
                ''')
                continue
            print("Multiplication of matrix1 and matrix2: ", matrix_mult(matrix1, matrix2))


        elif input_key == DETR_KEY:
            matrix_to_determinant = input("Enter matrix for transposition 'm1' or 'm2': ").strip()
            if matrix_to_determinant == 'm1':
                result, err = determinant(matrix=matrix1)
                if err != None:
                    print(f"Error in finding determinan: {err}")
                    continue
                print(result)
            elif matrix_to_determinant == 'm2':
                result, err = determinant(matrix=matrix2)
                if err != None:
                    print(f"Error in finding determinan: {err}")
                    continue
                print(result)
            else:
                print("Unknown value - try again and choose matrix1 -> 'm1' or  matrix2 -> 'm2'")


        elif input_key == INVERSE_KEY:
            matrix_to_invert = input("Enter matrix for inversion 'm1' or 'm2': ").strip()
            if matrix_to_invert == 'm1':
                res, err = inversion(matrix=matrix1)
                if err == None:
                    print(res)
                else:
                    print(f"Go Error in inversion operation: {err}")
            elif matrix_to_invert == 'm2':
                res, err = inversion(matrix=matrix2)
                if err == None:
                    print(res)
                else:
                    print(f"Go Error in inversion operation: {err}")
            else:
                print("Unknown value - try again and choose matrix1 -> 'm1' or  matrix2 -> 'm2'")


        elif input_key == DIV_KEY:
            if m1 != n2 or m2 != n2:
                print('''
                Cannot do division operation because columns of matrix1
                should be equal to rows of matrix2
                or matrix2 is not quadratic but should be it
                ''')
                continue
            
            print("Division of two matrices: ", matrix_div(matrix1, matrix2))


        elif input_key == TRANSPOSITION_KEY:
            matrix_to_transposition = input("Enter matrix for transposition 'm1' or 'm2': ").strip()
            if matrix_to_transposition == 'm1':
                print(transposition(matrix=matrix1))
            elif matrix_to_transposition == 'm2':
                print(transposition(matrix=matrix2))
            else:
                print("Unknown value - try again and choose matrix1 -> 'm1' or  matrix2 -> 'm2'")


        elif input_key == HELP_KEY:
            help_func()


        else:
            print("Unknown command. Use 'help' for getting list of available commands\n")


main()
