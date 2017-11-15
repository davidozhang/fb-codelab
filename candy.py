class Solution:
    # @param ratings : list of integers
    # @return an integer
    def candy(self, ratings):
        l = len(ratings)
        if l == 1:
            return 1
        result = [1]*l
        for i in xrange(1, l):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1
        for i in reversed(xrange(l-1)):
            if ratings[i] > ratings[i+1]:
                result[i] = max(result[i], result[i+1] + 1)
        return sum(result)
