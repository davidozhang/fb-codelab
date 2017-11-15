class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        l = len(A) - 1
        carry = 0
        plus_value = 1
        while l >= 0:
            if A[l] + plus_value + carry >= 10:
                A[l] = 0
                carry = 1
            else:
                A[l] += plus_value + carry
                carry = 0
            plus_value = 0
            l -= 1
        if carry == 1:
            A.insert(0, 1)
        first_pos_index = 0
        while first_pos_index < len(A) and A[first_pos_index] == 0:
            first_pos_index += 1
        return A[first_pos_index:]
