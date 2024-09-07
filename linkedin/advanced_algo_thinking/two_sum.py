def two_sum_problem(arr: list, target: int) -> list:
    # brute force
    return two_sum_problem_brute_force(arr, target)


def two_sum_problem_brute_force(arr: list, target: int) -> list:
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
