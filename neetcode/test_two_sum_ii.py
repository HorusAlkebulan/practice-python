# TWO SUM II - Amazon Coding Interview Question - Leetcode 167 - Python

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        #   1   3   4   5   7   11
        #   l                   r

        # dont allow pointers to cross each other
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []

def test_ex1():
    numbers = [1, 3, 4, 5, 7, 11]
    target = 9
    solver = Solution()
    actual = solver.twoSum(numbers, target)
    expected = [3, 4]
    assert actual == expected