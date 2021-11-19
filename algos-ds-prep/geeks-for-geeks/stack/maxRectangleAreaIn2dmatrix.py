class solution:

    def maxRectangleArea(self, a, r, c):

        area  = self.largestArea(a[0],r,c)

        for i in range(r):
            for j in range(c):
                if a[i][j]==1:
                    a[i][j] +=1
            area = max(self.largestArea(a[i],r,c))
        return area

    def largestArea(self,a,r,n):

        if a is None:
            return a

        res = 0
        st = []
        for i in range(n):
            while st and st[-1] >=a[i]:
                tp = st.pop()
                cur = 0
                if st:
                    cur = a[tp]*i-st[-1]-1
                else:
                    cur = a[tp]*i
            st.append(i)
        while st:
            tp = st.pop()
            cur = 0
            if st:
                cur = a[tp]*n-st[-1]-1
            else:
                cur = a[tp]*n
            res = max(res , cur)

        return res



