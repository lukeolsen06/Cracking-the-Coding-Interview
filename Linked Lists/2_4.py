# Problem: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. 
# (IMPORTANT: The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions. The additional spacing in the example below is to indicate the partition. The output is one of many valid outputs.)

# Ex: Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 ->        10  -> 5 -> 5 -> 8

# Time Complexity: O(n), Space Complexity: O(1)

from linked_list import LinkedList, Node, print_linked_list

def partition(head, x):
    curr = head
    if (curr == None or curr.next == None):
        return
    while (curr.next != None):
        if (curr.next.val < x):
            temp1 = head.next # The second node in the list
            head.next = curr.next # The second node in the list becomes the  node we want to move to the front
            temp2 = curr.next.next # Save the node that the current node will eventually point to after shifting
            curr.next.next = temp1 # The node that we are shifting will now point to the current head's "next" node, effectively shifting it by 1
            curr.next = temp2 # Set the current node's next point to the node after the one we are shifting
        else:
            curr = curr.next 
    print_linked_list(head)
    if (head.val >= x): # This is the case where the the first element of the list is greater than the partition value
        temporary1 = head
        head = head.next
        curr = head
        while (curr.val < x):
            curr = curr.next
        temporary2 = curr.next
        curr.next = temporary1
        temporary1.next = temporary2
    return head



list = LinkedList()
nums = [4, 5, 8, 5, 10, 2, 1]
for num in nums:
    list.append(num)

list.head = partition(list.head, 5)
print_linked_list(list.head)