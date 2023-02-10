"""Module"""
def check_row(board):
    """
    Check row if they have more than one number.
    If yes - return False, else True.
    >>> check_row(['**** ****', '***1 ****', '**  3****', '* 4 1****',\
    '     9 5 ', ' 6  83  *', '3  1  ** ', '  8  2***', '  2  ****'])
    True
    >>> check_row(['**** ****', '***1 ****', '**  3****', '* 4 1****',\
    '     9 5 ', ' 6  83  *', '3  11 ** ', '  8  2***', '  2  ****'])
    False
    """
    for row in board:
        for eli in row:
            if eli != '*' and eli != ' ':
                if row.count(eli) > 1:
                    return False
    return True
def convert_to_columns(board):
    """
    Function which converts rows to columns.
    >>> convert_to_columns(['**** ****', '***1 ****', '**  3****', '* 4 1****',\
    '     9 5 ', ' 6  83  *', '3  1  ** ', '  8  2***', '  2  ****'])
    ['****  3  ', '***  6   ', '** 4   82', '*1    1  ', '  31 8   ',\
 '****93 2*', '****  ***', '****5 ***', '**** * **']
    >>> convert_to_columns(['**** ****', '***1 ****', '**  3****', '* 4 1****',\
    '     9 5 ', ' 6  83  *', '3  11 ** ', '  8  2***', '  2  ****'])
    ['****  3  ', '***  6   ', '** 4   82', '*1    1  ', '  31 81  ', '****93 2*',\
 '****  ***', '****5 ***', '**** * **']
    """
    res = [[board[i][col] for i in range(len(board))] for col in range(len(board[0]))]
    temp = ["".join(elem) for elem in res]
    return temp
def check_column(board):
    """
    Check columns if they have more than one number.
    If yes - return False, else True.
    >>> check_column(['****  3  ', '***  6   ', '** 4   82', '*1    1  ',\
    '  31 8   ', '****93 2*', '****  ***', '****5 ***', '**** * **'])
    True
    >>> check_column(['****  3  ', '***  6   ', '** 4   82', '*1    1  ',\
    '  31 81  ', '****93 2*', '****  ***', '****5 ***', '**** * **'])
    False
    """
    temp = convert_to_columns(board)
    for row in temp:
        for eli in row:
            if eli != '*' and eli != ' ':
                if row.count(eli) > 1:
                    return False
    return True

def check_block(board):
    """
    Check blocks of the board if they have more than one number.
    If yes - return False, else True.
    >>> check_block(["**** ****","***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    """
    row = board
    columns = convert_to_columns(board)
    columns_r = [columns[i][::-1][i:][::-1] for i in range(len(columns))]
    rows_r = [row[::-1][y][y+1:] for y in range(len(row))]
    res = [i for i in map(list, zip(columns_r, rows_r))]
    res1 = []
    for elem in res:
        for i in enumerate(elem):
            res1.append(elem[0] + elem[1])
    smth = slice(0, len(res1), 2)
    end = res1[smth][:5]
    for row in end:
        for eli in row:
            if eli != '*' and eli != ' ':
                if row.count(eli) > 1:
                    return False
    return True

def validate_board(board):
    """
    Full and main function that checks all functions.
    >>> validate_board(["**** ****","***1 ****","**  3****",\
    "* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    >>> validate_board(["****1****","*** 2****","**  3****",\
    "*   4****","1   56789","        *","2      **","      ***","3 4  ****"])
    True
    """
    result = check_row(board) and check_column(board) and check_block(board)
    return result
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())