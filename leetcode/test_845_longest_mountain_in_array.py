# test_longest_mountain_in_array.py
# https://leetcode.com/problems/longest-mountain-in-array/

from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # base/edge cases
        if len(arr) < 3:
            return 0

        # APPROACH 1: try to find all mountains, return the longest?

        # note: length of mountain is (end - start) pointers

        # so basically we have two moving pointers, minimum length 3
        # start, end = 0, len(arr)-1

        # Input: arr = [    2,  1,  4,  7,  3,  2,  5]
        #                   i       j
        longest_mountain = 0
        run_count = 0
        for i in range(0, len(arr)):
            for j in range(2, len(arr)):
                # get mountain at start i, end j
                mountain_length = get_mountain(i, j, arr)
                run_count += 1
                if mountain_length > longest_mountain:
                    longest_mountain = mountain_length
        print(f"longest_mountain: {longest_mountain}, run_count: {run_count}")
        return longest_mountain


def get_mountain(window_start: int, window_end: int, arr: List[int]) -> int:

    peak_idx = -1

    # must increase until peak (which is first decrease)
    i = window_start
    while i < window_end and peak_idx < 0:
        cur = arr[i]
        next = arr[i + 1]
        if cur < next:
            # increasing, good to keep checking
            i += 1
        elif cur > next and i > window_start:
            # decreasing and not at the beginning of the window, set peak here
            peak_idx = i
        else:
            # decrease/flat before peak, invalid mountain
            return 0

    # if no peak found, invalid mountain
    if peak_idx < 0:
        return 0

    # after peak must decrease until the end (i == window(end))
    i = peak_idx
    while i < window_end:
        cur = arr[i]
        next = arr[i + 1]
        if cur > next:
            # decreasing, good to keep checking
            i += 1
        elif cur < next and i < window_end:
            # increasing before the end, invalid mountain
            return 0
        else:
            # decrease/flat before peak, invalid mountain
            return 0

    # if we get this far, increase and decreasing sides check out, return length
    length = window_end - window_start + 1
    return length


# Example 1:

# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.


def test_longest_mountain_1():

    # Input: arr = [2,1,4,7,3,2,5]
    # Input: arr = [    2,  1,  4,  7,  3,  2,  5]
    #                   i       j
    arr = [2, 1, 4, 7, 3, 2, 5]
    solver = Solution()
    actual = solver.longestMountain(arr)
    expected = 5
    assert actual == expected, f"actual={actual}, expected={expected}"


# Example 2:
# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.


def test_longest_mountain_2():
    arr = [2, 2, 2]
    solver = Solution()
    actual = solver.longestMountain(arr)
    expected = 0
    assert actual == expected, f"actual={actual}, expected={expected}"


# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104
# arr.length >= 3

# edge case
def test_longest_mountain_3():
    arr = [0]
    solver = Solution()
    actual = solver.longestMountain(arr)
    expected = 0
    assert actual == expected, f"actual={actual}, expected={expected}"


test_longest_mountain_1()
test_longest_mountain_2()
test_longest_mountain_3()
