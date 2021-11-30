class solution:

    #TC: 0((n-m+1)*m)
    def patternSearchingNaive(self, str, pattern):

        result = []
        n = len(str)
        m = len(pattern)
        for i in range(n-m):

            j = 0
            for j in range(m):
                if pattern[j]!=str[i]:
                    break
            if j == len(pattern):
                result.append(i)
        return result

    #This is better naive for distinct elements
    # TC: Theta(n)
    def patternSearchingBetterNaive(self, str, pattern):

        result = []
        n = len(str)
        m = len(pattern)
        i = 0
        while i < n-m:
            j = 0
            while j < m:
                if pattern[j] != str[i]:
                    break
                j +=1
            if j == len(pattern):
                result.append(i)
            if j == 0:
                i +=1
            else:
                 i = i + j

        return result