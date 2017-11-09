class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        count = 0
        off = 0
        for bulb in A:
            if bulb == off:
                count += 1
                off = off ^ 1
        return count
