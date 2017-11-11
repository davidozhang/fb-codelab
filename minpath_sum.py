class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        m = len(A)
        n = len(A[0])
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j > 0:
                    A[i][j] += A[i][j-1]
                elif i > 0 and j == 0:
                    A[i][j] += A[i-1][j]
                elif i > 0 and j > 0:
                    A[i][j] += min(A[i-1][j], A[i][j-1])
        return A[m-1][n-1]
