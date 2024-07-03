# test_longest_substring_without_duplicates.py

# Longest Substring Without Duplicates
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "zxyzxyz"
# Output: 3

# Explanation: The string "xyz" is the longest without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # APPROACH 4: uses sliding window technique
        char_set = set()
        l = 0
        result = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l = l + 1
            char_set.add(s[r])
            result = max(result, r - l + 1)
        return result


class SolutionV2:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # APPROACH 3: 
        # since limited set of chars, just create set of chars used

        if len(s) == 0: 
            return 0
        
        chars = list(s)
        char_map = set()
        for c in chars:
            char_map.add(c)
        result_len = len(char_map)
        return result_len



class SolutionV1:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # s = "xxxx"

        # APPROACH 2: 
        # since limited set of chars, just create hash map of all ascii chars used

        if len(s) == 0: 
            return 0
        
        chars = list(s)
        char_map = {}
        for c in chars:
            ascii_val = ord(c)
            if ascii_val not in char_map:
                char_map[ascii_val] = 1
            else:
                char_map[ascii_val] = char_map[ascii_val] + 1

        result = ""
        for char_key in char_map.keys():
            result = result + chr(char_key)
        result_len = len(result)
        return result_len

class SolutionV0:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # s = "xxxx"

        # APPROACH 1: 
        # (a) sort and find unique characters. 
        # (b) for each unique character, do the same for remaining subproblem working recursively?

        # Ex 2
        # s = "xxxx"
        # sorted = "xxxx"
        # unique = "x"
        # index = "x", recursive subproblem = ""
        #   subprob returns ""
        # get len of chars
        # return len as size
        if len(s) == 0: 
            return 0
        chars = list(s)
        chars_sorted = sorted(chars)
        results = []
        for i in range(len(chars_sorted)):
            if chars_sorted[i] not in results:
                results.append(chars_sorted[i])
        result_len = len(results)
        return result_len
    
# Example 1:

# Input: s = "zxyzxyz"
# sorted = "xxyyzzz"
# unique = "xyz"
# index = "x", recursive subprob = "yz"

def test_ex_1():
    s = "zxyzxyz"
    solver = Solution()
    actual = solver.lengthOfLongestSubstring(s)
    expected = 3
    assert actual == expected, f"locals: {locals()}"

# Example 2:

# Input: s = "xxxx"

# Output: 1

def test_length_single_char():
    s = "xxxx"
    solver = Solution()
    actual = solver.lengthOfLongestSubstring(s)
    expected = 1
    assert actual == expected, f"locals: {locals()}"


# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.

def test_constraints_0():
    s = ""
    solver = Solution()
    actual = solver.lengthOfLongestSubstring(s)
    expected = 0
    assert actual == expected, f"locals: {locals()}"


def test_pwwkew():
    s="pwwkew"
    solver = Solution()
    actual = solver.lengthOfLongestSubstring(s)
    expected = 3
    assert actual == expected, f"locals: {locals()}"








