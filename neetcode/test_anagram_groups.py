# test_anagram_groups.py
# https://neetcode.io/problems/anagram-groups

from typing import List

# Anagram Groups
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # PROBLEM: if word gets put into anagram, remove it from future consideration
        # APPROACH: keep another hashmap that flags if index has been used in anagram list. Check this list before adding a word to another output list.

        # Intermediate Steps:

        anagram_map = {}
        word_used_flag = [False] * len(strs)

        # Input: strs = ["act","pots","tops","cat","stop","hat"]
        #                 i ->
        #                 cur_word
        #                       j ->

        # for each anagram group via going word by word
        for i in range(len(strs)):
            # output anagram that matches the group
            # creating hashmap keys for each string as sorted chars in word as key
            cur_word = strs[i]
            word_key = sorted(cur_word)
            word_key = "".join(word_key)

            # if exists key, get value, concatenate word to array list
            # IF haven't used the word yet
            if word_key in anagram_map and word_used_flag[i] is False:
                anagram_map[word_key].append(cur_word)
                word_used_flag[i] = True
            elif word_key not in anagram_map and word_used_flag[i] is False:
                anagram_map[word_key] = [cur_word]
                word_used_flag[i] = True
            else:
                raise ValueError("Unexpected word_key value")

            # otherwise skip (don't need it)
        # next word

        # output to result strs
        # for each key, append value array (list of strings)
        results = []
        for key in anagram_map.keys():
            anagram_array = anagram_map[key]
            results.append(anagram_array)

        return results


# Example 1:
def test_list_ex_1():

    # Input: strs = ["act","pots","tops","cat","stop","hat"]
    # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    # expected = [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    expected = [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

    solver = Solution()
    actual = solver.groupAnagrams(strs)
    assert actual == expected, f"actual={actual},\n expected={expected}"


# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
def test_single_char_ex_2():
    strs = ["x"]
    expected = [["x"]]
    solver = Solution()
    actual = solver.groupAnagrams(strs)
    assert actual == expected, f"actual={actual},\n expected={expected}"


# Example 3:
# Input: strs = [""]
# Output: [[""]]
def test_empty_3():
    strs = [""]
    expected = [[""]]
    solver = Solution()
    actual = solver.groupAnagrams(strs)
    assert actual == expected, f"actual={actual},\n expected={expected}"


# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

test_list_ex_1()
test_single_char_ex_2()
test_empty_3()
