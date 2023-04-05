def isValidMove(chess_piece_type, frm, to):
    # Convert the input strings to row-column format
    frm_col, frm_row = ord(frm[0])-ord('A'), int(frm[1])-1
    to_col, to_row = ord(to[0])-ord('A'), int(to[1])-1
    
    # Check if the from and to positions are valid
    if not (0 <= frm_col <= 7 and 0 <= frm_row <= 7 and 0 <= to_col <= 7 and 0 <= to_row <= 7):
        return False
    
    # Get the absolute differences between the rows and columns
    diff_col, diff_row = abs(to_col - frm_col), abs(to_row - frm_row)
    
    # Check the valid moves for each chess piece type
    if chess_piece_type.lower() == "pawn":
        if frm_col == to_col and frm_row - to_row == 1:
            return True
        else:
            return False
    elif chess_piece_type.lower() == "rook":
        if diff_col == 0 or diff_row == 0:
            return True
        else:
            return False
    elif chess_piece_type.lower() == "knight":
        if (diff_col == 2 and diff_row == 1) or (diff_col == 1 and diff_row == 2):
            return True
        else:
            return False
    elif chess_piece_type.lower() == "bishop":
        if diff_col == diff_row:
            return True
        else:
            return False
    elif chess_piece_type.lower() == "queen":
        if diff_col == 0 or diff_row == 0 or diff_col == diff_row:
            return True
        else:
            return False
    elif chess_piece_type.lower() == "king":
        if diff_col <= 1 and diff_row <= 1:
            return True
        else:
            return False
    else:
        return False
