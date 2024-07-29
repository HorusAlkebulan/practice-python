# singly_linked_list.py

"""
Singly-linked lists are a type of linked list where nodes have only one pointer: A pointer to the next element. 
Create a class SinglyLinkedList along with its methods:

add_head(element) - adds an element to the head of the list. This becomes the new head of the linked list.
add_tail(element) - adds an element to the tail of the list. This becomes the new tail of the linked list.
remove_head() -> element - removes the head and returns the value of the removed element.
remove_tail() -> element - removes the tail and returns the value of the removed element.
__contains__(item) -> bool - checks if the item is inside the list. Returns True if it is inside the list and returns False if not. This method is implemented to allow the use of Python’s in operator.
__getitem__(index) - returns the element at the specified index. Raises an IndexError if the index is out of bounds. This method is implemented to allow the use of Python’s [] operator.
__len__() - returns the length of the SinglyLinkedList.
"""

"""
Notes:

for example, linked list of 10, 20, 30

head -> ["10"] -> ["20"] -> ["30"] -> tail

"""

class Node():
    def __init__(self, element: any, next: any) -> None:
        self.element: any = element
        self.next: Node = next

    def __str__(self) -> str:
        return str(self.element)

class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        self.tail = None

    def add_head(self, element: any) -> None:
        """
        head -> ["10"] -> ["20"] -> ["30"] <- tail
        ["5"]
        head -> ["5"]
        """
        if self.size == 0:
            self.head = Node(element, None)
            self.tail = self.head
        else:
            self.head = Node(element, self.head)
        self.size += 1

    def add_tail(self, element: any) -> None:
        """
        head -> ["10"] -> ["20"] -> ["30"] <- tail
        ["40"]
        head -> ["10"] -> ["20"] -> ["30"] -> ["40"] <- tail
        """
        if self.size == 0:
            self.tail = Node(element, None)
            self.head = self.tail
        else:
            old_tail = self.tail
            self.tail = Node(element, None)
            old_tail.next = self.tail
        self.size += 1

    def remove_head(self) -> any:
        """
        head -> ["10"] -> ["20"] -> ["30"] <- tail
        head -> ["20"] -> ["30"] <- tail
        """
        if self.size == 0:
            return None
        
        popped_value = self.head.element
        new_head = self.head.next
        self.head = new_head
        self.size -= 1
        return popped_value

    def remove_tail(self) -> any:
        """
        head -> ["10"] -> ["20"] -> ["30"] <- tail
        head -> ["10"] -> ["20"] <- tail
        """     
        if self.size == 0:
            return 
        
        popped_value = self.tail.element

        # since singly linked, have to traverse the list
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            # head -> ["10"] -> ["20"] -> ["30"] <- tail
            #           cur       next
            #                     cur       next
            cur_node = self.head
            next_node = cur_node.next
            while next_node.next is not None:
                # move forward
                cur_node = next_node
                next_node = cur_node.next
            new_tail = cur_node
            new_tail.next = None
            self.tail = new_tail
        self.size -= 1
        return popped_value
    
    def __contains__(self, item: any) -> bool:
        if self.size == 0:
            return False
        
        cur_node = self.head
        while cur_node is not None:
            if cur_node.element == item:
                return True
            cur_node = cur_node.next

        return False


    def __getitem__(self, index: int) -> Node:
        if self.size == 0:
            raise IndexError("List is empty")
        if index > self.size - 1:
            raise IndexError(f"Invalid index: {index}")
        
        cur_node = self.head
        for _ in range(index):
            cur_node = cur_node.next
        return cur_node.element

    def __len__(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        cur_node = self.head
        contents_lst = []
        while cur_node is not None:
            contents_lst.append(cur_node.element)
            cur_node = cur_node.next

        return f"head: {self.head}, tail: {self.tail}, size: {self.size}, contents: {str(contents_lst)}"

if __name__ == "__main__":

    list = SinglyLinkedList()
    print(f"list: {list}")
    list.add_head(10)
    print(f"list: {list}")
    list.add_tail(20)
    print(f"list: {list}")
    list.add_tail(30)  
    print(f"list: {list}") 
    list.add_tail(40)  
    print(f"list: {list}")
    list.add_head(5)  
    print(f"list: {list}")
    list.remove_head()
    print(f"after remove_head(), list: {list}")
    list.remove_tail()
    print(f"after remove_tail(), list: {list}")