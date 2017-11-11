class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a = map(int, A.split('.'))
        b = map(int, B.split('.'))
        for (num1, num2) in zip(a, b):
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        l_a = len(a)
        l_b = len(b)
        if l_a == l_b:
            return 0
        elif l_a > l_b:
            return 1 if sum(a[l_b:]) > 0 else 0
        else:
            return -1 if sum(b[l_a:]) > 0 else 0
