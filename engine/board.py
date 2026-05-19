#board representation
#8x8 2D array
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]


def generate_pawn_moves(board, row, col,moves):
    piece = board[row][col]
    if piece == "P":
        if row == 6:
            if board[row-1][col] == ".":
                 moves.append((row, col, row - 1, col))
                 if board[row-2][col] == ".":
                     moves.append((row, col, row - 2, col))
        elif row > 0 and board[row -1][col] == ".":
            moves.append((row, col, row - 1, col))
        # capture moves
        if row >0 and col >0 and board[row -1][col -1].islower():
            moves.append((row, col, row -1, col -1))
        if row > 0 and col <7 and board[row -1][col +1].islower():
            moves.append((row, col, row -1, col +1))
        #for black pawns
    elif piece == "p":
        if row == 1:
            if board[row +1][col] == ".":
                 moves.append((row, col, row + 1, col))
                 if board[row +2][col] == ".":
                     moves.append((row, col, row + 2, col))
        elif row <7 and board[row +1][col] == ".":
            moves.append((row, col, row + 1, col))
        # capture moves
        if row <7 and col >0 and board[row +1][col -1].isupper():
            moves.append((row, col, row +1, col -1))
        if row <7 and col <7 and board[row +1][col +1].isupper():
            moves.append((row, col, row +1, col +1))
        

        
