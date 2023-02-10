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
