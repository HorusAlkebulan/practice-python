"""
test_is_palindrome.py

Is Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # APPROACH 1:
        # two pointers from each end, skipping non alphanumerical

        # "Was it a car or a cat I saw?"
        #  i                          j
        i = 0
        j = len(s) - 1
        while i < len(s) and j > 0:
            # if char is non-alpha, skip it by incrementing only
            is_alpha = (s[i] >= "a" and s[i] <= "z") or (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "0" and s[i] <= "9")
            if not is_alpha:
                i += 1
                continue

            is_alpha = (s[j] >= "a" and s[j] <= "z") or (s[j] >= "A" and s[j] <= "Z") or (s[j] >= "0" and s[j] <= "9")
            if not is_alpha:
                j -= 1
                continue

            # otherwise if alpha
            # is lower case of char at i equal to char at j
            if s[i].lower() == s[j].lower():
                # increment both pointers
                i += 1
                j -= 1
            else:
                # otherwise return false
                return False

        # reach this, is valid, return True
        return True


"""
Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

"""


def test_ex1():
    solver = Solution()
    s = "Was it a car or a cat I saw?"
    expected = True
    actual = solver.isPalindrome(s)
    assert actual == expected


"""
Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
123
class Solution:
    def isPalindrome(self, s: str) -> bool:

"""


def test_ex2():
    solver = Solution()
    s = "tab a cat"
    expected = False
    actual = solver.isPalindrome(s)
    assert actual == expected


def test_numeric():
    solver = Solution()
    s = "234,010,432"
    expected = True
    actual = solver.isPalindrome(s)
    assert actual == expected


def test_single_numeric_and_alpha():
    solver = Solution()
    s = "Z6"
    expected = False
    actual = solver.isPalindrome(s)
    assert actual == expected
