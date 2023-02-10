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

