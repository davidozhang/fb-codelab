class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        profit = 0
        _max = float('-inf')
        for i in reversed(xrange(len(A))):
            _max = max(_max, A[i])
            profit = max(profit, _max-A[i])
        return profit
