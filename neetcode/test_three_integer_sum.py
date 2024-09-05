# test_three_integer_sum.py
from typing import List

# APPROACH 1: 3 level iteration, if sum matches 0, add to output set, otherwise no
# APPROACH 2: Use 2 sum solution with an added lead value of the sum. if too big, move right less, otherwise move left higher


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # base input checks
        if len(nums) < 3:
            return []

        results = []

        # set 3 pointers
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    # make sure all indices unique
                    if i != j and j != k and i != k:
                        sum = nums[i] + nums[j] + nums[k]
                        if sum == 0:
                            output = sorted([nums[i], nums[j], nums[k]])
                            if output not in results:
                                results.append(output)
        return results


class DebugSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # base input checks
        if len(nums) < 3:
            return []

        results = []

        # set 3 pointers
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    # make sure all indices unique
                    if i != j and j != k and i != k:
                        sum = nums[i] + nums[j] + nums[k]
                        if sum == 0:
                            output = sorted([nums[i], nums[j], nums[k]])
                            if output not in results:
                                print(f"Adding to valid output")
                                results.append(output)
                            else:
                                print(f"Already in results")
                        else:
                            print(f"Doesn't sum to 0, skipping")
        return results


def test_3_element_non_zero_sum_input():
    input = [0, 1, 1]
    solver = Solution()
    actual = solver.threeSum(input)
    expected = []
    print(f"actual={actual}, expected={expected}")
    assert actual == expected


def test_3_element_zero_sum_input():
    input = [0, 0, 0]
    solver = Solution()
    actual = solver.threeSum(input)
    expected = [[0, 0, 0]]
    print(f"actual={actual}, expected={expected}")
    assert actual == expected


def test_6_elements():
    input = [-1, 0, 1, 2, -1, -4]
    solver = Solution()
    actual = solver.threeSum(input)
    expected = [[-1, -1, 2], [-1, 0, 1]]
    print(f"actual={actual}, expected={expected}")
    for result in actual:
        assert result in expected
    assert len(actual) == len(expected)
