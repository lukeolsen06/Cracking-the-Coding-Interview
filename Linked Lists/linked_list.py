
# Classes for Node and LinkedList. Will add method functions as needed

# Node class for the linked list
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# LinkedList class
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def append(self, val):
        """Add a node with value val at the end of the list."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node



# Visualization function (outside of classes)
def print_linked_list(head):
    """Print the linked list in the format: val1 -> val2 -> ... -> None"""
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))