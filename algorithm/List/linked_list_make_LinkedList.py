"""
Linked List 구현
"""


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# first = Node(1)
# second = Node(2)
# third = Node(3)
# first.next = second
# second.next = third
# first.value = 6


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def append_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def insert(self, idx, value):
        current = self.head
        new_node = Node(value)
        for _ in range(idx - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove(self, idx):
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        current.next = current.next.next


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert(2, 9)
print(ll.get(0), ll.get(1), ll.get(2), ll.get(3))
ll.remove(1)
print(ll.get(0), ll.get(1), ll.get(2), ll.get(3))
