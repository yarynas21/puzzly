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