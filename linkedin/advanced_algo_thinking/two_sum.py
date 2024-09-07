def two_sum_problem(arr: list, target: int) -> list:
    # brute force
    return two_sum_problem_brute_force(arr, target)


def two_sum_problem_brute_force(arr: list, target: int) -> list:
    # brute force
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                sum = arr[i] + arr[j]
                if sum == target:
                    return (i, j)
    return None
