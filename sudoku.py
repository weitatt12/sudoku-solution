# sudoku has 9 boxes and 9X9 = possibilities => 81 boxes 
# x = row
# y = column
# check row, coloumn, and 3X3 boxes


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

#back track
def working(board):
    print(board)
    find = empty_box(board)
    if not find:
        return True
    else:
        row, col = find

    for x in range(1,10):
        if valid_num(board, x, (row, col)):
            board[row][col] = x

            if working(board):
                return True
            
            board[row][col] = 0
    return False


#check rows, column and 3X3 boxes 
def valid_num(board, num, position):
    #check rows
    for x in range(len(board[0])): #this will give me row 1
        if board[position[0]][x] == num and position[1] != x:
            return False

    #check columns
    for x in range(len(board)): #entire board
        if board[x][position[1]] == num and position[0] != x:
            return False

    #check 3X3 boxes
    box_a = position[1] // 3
    box_b = position[0] // 3

    for x in range(box_b*3, box_b*3 + 3):
        for y in range(box_a*3, box_a*3 + 3):
            if board[x][y] == num and (x,y) != position:
                return False
    return True


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

#find empty box
def empty_box(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                print(x, y)
                return (x, y) # row and column
    return None

# print(print_box(board))
working(board)
# print("________________")
# print(print_box(board))