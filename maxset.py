class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        subarrays = []
        result = None
        max_sum = -float('inf')
        max_len = -float('inf')
        head = None
        for i in xrange(len(A)):
            if A[i] < 0 and head is not None:
                subarrays.append(A[head:i])
                head = None
            elif A[i] >= 0 and head is None:
                head = i
        if head is not None:
            subarrays.append(A[head:len(A)-1])
        for array in subarrays:
            s = sum(array)
            l = len(array)
            if s >= max_sum and l > max_len:
                max_sum = s
                max_len = l
                result = array
        return result
