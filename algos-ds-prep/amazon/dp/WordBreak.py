class Solution:

    #Naive Aproach TC = 2^n and sc = o(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def wordBreakRecur(s: str, word_dict: Set[str], start: int):

            # write base case here
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and wordBreakRecur(s, word_dict, end):
                    return True

            return False

        return wordBreakRecur(s, set(wordDict), 0

        # Dp Approach TC = O(n^3) sc = o(n)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]
