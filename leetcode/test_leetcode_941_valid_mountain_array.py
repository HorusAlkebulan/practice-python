# test_leetcode_valid_mountain_array.py

# pytest leetcode/test_leetcode_941_valid_mountain_array.py -s -v

# 941. Valid Mountain Array
# Given an array of integers arr, return true if and only if it is a valid mountain array.
from typing import List

# import pytest
# len = 4
# arr = [0,    3,  2,  1], expected = True
# idx =  0      1   2   3
#        start          end
# peak
#        i      i+1

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        print(f"validMountainArray({arr})")
        # set up the window
        window_start_idx = 0
        window_end_idx = len(arr) - 1
        current_peak_idx = -1
        current_valley_idx = -1
        result = valid_mountain(
            arr, window_start_idx, window_end_idx, current_peak_idx, current_valley_idx
        )
        return result


def valid_mountain(
    arr: List[int], start: int, end: int, current_peak_idx: int, current_valley_idx: int
) -> bool:

    # param check
    if start == end:
        return False

    for i in range(start, end, 1):
        cur = arr[i]
        next = arr[i + 1]

        # pairwise compare to determine if increasing/decreasing
        if next > cur:
            if current_peak_idx < 0 and current_valley_idx < 0:
                current_peak_idx = i + 1
            elif current_peak_idx < 0 and current_valley_idx > 0:
                raise ValueError("Peak not yet set, but valley set")
            elif current_peak_idx > 0 and current_valley_idx < 0:
                current_peak_idx = i + 1
            else:  # elif current_peak_idx > 0 and current_valley_idx > 0:
                return False
        elif next < cur:
            if current_peak_idx > 0:
                current_valley_idx = i + 1
            else:  # current_peak_idx < 0:
                return False
        else:
            return False

    # if get to the end with no valley, means only up slope found
    if current_valley_idx < 0:
        return False
    else:
        return True

def valid_mountain_with_log(arr: List[int], start: int, end: int) -> bool:

    # param check
    if start == end:
        return False

    current_peak_idx = -1
    current_valley_idx = -1

    for i in range(start, end, 1):
        cur = arr[i]  # 0
        next = arr[i + 1]  # 3

        print(f"\tlocals: {locals()}")

        # pairwise compare to determine if increasing/decreasing
        if next > cur:
            print(f"Increasing")
            if current_peak_idx < 0 and current_valley_idx < 0:
                print(f"\tPeak not yet set, set to {i+1}, valley not yet set")
                current_peak_idx = i + 1
            elif current_peak_idx < 0 and current_valley_idx > 0:
                raise ValueError(f"\tPeak not yet set, but valley set")
            elif current_peak_idx > 0 and current_valley_idx < 0:
                print(
                    f"\tPeak set this is higher and valley not yet set, so set to {i+1}"
                )
                current_peak_idx = i + 1
            elif current_peak_idx > 0 and current_valley_idx > 0:
                print(
                    f"\tIncreasing again after finding a valley, therefore no longer a mountain"
                )
                return False
            else:
                raise ValueError("Invalid branch")
        elif next < cur:
            print(f"Decreasing")
            if current_peak_idx > 0:
                current_valley_idx = i + 1
                print(
                    f"Peak set to {current_peak_idx}, setting valley idx to {current_valley_idx}"
                )
            elif current_peak_idx == -1:
                print(f"Valley found before peak, not a mountain.")
                return False
            else:
                raise ValueError("Invalid branch")
        else:
            print(f"Constant, not allowed")
            return False

    print(f"getting this far, means we got to the end on a decreasing not. We're good!")
    return True


# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104


# Example 1:
# Input: arr = [2,1]
# Output: false
def test_example_1():
    arr = [2, 1]
    expected = False
    base_test_example(arr, expected)


def base_test_example(arr, expected):
    solver = Solution()
    actual = solver.validMountainArray(arr)
    assert expected == actual, f"Failed - arr: {arr}, expected: {expected}"


# Example 2:
# Input: arr = [3,5,5]
# Output: false
def test_example_2():
    arr = [3, 5, 5]
    expected = False
    base_test_example(arr, expected)


# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
def test_example_3():
    arr = [0, 3, 2, 1]
    expected = True
    base_test_example(arr, expected)


def test_example_4():
    arr = [2, 4, 6, 8, 10, 9, 4, 0]
    expected = True
    base_test_example(arr, expected)


def test_example_5():
    # len(arr) == 1
    arr = [5]
    expected = False
    base_test_example(arr, expected)

def test_example_6():
    # only increasing
    arr = [0,1,2,3,4,5,6,7,8,9]
    expected = False
    base_test_example(arr, expected)

if __name__ == "__main__":

    test_example_1()
    test_example_2()
    test_example_3()
