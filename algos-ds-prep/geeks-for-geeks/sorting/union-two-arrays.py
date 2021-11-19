class solution:

    def doUnion(self, a, n, b, m):

        result = []
        i, j = 0, 0
        while i < n and j < m:

            if i > 0 and a[i - 1] == a[i]:
                i += 1
                continue
            if j > 0 and b[j - 1] == b[j]:
                j += 1
                continue

            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                result.append(b[j])
                j += 1
            else:
                result.append(a[i])
                i += 1
                j += 1
        while i < n:
            if i == 0 or a[i] != a[i - 1]:
                result.append(a[i])
            i += 1
        while j < m:
            if j == 0 or b[j] != b[j - 1]:
                result.append(b[j])
            j += 1

        return result

