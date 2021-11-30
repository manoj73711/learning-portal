class solution:

    def leftMostNonRepeatingCharacter1(self, str):

        no_of_chars = 256;
        charCount = [0]*no_of_chars

        for i in range(len(str)):
            charCount[ord(str[i])] +=1

        for i in range(len(str)):

            if charCount[ord(str[i])] == 1:
                return i
        return -1

