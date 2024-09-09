# euclid_gcd.py


# def euclid_gcd(a_list: list):
#     result = 0
#     for val in a_list:
#         result += val
#     return result


def euclid_gcd_recursive(a: int, b: int):
    # base case(s): empty, single value, etc.
    remainder = a % b
    if remainder == 0:
        return b

    # recursive case: subproblems, move towards base case
    # take diff
    gcd = euclid_gcd_recursive(b, remainder)

    # combine sub problems
    return gcd
