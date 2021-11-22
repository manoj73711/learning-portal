class solution:

    #This is efficient solution 1, tc o(n), sc 0(1)
    def leftMostRepeatingCharacter1(self, string):

        noOfChars = 256
        firstIndex = [-1]*noOfChars

        res = float('inf')

        for i in range(len(string)):

            if firstIndex[ord(string[i])] == -1:
                firstIndex[ord(string[i])] = i
            else:
                res = min(res, firstIndex[ord(string[i])])
        if res == float('inf'):
            return -1
        else:
            return res

    #This is more efficient solution
    def leftMostRepeatingChars(self, str):

        noOfChars = 256
        visited = [False]*noOfChars
        res = -1
        for i in range(len(str)-1, -1, -1):
            if visited[str.index(str[i])] == False:
                visited[str.index(str[i])] == True
            else:
                res = i
        return res



