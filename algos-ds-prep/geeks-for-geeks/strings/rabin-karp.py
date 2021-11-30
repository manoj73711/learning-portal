class solution:


    def rabinKarp(self, pat, str, m, n):

        result = []
        #assume d = 5
        d = 256
        q = 101
        #step 1: compute d**m-1
        h =1

        for i in range(m):
            h = (h * d)%q

        # step 2: compute p and t
        p = 0
        t = 0
        for i in range(m):
            p = (p*d + pat[i])%q
            t = (t*d + str[i])%q

        for i in range(n-m+1):
            #Check for hit

            if p == t:
                flag = True
                for j in range(m):
                    if str[i+j]!=pat[j]:
                        flag = False
                        break
                if flag:
                    result.append(i)

                if i < n-m:
                    t = ((d*(t - str[i]*h))+str[i+m])%q
                if t <0:
                    t = t + q
        return result




