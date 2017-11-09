class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        root = {}
        output = []
        for word in A:
            current = root
            for c in word:
                if c not in current:
                    current[c] = {'count': 0}
                current[c]['count'] += 1
                current = current[c]
        for word in A:
            current = root
            for i, c in enumerate(word):
                current = current[c]
                if current['count'] == 1:
                    output.append(word[:i+1])
                    break
        return output
