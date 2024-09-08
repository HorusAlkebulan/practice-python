def two_sum_problem(arr: list, target: int) -> tuple:
    # brute force
    # return two_sum_problem_brute_force(arr, target)

    # optimized
    return two_sum_hash_table(arr, target)


def two_sum_problem_brute_force(arr: list, target: int) -> tuple:
    # brute force
    # loop through 2nd to last item
    for i in range(len(arr) - 1):
        # start with 2nd item
        for j in range(i + 1, len(arr)):
            if i != j:
                sum = arr[i] + arr[j]
                if sum == target:
                    return (i, j)
    return None


def two_sum_hash_table(arr: list, target: int) -> tuple:

    # initialize
    hash_map = {}

    # iterate over array
    for i, value in enumerate(arr):

        # needed value = target - current value
        needed_value = target - value

        # needed value in dict?
        if needed_value in hash_map:

            # if yes, return current index and other index
            return (i, hash_map[needed_value])

        # otherwise continue
        # if current item value in dict, no op
        # otherwise, add using current item value as key, index as value
        if value not in hash_map:
            hash_map[value] = i

    # if get to the end, not found, return None
    return None
