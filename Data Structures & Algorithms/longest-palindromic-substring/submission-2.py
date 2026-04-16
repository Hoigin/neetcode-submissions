class Solution:
    def longestPalindrome(self, s: str) -> str:
        pt = 0
        res = s[0]
        n = len(s)
        for i in range(2, n+1):
            j = 0
            # print(j+i)
            while j+i <= n:
                subs = s[j:j+i]
                if subs == subs[::-1]:
                    res = subs
                j += 1
        return res