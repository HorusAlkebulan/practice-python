
def solution_brute_force(arr, k):

    # ASSUMES VALID INPUTS
    sums_ls = []

    # iterate each element (i) until second to last element
    i = 0
    while i < len(arr) - 1:

        # starting with i+1, iterate each other element (j) until second to last element
        j = i + 1
        while j < len(arr):

            # compute sum, add to array
            cur_sum = arr[i] + arr[j]
            sums_ls.append(cur_sum)
            j += 1

        i += 1

    # sort array
    sorted_arr = sorted(sums_ls, reverse=True)

    # return kth element
    return sorted_arr[k - 1]

def solution_optimized(arr, k):
    pass


def test_ex1_brute_force():

    arr = [1, 2, 3, 5]
    k = 3
    expected = 6
    actual = solution_brute_force(arr, k)
    assert actual == expected

def test_ex2_brute_force():

    arr = [4, 2, 5, 5]
    k = 3
    expected = 9
    actual = solution_brute_force(arr, k)
    assert actual == expected

def test_ex1_optimized():

    arr = [1, 2, 3, 5]
    k = 3
    expected = 6
    actual = solution_optimized(arr, k)
    assert actual == expected

def test_ex2_optimized():

    arr = [4, 2, 5, 5]
    k = 3
    expected = 9
    actual = solution_optimized(arr, k)
    assert actual == expected


test_ex1_brute_force()
test_ex2_brute_force()