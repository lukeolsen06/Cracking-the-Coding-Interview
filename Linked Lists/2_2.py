
# Question 2.2: Implement an algorithm to find the k_th last element of a singly linked list

# O(n) time and O(1) space

from linked_list import LinkedList

def kth_element(head, k):
    if (head == None):
        return head
    s = 1
    current = head
    while (current.next):
        current = current.next 
        s += 1
    index = s - k
    newCurrent = head
    j = 0
    while (j < index):
        newCurrent = newCurrent.next
        j += 1
    return newCurrent.val


list = LinkedList()
chars = "Two roads diverged in a yellow wood"
for char in chars:
    list.append(char)
print(f"d should be the output: {kth_element(list.head, 18)}") # d
print(f"The 2nd to last element is: {kth_element(list.head, 2)}") # o
print(f"The first letter in this sentence is: {kth_element(list.head, 35)}") # T

