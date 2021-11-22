class solution:

    #Check if a string is subsequence.
    #Solution1: iterative
    def checkIfStringIsSubsequence(self, str1, str2):

        m = len(str1)
        n = len(str2)
        j = 0
        for i in range(m):
            if str1[i] == str2[j]:
                j +=1
        return j == n-1

    #This is iterative solution
    def checkIfStringIsSubsequence(self, s1, s2, m, n):

        if n == 0:
            return True
        if m ==0:
            return False
        if s1[m-1] == s2[n-1]:
            return self.checkIfStringIsSubsequence(s1, s2, m-1, n-1)
        else:
            return self.checkIfStringIsSubsequence(s1, s2, m-1, n)






