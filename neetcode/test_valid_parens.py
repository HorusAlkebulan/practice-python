"""
Validate Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Constraints:

1 <= s.length <= 1000
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # neetcode solution adjusting to my coding style
        paren_stack = []
        valid_pairs_map = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        is_valid = False
        for char in s:
            if char in valid_pairs_map:
                # NOTE: Top of the stack is stack[-1]
                if len(paren_stack) > 0:
                    pop_char = paren_stack.pop()
                    if pop_char == valid_pairs_map[char]:
                        is_valid = True
                    else:
                        return False
                else:
                    return False
            else:
                paren_stack.append(char)

        # only valid if it stack is empty at this point
        is_valid = (len(paren_stack) == 0)
        return is_valid

    def isValidApproach2(self, s: str) -> bool:
        # Approach 2: use stack for chars, hashmap to pair valid opening for closing
        if len(s) < 1:
            return False
        
        paren_stack = []
        valid_pairs_map = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        # load up the stack with the string
        top = 0
        for i in range(len(s)):
            paren_stack.append(s[i])
            top += 1

        # start popping using map until you reach paired opening
        # if you reach bottom of stack without finding the valid pair, not valid
        while top > 0:
            pop_char = paren_stack.pop()
            # while reverse popping we should always be starting with a closed
            # if we pop a open to begin, we know it is not valid
            if pop_char in valid_pairs_map:
                matching_char = valid_pairs_map[pop_char]
                top -= 1
            else:
                return False

            # find matching char
            found_matching_char = False
            while not found_matching_char:
                match_pop_char = paren_stack.pop()
                top -= 1
                if top < 0:
                    return False
                if matching_char == match_pop_char:
                    # found it, we can proceed
                    found_matching_char = True

        return True

            

    def isValidApproach1(self, s: str) -> bool:
        # APPROACH 1: create 3 stacks (append and pop), iterate through string, pushing with open, pop with closed
        paren_stack = []
        curly_stack = []
        square_stack = []
        s_len = len(s)

        for i in range(s_len):
            cur_char = s[i]
            if cur_char == "(":
                paren_stack.append("(")
            elif cur_char == ")":
                if len(paren_stack) == 0:
                    return False
                else:
                    paren_stack.pop()
            elif cur_char == "{":
                curly_stack.append("{")
            elif cur_char == "}":
                if len(curly_stack) == 0:
                    return False
                else:
                    curly_stack.pop()
            elif cur_char == "[":
                square_stack.append("[")
            elif cur_char == "]":
                if len(square_stack) == 0:
                    return False
                else:
                    square_stack.pop()
        
        # we get this far, it is valid
        return True



def test_ex1():
    """
    Input: s = "[]"

    Output: true
    """
    s = "[]"
    solver = Solution()
    actual = solver.isValid(s)
    expected = True
    assert actual == expected

def test_ex2():
    """
    Input: s = "([{}])"

    Output: true
    """
    s = "([{}])"
    solver = Solution()
    actual = solver.isValid(s)
    expected = True
    assert actual == expected

def test_ex3():
    """
    Input: s = "[(])"

    Output: false
    """
    expected = False   
    s = "[(])"
    solver = Solution()
    actual = solver.isValid(s)
    assert actual == expected
