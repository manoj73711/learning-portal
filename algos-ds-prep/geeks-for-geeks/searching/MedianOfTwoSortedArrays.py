#This is easy but challenging. Needs strong revision

class MedianOfTwoSortedArrays:

    def medianOfTwoSortedArrays(self, a1, a2, n1, n2):

        begin1, end1 = 0, n1

        while begin1 < end1:
            i1 = begin1 + end1 //2
            i2 = (n1 +n2 + 1) //2 -i1

            min1 = float('inf') if i1 == n1 else a1[i1]
            max1 = float('-inf') if i1 == 0 else a1[i1-1]

            min2 = float('inf') if i2 == n2 else a2[i2]
            max2 = float('-inf') if i2 == 0 else a2[i2 - 1]

            if max1 <= min2 and max2 <= min1:

                if (n1 + n2) % 2 ==0:
                    return max(max1, max2)+min(min1, min2) /2
                else:
                    return max(max1, max2)

            elif max1 > min2:
                end1 = i1-1
            else:
                end1 = i1+1

        return -1
