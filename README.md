# Matrix-Operations
Program Performing Matrix Operation

### Requirements 
* Python installed on your system(version 3.9 is preferrable)

### Input procedure
* Input order of matrix as exact two integer values:
`{number_of_rows} {number_of_columns}`
with 'space' separating them
* Input row's column values separating them with space. *All extra values beyond column limit*(second value in order of matrix input(previous step)) *will be trimmed*
* If there is still a possible place for column value in a row but no value was provided, then it will be filled with 0

### Additional Information
* For Sum and Subtraction the matrices(matrix1 and matrix2) have to be equal in case of order(rows == columns)
* For multiplication operation columns of matrix1 should be equal to rows of matrix2
##### DIVISION INFORMATION
* Division in fact is an operation of inversing matrix1 and multiplying it with matrix2
* For division operation(more info in above point) columns of matrix1 should be equal to rows of matrix2 and matrix2 have to be quadratic

### Available commands
```
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
```
