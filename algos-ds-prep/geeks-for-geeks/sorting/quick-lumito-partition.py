class solution:

    #TC: theta(n), sc: theta(1)
    def lumitoPartition(self, a, l, h):

        #Consider the last element as greater element always
        pivot = a[h]
        i = -l
        for j in range(l, h):
            if a[j] < pivot:
                i +=1
                #do swapping
                a[j], a[i] = a[i], a[j]
        a[i+1], a[h] = a[h], a[i+1]
        return i+1

