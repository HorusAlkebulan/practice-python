# ordered list problem


class ListNode:
    def __init__(self, val: int) -> None:
        self.value: int = val
        self.next: ListNode = None
        self.prev: ListNode = None


class OrderedList:
    def __init__(self) -> None:
        self.head: ListNode = None
        self.tail: ListNode = None

    def add(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # head -> tail
            # head -> tail -> new_node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find_first(self, val: int) -> ListNode:
        # iterate through list until node matching value is found
        # return that node
        # if not found return None
        if self.head is None:
            return None

        cur = self.head
        while cur is not None:
            if cur.value == val:
                return cur
            else:
                cur = cur.next

        # if we get here, not found
        return None

    def to_string(self) -> str:
        if self.head is None:
            return ""

        index: int = 0
        output: str = ""
        cur = self.head
        while cur is not None:
            if index == 0:
                output = str(cur.value)
            else:
                output = output + "," + str(cur.value)
            cur = cur.next
            index += 1
        return output

def test_ordered_list_add_1():
    olist = OrderedList()

    # test adding 1
    olist.add(1)

    expected = "1"
    actual = olist.to_string()
    assert actual == expected

def test_ordered_list_add_2():
    olist = OrderedList()

    # test adding 1 2
    olist.add(1)
    olist.add(2)

    expected = "1,2"
    actual = olist.to_string()
    assert actual == expected

def test_ordered_list_add_3():
    olist = OrderedList()

    # test adding 1 2 4
    olist.add(1)
    olist.add(2)
    olist.add(4)

    expected = "1,2,4"
    actual = olist.to_string()
    assert actual == expected

def test_new_node():
    node = ListNode(1)
    actual = node.value
    expected = 1
    assert actual == expected
