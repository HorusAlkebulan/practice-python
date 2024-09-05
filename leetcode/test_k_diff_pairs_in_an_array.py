# 532. K-diff Pairs in an Array
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

        A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

        0 <= i, j < nums.length
        i != j
        |nums[i] - nums[j]| == k
        Notice that |val| denotes the absolute value of val.
        """

        if k < 0:
            return 0

        # ex
        #   3   1   4   1   5

        # store counts of each unique value
        value_freq_map = {}
        for num in nums:
            if num in value_freq_map:
                value_freq_map[num] += 1
            else:
                value_freq_map[num] = 1

        #   key     3   1   4   5
        #   value   1   2   1   1
        #           i

        # k = 2
        results = []
        for num in value_freq_map:
            if k == 0:
                # only way to get 0 diff if subtracting duplicates
                if value_freq_map[num] > 1:
                    results.append([num, num])
            else:
                # check for each num in the map, does the needed matching num exist
                # so, (num - x) must equal k or (num - x) must equal -k
                # or, (3 - x) = 2 or (3 - x) = -2
                # or, x = (3 - 2) or 3 + 2 = x
                # or, x = 1 or x = 5
                # rewriting in terms of vars
                # so, (num - paring_needed) = k or (num - pairing_needed) = -k
                # or, paring_needed = num - k or paring_needed = num + k
                paring_needed_pos = num - k
                paring_needed_neg = num + k
                # if paring_needed_pos in value_freq_map:
                #     results.append([num, paring_needed_pos])
                # NOTE: Not sure why including both produces duplicates
                if paring_needed_neg in value_freq_map:
                    results.append([num, paring_needed_neg])
        # print(f"results: {results}")
        results_count = len(results)
        return results_count


"""

Constraints:

1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107
"""


def test_ex1():
    """
    Example 1:

    Input: nums = [3,1,4,1,5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.
    """
    nums = [3, 1, 4, 1, 5]
    k = 2
    expected = 2

    solver = Solution()
    actual = solver.findPairs(nums, k)
    assert actual == expected


def test_ex2():
    """
    Example 2:

    Input: nums = [1,2,3,4,5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
    """
    nums = [1, 2, 3, 4, 5]
    k = 1
    expected = 4

    solver = Solution()
    actual = solver.findPairs(nums, k)
    assert actual == expected


def test_ex3():
    """
    Example 3:

    Input: nums = [1,3,1,5,4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).
    """
    nums = [1, 3, 1, 5, 4]
    k = 0
    expected = 1

    solver = Solution()
    actual = solver.findPairs(nums, k)
    assert actual == expected
