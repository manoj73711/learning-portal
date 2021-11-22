class solution:

    #tc: o(n), sc: 0(1)
    def palindromCheck(self, str):

        start = 0
        end = len(str)-1

        while start < end:
            if str[start] != str[end]:
                return False
        return True