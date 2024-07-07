"""
Validate Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
"""


class Solution:
    def isValid(self, s: str) -> bool:
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
    solver = Solution()
    s = "[]"
    actual = solver.isValid(s)
    expected = True

def test_ex2():
    """
    Input: s = "([{}])"

    Output: true
    """
    s = "([{}])"
    expected = True

def test_ex3():
    """
    Input: s = "[(])"

    Output: false
    """
    expected = False   
    s = "[(])"