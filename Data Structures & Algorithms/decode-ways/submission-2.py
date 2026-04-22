class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        pprev = 1
        prev = 1
        for i in range(1, n):
            current = 0
            if s[i] != '0':
                current += prev
            if 10 <= int(s[i-1:i+1]) <= 26:
                current += pprev
            if count == 0:
                return 0
            pprev = prev
            prev = current
        return prev