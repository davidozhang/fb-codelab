class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        chars = map(ord, A)
        l = len(chars)
        return sum([(chars[i]-64)*26**(l-1-i) for i in xrange(l)])
