def count_negatives(given_array):

    # given largest values in each row are on the right
    # start with the top row, and column == last
    cur_row = 0
    array_edge_size = len(given_array[0])
    cur_col = array_edge_size - 1

    print(
        f"Value at (row: {cur_row}, col: {cur_col}) = {given_array[cur_row][cur_col]}"
    )

    # iterate rows from top to bottom
    overall_count = 0
    while cur_row < array_edge_size:
        print(
            f"Value at (row: {cur_row}, col: {cur_col}) = {given_array[cur_row][cur_col]}"
        )

        # iterate right to left until finding a negative value
        # determine count of values that are negative: cur_col + 1
        negative_count_in_row = 0
        while cur_col >= 0:
            if given_array[cur_row][cur_col] < 0:
                # found first negative value
                negative_count_in_row = cur_col + 1
                break
            else:
                cur_col -= 1

        overall_count += negative_count_in_row
        cur_row += 1

    return overall_count


if __name__ == "__main__":

    given_array = [[-4, -3, -1, 1], [-2, -2, 1, 2], [-1, 1, 2, 3], [1, 2, 4, 5]]
    expected = 6
    result = count_negatives(given_array)
    assert (
        result == expected
    ), f"result: {result}, expected: {expected}, locals(): {locals()}"

    given_array = [[-2, 0], [-1, 0]]
    expected = 2
    result = count_negatives(given_array)
    assert (
        result == expected
    ), f"result: {result}, expected: {expected}, locals(): {locals()}"

    given_array = [[0]]
    expected = 0
    result = count_negatives(given_array)
    assert (
        result == expected
    ), f"result: {result}, expected: {expected}, locals(): {locals()}"

    print("All tests pass.")
