# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if m == n:
            return A

        dummyNode = ListNode(0)
        dummyNode.next = A
        prev = dummyNode

        for _ in xrange(m-1):
            prev = prev.next

        reversal_prev = None
        traverse = prev.next
        # one past the end
        for i in range(n-m+1):
            next = traverse.next
            traverse.next = reversal_prev
            reversal_prev = traverse
            traverse = next

        prev.next.next = traverse
        prev.next = reversal_prev

        return dummyNode.next
