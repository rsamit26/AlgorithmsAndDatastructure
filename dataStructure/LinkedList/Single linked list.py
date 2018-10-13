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
        self.next = None  # the pointer initially points to nothing

    def get_data(self):
        return self.val  # will return the value of the node

    def get_next(self):
        return self.next  # will return the next node

    def set_next(self, new_next):
        self.next = new_next  # will set a new next of the node


class ListNode:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        """
        :param data: Data to be inserted in the linked list
        :return: Connected Nodes
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def push(self, new_data):
        """ Insert a Node at the beginning of the list"""

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def append(self, end_data):
        """ Insert a Node at the end of the list"""

        end_node = Node(end_data)

        if self.head is None:
            self.head = end_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = end_node

    def insert_after(self, pos, data):
        """ Insert a Node at a given position in the list"""

        if pos is None:
            print("Given Position Not Found")
            return
        new_node = Node(data)

        new_node.next = pos.next
        pos.next = new_node

    def size_of_list(self):
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.get_next()
        return count

    def search_list(self, key):
        p = self.head
        while p:
            if p.get_data() == key:
                return p, "Found"
            else:
                p = p.get_next()
        if p is None:
            raise ValueError("Node not in list")

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

    def print_list(self):
        p = self.head  # Starting from the head node
        while p is not None:
            print(p.val)  # Printing the node value
            p = p.next  # Moving to next node


"""
Testing Code
"""
l = ListNode()
l.insert_node("Mon")
l.insert_node("Tues")
l.insert_node("Fri")

l.push("Sun")
l.append("Thu")
l.insert_after(l.head.next.next.next, "Fri")
l.remove_node("Sun")

l.print_list()
print(l.search_list("Fri"))
print(l.size_of_list())
