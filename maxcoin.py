class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0]
        return max(
            A[0] + min(self.maxcoin(A[2:]), self.maxcoin(A[1:-1])),
            A[-1] + min(self.maxcoin(A[:-2]), self.maxcoin(A[1:-1])))
