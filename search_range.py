class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        left = 0
        right = len(A) - 1
        mid = -1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] == B:
                break
            elif A[mid] > B:
                right = mid - 1
            else:
                left = mid + 1
        if mid == -1 or A[mid] != B:
            return [-1, -1]
        else:
            # TODO: Run separate binary searches for left and right boundaries
            left = mid
            while left > 0 and A[left-1] == B:
                left -= 1
            right = mid
            while right < len(A)-1 and A[right+1] == B:
                right += 1
            return [left, right]
