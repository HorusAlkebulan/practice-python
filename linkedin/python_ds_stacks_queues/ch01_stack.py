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

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        # CASE 1: stack is empty
        if self.head is None:
            raise IndexError("Empty stack")

        # save the top to return it
        top_data = self.head.data

        # make current_node the new top
        self.head = self.head.next

        # return the saved top
        return top_data

    def peek(self):
        if self.head is None:
            raise IndexError("Empty stack")
        return self.head.data

    def isEmpty(self):
        return self.head is None
    
    def __repr__(self) -> str:
        """repr, on the other hand, is used to return a string representation of an object 
        that is a valid Python expression, which can be used to recreate the object. 
        This is typically used for debugging, logging, or serializing the object.

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __repr__(self):
                return f"Person('{self.name}', {self.age})"

        p = Person("John", 30)
        print(repr(p))  # Output: Person('John', 30)
        """

        if self.head is None:
            return ""
        
        current_node = self.head
        repr = ""
        i = 0
        items = []

        while current_node is not None:
            items.append(current_node.data)
            i += 1
            current_node = current_node.next

        while i >= 0:
            repr = repr + f"Stack().push({items[i]})\n"
            i -= 1
        return repr
    
    def __str__(self) -> str:
        """str is used to return a string representation of an object that is 
        human-readable and suitable for display to the end-user. 
        This is typically used for printing or displaying the object 
        in a user-friendly format.

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __str__(self):
                return f"{self.name}, {self.age} years old"

        p = Person("John", 30)
        print(str(p))  # Output: John, 30 years old
        """

        if self.head is None:
            return ""
        current_node = self.head
        str = ""
        i = 0
        while current_node is not None:
            if i == 0:
                str = str + f"{current_node.data} <-- top\n"
            else:
                str = str + f"{current_node.data}\n"
            i += 1
            current_node = current_node.next
        return str


# Define a function that checks if a string is a palindrome using a stack
def isPalindrome(string):

    i = 0
    stack = Stack()
    clean_string = ""
    popped_string = ""
    if len(string) == 0:
        return False

    # push chars to stack (skipping non-ascii)
    string = str(string).lower()
    while i < len(string):
        char = string[i]
        if char >= "a" and char <= "z": # or c.isalnum()
            stack.push(char)
            clean_string = clean_string + char # or use "".join(c for c in string if c.isalum())
        i += 1

    print(f"Stack after pushing string:\n{stack}")

    # pop all chars while iterating over string (chars should always match)
    while not stack.isEmpty():
        char = stack.pop()
        popped_string = popped_string + char

    strings_match = clean_string == popped_string
    print(f"stack.str:\n{stack.__str__()}")
    print(f"repr:\n{stack.__repr__()}")
    return strings_match


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


# @pytest.mark.skip(reason="Stack not finished")
def test_ex1():

    # This is how your code will be called.
    # Your answer should be the largest value in the numbers list.
    # You can edit this code to try different testing cases.
    string = "race-car!!"
    result = Answer.isPalindrome(string)
    expected = True
    assert result == expected


def test_ex2():

    # This is how your code will be called.
    # Your answer should be the largest value in the numbers list.
    # You can edit this code to try different testing cases.
    string = "race-cars!!"
    result = Answer.isPalindrome(string)
    expected = False
    assert result == expected


def test_add_one_pop_one_is_empty():

    stack = Stack()
    stack.push("r")
    top = stack.pop()
    assert top == "r"
    assert stack.isEmpty()


def test_push_two_peek():

    stack = Stack()
    stack.push("r")
    stack.push("a")
    top = stack.peek()
    assert top == "a"

test_ex1()
