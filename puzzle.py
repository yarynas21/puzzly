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
