
# Question 2.1: Write code to remove duplicates from an unsorted linked list.
# EX: FOLLOW UP

from linked_list import LinkedList, print_linked_list

# Function to remove duplicates from the linked list
def removeDuplicates(head):
    seen = set()
    current = head
    seen.add(current.val)
    while (current.next):
        if (current.next.val in seen):
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next
    return head


# Mock linked list for FOLLOW UP example
# Creates: F -> O -> L -> L -> O -> W -> ' ' -> U -> P -> None
# After removing duplicates: F -> O -> L -> W -> ' ' -> U -> P -> None

# Create the linked list from "FOLLOW UP"
list = LinkedList()
chars = "FOLLOW UP"
for char in chars:
    list.append(char)

print("Original linked list:")
print_linked_list(list.head)
print("\nAfter removeDuplicates:")
removeDuplicates(list.head)
print_linked_list(list.head)

