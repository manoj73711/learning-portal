#Min cuts required to make all substrings in a string are palindrome
class Solution:
    def palindromicPartition(self, string):
        return ppHelper(string, 0, len(string) - 1)
        # code here
def isPalindrome(x):
    return x == x[::-1]


def ppHelper(string, i, j):
    if i >= j or isPalindrome(string[i:j + 1]):
        return 0

    res = float('inf')
    for k in range(i, j):
        res = min(res, 1 + ppHelper(string, i, k) + ppHelper(string, k + 1, j))

    return res
