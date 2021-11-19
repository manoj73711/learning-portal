class solution:

    def meetingMaxGuests(self, arrival, departures, n):

        arrival.sort()
        departures.sort()
        i,j = 1,0
        curr, res  = 1

        while i<n and j< n:
            if arrival[i]<departures[j]:
                curr +=1
                i +=1
            else:
                curr -=1
                j +=1
            res = max(res, curr)
        return res


