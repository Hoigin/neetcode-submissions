class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for end in range(n):
            for start in range(end, -1, -1):
                if s[start] == s[end] and (end-start<=1 or dp[start+1][end-1]):
                    dp[start][end] = True
                    res += 1
        return res