class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        result = ['' for _ in xrange(B)]
        counter = 0
        increment = True
        for c in list(A):
            result[counter] += c
            if increment and counter == B - 1:
                increment = False
            elif not increment and counter == 0:
                increment = True
            if increment and counter < B - 1:
                counter += 1
            elif not increment and counter > 0:
                counter -= 1
        return ''.join(result)
