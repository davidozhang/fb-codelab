class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        return int(''.join(list(bin(A)[2:].zfill(32))[::-1]), 2)
