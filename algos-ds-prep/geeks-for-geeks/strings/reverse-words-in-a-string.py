class solution:

    #TC: 0(n), sc: o(1)
    def reversWordsInString(self, str, n):

        first = 0
        for end in range(n):
            if str[end] == " ":
                self.reverseWord(str, first, end)
                start = end+1
        self.reverseWord(str, start, n-1)
        self.reverseWord(str, 0, n-1)

    def reverseWord(self, str, start, end):

        while start <= end:
            str[start], str[end] = str[end], str[start]
            start +=1
            end -=1

