# euclid_gcd.py


def euclid_gcd_recursive(a: int, b: int):
    # base case(s): empty, single value, etc.
    if b == 0:
        return a

    # recursive case: subproblems, move towards base case
    # take diff
    remainder = a % b
    gcd = euclid_gcd_recursive(b, remainder)

    # combine sub problems
    return gcd
