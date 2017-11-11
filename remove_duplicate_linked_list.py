# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        traverse = A
        while traverse and traverse.next:
            _next = traverse.next
            while _next and _next.val == traverse.val:
                _next = _next.next
            traverse.next = _next
            traverse = traverse.next
        return A
