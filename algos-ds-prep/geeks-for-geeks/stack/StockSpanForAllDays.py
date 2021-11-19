class Solution:

    # Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self, a, span):

        st = []

        st.append(0)

        for i in range(1, n):

            while st and a[st[-1]] <= a[i]:
                st.pop()

            span[i] = i + 1 if len(st) <= 0 else i - st[-1]

            st.append(i)

