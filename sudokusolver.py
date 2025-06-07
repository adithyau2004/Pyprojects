def findnextempty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    return None,None

def isvalid(puzzle,guess,row,col):
    #check row
    rowval=puzzle[row]
    if guess in rowval:
        return False

    #check col
    colval=[]
    for i in range(9):
        colval.append(puzzle[i][col])
    if guess in colval:
        return False

    #check square
    rowstart=(row//3)*3
    colstart=(col//3)*3
    for r in range(rowstart,rowstart+3):
        for c in range(colstart,colstart+3):
            if puzzle[r][c]==guess:
                return False

    return True

def solvesudoku(puzzle):
    row,col=findnextempty(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if isvalid(puzzle,guess,row,col):
            puzzle[row][col]=guess
            if solvesudoku(puzzle):
                return True
        puzzle[row][col]=-1
    return False

def print_sudoku(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            cell = sudoku[i][j]
            print(f"{cell if cell != -1 else '_'}", end=" ")
        print()

puzzle=[
    [ 3, 9,-1,   -1, 5,-1,   -1,-1,-1],
    [-1,-1,-1,    2,-1,-1,   -1,-1, 5],
    [-1,-1,-1,    7, 1, 9,   -1, 8,-1],

    [-1, 5,-1,   -1, 6, 8,   -1,-1,-1],
    [ 2,-1, 6,   -1,-1, 3,   -1,-1,-1],
    [-1,-1,-1,   -1,-1,-1,   -1,-1, 4],

    [ 5,-1,-1,   -1,-1,-1,   -1,-1,-1],
    [ 6, 7,-1,    1,-1, 5,   -1, 4,-1],
    [ 1,-1, 9,   -1,-1,-1,    2,-1,-1]
]

print_sudoku(puzzle)

solvesudoku(puzzle)

print('''
solved sudoku
''')

print_sudoku(puzzle)