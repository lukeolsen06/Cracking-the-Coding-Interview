# Problem: Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

# Ex: Input: the node c from the linked list a -> b -> c -> d -> e -> f

# Runtime: O(n), Space: O(1).
# Note: The deleteFromMiddle function takes O(1) time, but the overall runtime is O(n) because it iterates through the list to find the node to remove.
# If we don't need to implemenent the actual list building and can assume the node passed in is valid, we can remove the need to iterate through the list and the runtime will be O(1).

from linked_list import LinkedList, Node, print_linked_list

def deleteNodeFromMiddle(node):
    if (node == None or node.next == None):
        return
    next = node.next
    node.val = next.val
    node.next = next.next
    return


# Create a mock linked list
list = LinkedList()
chars = "abcdef"
for char in chars:
    list.append(char)

# Define the node to be removed. This can be changed.
toRemove = 'c'

# Gather the actual node to remove by iterating therough the list
curr = list.head
while (curr.next != None):
    if curr.val == toRemove:
        nodeToRemove = curr
        break
    curr = curr.next

deleteNodeFromMiddle(nodeToRemove)
print_linked_list(list.head)