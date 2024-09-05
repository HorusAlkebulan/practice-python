# SOURCE: https://www.linkedin.com/learning/get-ready-for-your-coding-interview/code-solution-to-sample-question-3-14350161?autoSkip=true&contextUrn=urn%3Ali%3AlearningCollection%3A7221626326309322752&resume=false&u=0


def rooks_are_safe(chessboard):
    # idea: basically all columns and row must be 0 or 1
    square_size = len(chessboard[0])

    # first row by row iterating across columns
    for i in range(square_size):
        row_sum = 0
        for j in range(square_size):
            row_sum += chessboard[i][j]
        if row_sum != 0 and row_sum != 1:
            return False

    # next column by column, iterating across rows
    for j in range(square_size):
        col_sum = 0
        for i in range(square_size):
            col_sum += chessboard[i][j]
        if col_sum != 0 and col_sum != 1:
            return False

    return True


if __name__ == "__main__":

    chessboard = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
    result = rooks_are_safe(chessboard)
    expected = True
    print(f"chessboard: {chessboard}, result: {result}, expected: {expected}")
    assert result == expected

    chessboard = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1]]
    result = rooks_are_safe(chessboard)
    expected = False
    print(f"chessboard: {chessboard}, result: {result}, expected: {expected}")
    assert result == expected

    chessboard = [[1]]
    result = rooks_are_safe(chessboard)
    expected = True
    print(f"chessboard: {chessboard}, result: {result}, expected: {expected}")
    assert result == expected

    chessboard = [[1, 0], [1, 0]]
    result = rooks_are_safe(chessboard)
    expected = False
    print(f"chessboard: {chessboard}, result: {result}, expected: {expected}")
    assert result == expected

    chessboard = [[0, 0, 0], [1, 0, 1], [0, 0, 0]]
    result = rooks_are_safe(chessboard)
    expected = False
    print(f"chessboard: {chessboard}, result: {result}, expected: {expected}")
    assert result == expected
