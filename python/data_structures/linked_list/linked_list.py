# create node class
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Linked list class with methods to insert, append, includes, insert before, insert after and convert to string
    """
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """Insert New Node with Value into Linked List

        Args:
            value (any): the value of the node, can be any data type
        """
        # initialization here
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        """traverse through Linked List and search for node in linked list

        Args:
            value (any): the nodes value that the method is searching for

        Returns:
            boolean: returns True or False if node is in Linked List
        """
        # method body here
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False


    def append(self, value):
        """add Node to the end of the Linked List

        Args:
            value (any): the data type can be any
        """
        node = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_before(self, query, value):
        """insert a node before a specific node in the linked list

        Args:
            query (any): the point where we want to insert before
            value (any): the new node with a value that we will insert before the query
        """
        pass

    def insert_after(self, query, value):
        pass

    def __str__(self):
        """
        convverts the Linked List to a string and returns the contents as a string 
        """
        current = self.head
        values = ""
        if self.head is None:
         return f"NULL"
        while current != None:
            values += "{}".format('{ ' + f"{current.value}" + ' } -> ')
            current = current.next
        values += "NULL"
        return values
        


    


class TargetError:
    pass
