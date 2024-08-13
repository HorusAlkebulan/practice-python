# SOURCE: https://www.linkedin.com/learning/python-data-structures-stacks-deques-and-queues/code-challenges/urn:li:la_assessmentV2:58453865?autoSkip=true&contextUrn=urn%3Ali%3AlearningCollection%3A7221626326309322752&resume=false&u=0


# Python code​​​​​​‌​‌‌‌​​‌​​​‌‌​‌​​‌‌‌‌‌​‌​ below
# Define a node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Define a stack class using a linked list
class Stack:
    def __init__(self):
        self.head = None  # The head node of the linked list

    def push(self, data):
        # TODO: Implement the push operation
        pass

    def pop(self):
        # TODO: Implement the pop operation
        pass

    def peek(self):
        # TODO: Implement the peek operation
        pass

    def isEmpty(self):
        # TODO: Implement the isEmpty operation
        pass


# Define a function that checks if a string is a palindrome using a stack
def isPalindrome(string):
    # TODO: Implement the palindrome checker function
    pass


showExpectedResult = False
showHints = False


class Answer:
    def __init__(self) -> None:
        pass

    @staticmethod
    def isPalindrome(string):
        return isPalindrome(string)

def test_is_empty():
    
    stack = Stack()
    result = stack.isEmpty()
    expected = True
    assert result == expected

def test_ex1():

    # This is how your code will be called.
    # Your answer should be the largest value in the numbers list.
    # You can edit this code to try different testing cases.
    string = "race-car!!"
    result = Answer.isPalindrome(string)
    expected = True
    assert result == expected

test_ex1()