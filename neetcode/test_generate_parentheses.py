""" Notes

git config --global user.email "horusjr@me.com"
git config --global user.name "Horus Alkebu-Lan"

Stack

putting 1, 2, 3

3 <--- top
2
1

FILO
LIFO

Contraints:
1 <= n <= 7

Intuition:
- need to come with all the possible sequences of 
    - "(": starts a group
    - ")"

- n = 2
- push "("

left:
( <--- top
(

right:
) <--- top
)

(

for i in range(2 ** 1)
    - must start with left

Suggested:
- only add open parens if open < n
- only add closing paren if closed < open
- solution valid IIF open == closed == n
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        print(f"n={n}")
        
        stack = []
        res = []

        def backtrack_gen(n: int, open: int, closed: int):
            # - solution valid IIF open == closed == n
            if n == open and open == closed:
                list_to_string = "".join(stack)
                res.append(list_to_string)
                return
            
            # - only add open parens if open < n
            if open < n:
                stack.append("(")
                backtrack_gen(n, open+1, closed)
                stack.pop()     # undo to try another tree branch

            # - only add closing paren if closed < open
            if closed < open:
                stack.append(")")
                backtrack_gen(n, open, closed+1)
                stack.pop()

        # begin
        backtrack_gen(n, 0, 0)
        return res
    

def test_ex1():
    solver = Solution()
    n = 1
    actual = solver.generateParenthesis(n)
    expected = ["()"]
    assert actual == expected
