class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        s = str(A)
        result = '-{}'.format(str(int(s[1:][::-1]))) if s[0] == '-' else str(int(s[::-1]))
        return 0 if len(bin(int(result))[2:]) > 32 else result
