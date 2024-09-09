# list_sum.py


def list_sum(a_list: list):
    result = 0
    for val in a_list:
        result += val
    return result


def list_sum_recursive(a_list: list):
    # base case(s): empty, single value, etc.
    if len(a_list) == 0:
        return 0
    if len(a_list) == 1:
        return a_list[0]

    # recursive case: subproblems
    # split list and sum becomes left + right side of list
    split_point_idx = len(a_list) // 2
    left = a_list[0:split_point_idx]
    right = a_list[split_point_idx:]
    left_sum = list_sum_recursive(left)
    right_sum = list_sum_recursive(right)
    return left_sum + right_sum
