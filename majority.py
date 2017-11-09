class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        majority = None
        counter = 0
        for item in A:
            if not majority or item == majority:
                majority = item
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                majority = None
        return majority
