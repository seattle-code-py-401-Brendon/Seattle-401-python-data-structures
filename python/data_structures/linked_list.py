# create node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    """
    Linked List class that uses methods of insert, includes and to string
    """

    def insert(self, value):
        # initialization here
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        # method body here
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        """
        prints LinkedList 
        """
        return f"NULL"

    


class TargetError:
    pass
