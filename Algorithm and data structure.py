class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeSort(head):
    if not head or not head.next:
        return head

    # Find the middle of the list
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Split the list into two halves
    mid = slow.next
    slow.next = None

    # Recursively sort the two halves
    left = mergeSort(head)
    right = mergeSort(mid)

    # Merge the sorted halves
    dummy = ListNode()
    curr = dummy
    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next

    # Append any remaining nodes
    curr.next = left or right

    return dummy.next
# Create a linked list from the input list
head = ListNode(11, ListNode(5, ListNode(-1, ListNode(20, ListNode(0, ListNode(2))))))

# Sort the list
head = mergeSort(head)

# Print the sorted list
while head:
    print(head.val, end=' ')
    head = head.next





