class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        steps = 0
        for i in range(0,len(X)-1):
            steps += max(abs(X[i+1]-X[i]), abs(Y[i+1]-Y[i]))
        return steps
