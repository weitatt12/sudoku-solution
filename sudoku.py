# sudoku has 9 boxes and 9X9 = possibilities => 81 boxes 
# x = row
# y = column
# check row, coloumn, and 3X3 boxes


board = [
    [1,0,3, 0,0,5, 0,0,8],
    [0,8,0, 0,0,0, 5,6,0],
    [2,0,0, 0,9,0, 0,0,0],

    [0,3,9, 0,1,0, 0,0,0],
    [5,0,0, 0,0,0, 0,0,4],
    [0,0,0, 0,8,0, 9,5,0],

    [0,0,0, 0,3,0, 0,0,5],
    [0,1,2, 0,0,0, 0,8,0],
    [9,0,0, 6,0,0, 3,0,1]
]

#back track
def working(board):
    # print(board)
    find = empty_box(board)
    if not find:
        return True
    else:
        row, col = find

    for x in range(1,10):
        if check_num(board, x, (row, col)):
            board[row][col] = x

            if working(board):
                return True
            
            board[row][col] = 0
    return False

#check rows, column and 3X3 boxes 
def check_num(board, num, position):
    #check rows
    for x in range(len(board[0])): #this will give me row 1
        if board[position[0]][x] == num and position[1] != x:
            # print(position[1])
            return False

    #check columns
    for x in range(len(board)): #entire board
        if board[x][position[1]] == num and position[0] != x:
            # print(board[x][position[1]])
            return False

    #check 3X3 boxes (with these 2 box will give me (0,1,2) "index" only, it will gives me 1/9 box)
    box_a = position[1] // 3 #columns //positions[1] give the entire column divide 3 is to get one box
    box_b = position[0] // 3 #rows //position[0] gives entire row divide 3 get one box
    # max is (6,9) but not including 9 == same as based on index

    for x in range(box_b*3, box_b*3 + 3): 
        for y in range(box_a*3, box_a*3 + 3):
            if board[x][y] == num and position != (x,y):
                return False
    return True

#find empty box
def empty_box(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                return (x, y) # row and column
    return None

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


print(print_box(board))
working(board)
print(print_box(board))