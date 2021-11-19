class solution:

    #segregate positive and negative integers
    #Segregate even and odd elements
    #segrefate 0s and 1s
    #tc : 0(N), SC = 0(1)
    #This solution is based on hoare partition
    def segPosNeg(self, arr, n):

        i = -1
        j = n

        while True:
            i+=1
            while arr[i]<0:
                i +=1
            j -=1
            while arr[j]>=0:
                j -=1
            if i >=j:
                return arr
            arr[i], arr[j] = arr[j], arr[i]

        return arr

