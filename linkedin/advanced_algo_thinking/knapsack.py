# knapsack.py


def knapsack(max_capacity: int, weights: list, values: list) -> list:
    # create the empty table
    capacity_table = []
    for i in range(len(values)):
        capacity_row = []
        for j in range(max_capacity + 1):
            capacity_row.append(0)
        capacity_table.append(capacity_row)

    # iterate over rows
    for i in range(1, len(values)):

        # iterate over columns, computing max of
        for j in range(1, max_capacity + 1):

            # 1. previous max (cell[i-1][j])
            # 2. value of current item + value of remaining space (cell[i-1][j-weight])
            previous_max = capacity_table[i - 1][j]
            value = values[i]
            weight = weights[i]
            if j - weight >= 0:
                remain_space_value = capacity_table[i - 1][j - weight]
                max_value = max(previous_max, value + remain_space_value)
            else:
                max_value = previous_max

            # store max value in table
            capacity_table[i][j] = max_value

    # return final table
    return capacity_table
