
class solution:

    #TC : theta(n), SC: theta(n)

    def naive_partition(self, a, l, h, p):

        temp = [0]*h-l+1
        index = 0
        pivot = a[p]
        for i in range(l, h+1):
            if a[i]<pivot:
                temp[index] = a[i]
                index +=1

        temp[index]=pivot
        index +=1
        for i in range(l,h+1):
            if a[i]>pivot:
                temp[index] = a[i]
                index+=1
        index = 0
        for i in range(l, h+1):
            a[i] = temp[i-l]
            index+=1




