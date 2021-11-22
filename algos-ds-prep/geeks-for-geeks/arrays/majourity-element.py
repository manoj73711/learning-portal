class solution:

    def majourityElement(self, arr, n):

        res = 0
        count =1
        #Find the majourity element first
        for i in range(1, n):

            if arr[i] == arr[res]:
                count +=1
            else:
                count -=1

            if count  == 0:
                res = i
                count =1
        #Now check if this is the majourity element

        count = 0

        for i in range(n):
            if arr[i] == arr[res]:
                count +=1

        if count >= n//2:
            res = -1

        return res
