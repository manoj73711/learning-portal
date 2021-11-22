class solution:

    def checkForAnagram(self, s1, s2):
        noOfChars = 256
        if len(s1) != len(s2):
            return False
        result = [0] * noOfChars

        for i in range(len(s1)):
            result[ord(s1[i])] +=1
            result[ord(s2[i])] -= 1

        for i in range(noOfChars+1):
            if result[i]!=0:
                return False

        return True







