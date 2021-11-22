class solution:

    #TC: Theta(n), SC: o(d)
    def leadersInAnArray(self, arr, n):

        currentLeader = arr[n-1]
        leaders = []
        for i in range(n-2, -1, -1):

            if currentLeader < arr[i]:
                leaders.append(arr[i])
                currentLeader = arr[i]
        reversed(leaders)
        return leaders
