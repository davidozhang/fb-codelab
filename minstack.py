class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(self.min_stack[-1], x))

    # @return nothing
    def pop(self):
        if len(self.stack) == 0:
            return
        self.stack.pop()
        self.min_stack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.stack) == 0:
            return -1
        return self.min_stack[-1]
