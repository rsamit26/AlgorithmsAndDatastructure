"""
Creating doubly Linked list and some basic operations ::
    0. create a doubly linked list
    1. add none at beginning
    2. add node at end
    3. add node at any position
    4. delete node by value
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_value(self):
        return self.val

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):

        new_node = Node(data)

        new_node.set_next(self.head)

        new_node.set_prev(None)

        if self.head is not None:
            self.head.set_prev(new_node)

        self.head = new_node

    def append_node(self, data):

        new_node = Node(data)

        new_node.set_next(None)

        if self.head is None:
            self.head = new_node
            new_node.set_prev(None)
            return

        tail = self.head

        while tail.get_next() is not None:
            tail = tail.get_next()

        tail.set_next(new_node)
        new_node.set_prev(tail)

        return

    def insert_after_node(self, prev_node, data):

        if prev_node is None:
            raise ValueError("Previous Node can't be null")

        new_node = Node(data)
        new_node.set_next(prev_node.get_next())

        prev_node.set_next(new_node)

        new_node.set_prev(prev_node)

        if new_node.get_next() is not None:
            new_node.get_next().set_prev(new_node)

    def traverse_list(self):

        p = self.head
        tail = None

        print("Traversing the list in forward order")

        while p is not None:
            print(p.get_value(), end="->")
            tail = p
            p = p.get_next()

        print("\nTraversing the list in reverse order")

        while tail is not None:
            print(tail.get_value(), end="->")
            tail = tail.get_prev()


"""Testing Code"""
l = DoublyLinkedList()
l.push("Mon")
l.push("Tue")
l.push("Wed")
l.append_node("Sun")
l.insert_after_node(l.head.next, "Sat")

l.traverse_list()
