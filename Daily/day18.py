def rows_valid(board):
    for row in board:
        digit_count = [0] * 10
        for cell in row:
            if cell != '.':
                digit_count[int(cell)] += 1
                if digit_count[int(cell)] > 1:
                    return False
    return True

def columns_valid(board):
    for col in range(len(board[0])):
        digit_count = [0] * 10
        for row in range(len(board)):
            cell = board[row][col]
            if cell == '.':
                continue
            digit_count[int(cell)] += 1
            if digit_count[int(cell)] > 1:
                return False
    return True

def box_valid(board, x, y):
    digit_count = [0] * 10
    for i in range(3):
        for j in range(3):
            cell = board[i + y * 3][j + x * 3]
            if cell == '.':
                continue
            digit_count[int(cell)] += 1
            if digit_count[int(cell)] > 1:
                return False
    return True

def boxes_valid(board):
    for i in range(3):
        for j in range(3):
            if not box_valid(board, i, j):
                return False
    return True

def board_valid(board):
    return rows_valid(board) and columns_valid(board) and boxes_valid(board)

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


print(board_valid(board))