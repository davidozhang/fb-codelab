class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        s = set()
        l = len(A)
        a = None

        for num in A:
            if num not in s:
                s.add(num)
            else:
                a = num

        expected_sum = (1 + l) * l / 2
        actual_sum = sum(s)
        b = expected_sum - actual_sum
        return [a, b]
