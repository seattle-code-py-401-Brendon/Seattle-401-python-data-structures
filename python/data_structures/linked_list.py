# create node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    """
    Linked List class that uses methods of insert,...
    """

    def insert(self, value):
        # initialization here
        node = Node(value)
        node.next = self.head
        self.head = node

    def some_method(self):
        # method body here
        pass


class TargetError:
    pass
