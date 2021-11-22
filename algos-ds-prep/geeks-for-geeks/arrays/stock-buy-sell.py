class solution:

    #This is peaks and valleys pattern, one of my fav solution
    #Tc: o(n)
    def stockBuySell(self, arr, n):

        profit = 0
        for i in range(1, n):

            if arr[i] > arr[i-1]:
                profit += arr[i]-arr[i-1]

        return profit
