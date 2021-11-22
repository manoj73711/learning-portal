class solution:
    #TC: o(n), sc: 0(n)
    def trappingRainWater(self, arr, n):
        lmax = [0]*n
        rmax = [0]*n
        area = 0
        lmax[0] = arr[0]

        for i in range(1,n):
            lmax[i] = max(arr[i], lmax[i-1])
        rmax[0] = arr[n-1]

        for i in range(n-2, -1, -1):
            rmax = max(arr[i], rmax[i+1])

        for i in range(1, n-1):
            area += min(lmax[i], rmax[i]) - arr[i]

        return area



