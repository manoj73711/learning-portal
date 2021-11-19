class solution:

    def longestRectangularArea(self, a, n):

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