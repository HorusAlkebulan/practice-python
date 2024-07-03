# test_kth_largest_integer_in_a_stream.py

# Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

# Implement the following methods:

# constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
# int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

# MY APPROACH

# Given we have a heap, we can do a max heap, add the values, then pop k times

# i.e.
#       3
#
#     3   2
#
#   1

from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initialize with 0 already in place. actually not needed using internal heapq
        self.heap = []
        self.k = k
        # add numbers to the heap
        for num in nums:
            heapq.heappush(self.heap, num)

    def get_heap(self) -> list[int]:
        return self.heap

    def add(self, val: int) -> int:
        # add to the heap
        heapq.heappush(self.heap, val)

        # return k'th largest. NOTE: nlargest returns high to low order
        kth_largest = heapq.nlargest(self.k, self.heap)
        return kth_largest[self.k - 1]
        
# Example 1:

# Input:
# ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
def test_get_heap():
    nums = [1, 2, 3, 3]
    k = 3
    heap = KthLargest(k, nums)
    contents = heap.get_heap()
    print(contents)
    assert contents is not None

# Output:
# [null, 3, 3, 3, 5, 6]

# Explanation:
# KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);

def test_add_3_5_6_7_8():
    nums = [1, 2, 3, 3]
    k = 3
    heap = KthLargest(k, nums)
    contents = heap.get_heap()
    print(contents)
    assert contents is not None
    # kthLargest.add(3);   // return 3
    res = heap.add(3)
    # kthLargest.add(5);   // return 3
    res = heap.add(5)
    # kthLargest.add(6);   // return 3
    res = heap.add(6)
    # kthLargest.add(7);   // return 5
    res = heap.add(7)
    # kthLargest.add(8);   // return 6
    res = heap.add(8)
    print(f"res={res}")
    assert res == 6
# Constraints:

# 1 <= k <= 1000
# 0 <= nums.length <= 1000
def test_nums_length_0():
    nums = []
    k = 1
    heap = KthLargest(k, nums)
    res = heap.add(9)
    assert res == 9

# -1000 <= nums[i] <= 1000
# -1000 <= val <= 1000
# There will always be at least k integers in the stream when you search for the kth integer.
def test_negative_nums():
    nums = [-1, 2, 3, 3]
    k = 2
    heap = KthLargest(k, nums)
    res = heap.add(-4)
    assert res == 3

test_get_heap()
test_add_3_5_6_7_8()
test_nums_length_0()