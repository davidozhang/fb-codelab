class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        l = len(A)
        if l == 1:
            return A
        s = sorted(A)
        prev = None
        output = []
        for i, num in enumerate(s):
            if i % 2 == 1:
                output.append(num)
                output.append(prev)
                prev = None
            else:
                prev = num
        if prev:
            output.append(prev)
        return output
