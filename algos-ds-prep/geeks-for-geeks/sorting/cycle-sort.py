class solution:

    #Average, best and worst case : 0(n2), Sc = 0(1)
    def cycleSort(self, arr, n):

        writes = 0
        for cs in range(n):
            item = arr[cs]
            pos = cs
            #Find out how many elements are smaller
            for i in range(cs+1, n):
                if arr[i] < item:
                    pos +=1
            #Skip is this is already in correct position
            if pos == cs:
                continue
            #Check if there are any duplicates
            while arr[pos] == item:
                pos +=1

            #found the position, swap it
            arr[pos], item = item, arr[pos]
            writes +=1

            while pos!=cs:
                pos = cs
                for i in range(cs+1, n):
                    if arr[i]<item:
                        pos +=1
                #Put the item in the right position
                while item == arr[pos]:
                    pos +=1
                arr[pos], item = item, arr[pos]
                writes +=1

        return writes

