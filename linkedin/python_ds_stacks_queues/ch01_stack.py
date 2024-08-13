# SOURCE: https://www.linkedin.com/learning/python-data-structures-stacks-deques-and-queues/code-challenges/urn:li:la_assessmentV2:58453865?autoSkip=true&contextUrn=urn%3Ali%3AlearningCollection%3A7221626326309322752&resume=false&u=0
import pytest

# Python code​​​​​​‌​‌‌‌​​‌​​​‌‌​‌​​‌‌‌‌‌​‌​ below
# Define a node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Define a stack class using a linked list
class Stack:
    def __init__(self):
        self.head: Node = None  # The head node of the linked list
        self.top: Node = None
        

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            # new linked list
            self.head = new_node
            self.top = new_node
        else:
            # add to existing linked list
            current_top = self.top
            self.top = new_node
            current_top.next = new_node

    def pop(self):
        # CASE 1: stack is empty
        if self.head is None:
            raise IndexError("Empty stack")
        
        # CASE 2: stack has one item
        if self.head == self.top:
            old_top = self.top
            self.head = None
            self.top = None
            return old_top.data

        # CASE 3: more than one item
        # starting with head, keep calling next until current_node.next is top
        current_node = self.head
        while current_node is not None and current_node.next != self.top:
            current_node = current_node.next

        # save the top to return it
        old_top = self.top

        # make current_node the new top
        self.top = current_node

        # return the saved top
        return old_top.data

    def peek(self):
        if self.head is None:
            raise IndexError("Empty stack")
        return self.top.data

    def isEmpty(self):
        return (self.head is None)


# Define a function that checks if a string is a palindrome using a stack
def isPalindrome(string):
    # TODO: Implement the palindrome checker function
    return False


showExpectedResult = False
showHints = False


class Answer:
    def __init__(self) -> None:
        pass

    @staticmethod
    def isPalindrome(string):
        return isPalindrome(string)

def test_is_empty_true():
    
    stack = Stack()
    result = stack.isEmpty()
    expected = True
    assert result == expected

def test_is_empty_false():
    
    stack = Stack()
    stack.push("r")
    result = stack.isEmpty()
    expected = False
    assert result == expected

@pytest.mark.skip(reason="Stack not finished")
def test_ex1():

    # This is how your code will be called.
    # Your answer should be the largest value in the numbers list.
    # You can edit this code to try different testing cases.
    string = "race-car!!"
    result = Answer.isPalindrome(string)
    expected = True
    assert result == expected

# test_ex1()