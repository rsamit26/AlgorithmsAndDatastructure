"""
Linked list and some basic operations ::
    0. create a singly linked list
    1. add none at beginning
    2. add node at end
    3. add node at any position
    4. delete node by value

"""



class Node:
    def __init__(self, v):
        self.val = v
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    def print_list(self):
        p = self.head
        while p is not None:
            print(p.val)
            p = p.next

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def insert_at_end(self, end_data):

        end_node = Node(end_data)

        if self.head is None:
            self.head = end_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = end_node

    def insert_at_position(self, pos, data):

        if pos is None:
            print("Given Position Not Found")
            return
        new_node = Node(data)

        new_node.next = pos.next
        pos.next = new_node

    def remove_node(self, remove_key):

        head = self.head
        prev = None

        if head is not None:
            if head.val == remove_key:
                self.head = head.next
                head = None
                return

        while head is not None:
            if head.val == remove_key:
                break
            prev = head
            head = head.next

        if head.val is None:
            return

        prev.next = head.next




"""
Testing Code
"""
l = ListNode()
l.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

l.head.next = e2
e2.next = e3

l.insert_at_beginning("Sun")
l.insert_at_end("Thu")
l.insert_at_position(l.head.next.next.next, "Fri")
l.remove_node("Sun")

l.print_list()
