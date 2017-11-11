class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        freq = {0:0, 1:0, 2:0}
        for i in A:
            freq[i] += 1
        return [0]*freq[0] + [1]*freq[1] + [2]*freq[2]
        
