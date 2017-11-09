# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list

    def detectCycle(self, A):
        visited = set()
        traverse = A
        while traverse is not None:
            if traverse.val in visited:
                return traverse
            visited.add(traverse.val)
            traverse = traverse.next
        return None
