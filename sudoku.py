# sudoku has 9 boxes and 9X9 = possibilities => 81 boxes 
# let x = row
# let y = column


board = [
    [8,0,0, 0,0,0, 0,0,0],
    [0,0,3, 6,0,0, 0,0,0],
    [0,7,0, 0,9,0, 2,0,0],
    [0,5,0, 0,0,7, 0,0,0],
    [0,0,0, 0,4,5, 7,0,0],
    [0,0,0, 1,0,0, 0,3,0],
    [0,0,1, 0,0,0, 0,6,8],
    [0,0,8, 5,0,0, 0,1,0],
    [0,9,0, 0,0,0, 4,0,0]
]

#print sudoku boxes
def print_box(board):
    for x in range(len(board)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - -")

        for y in range(len(board[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            if y == 8:
                print(board[x][y])
            else:
                print(str(board[x][y]) + " ", end="")
# print_box(board)

#find empty box
def empty_box(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                print(x, y)
                return (x, y) # row and column

# empty_box(board)