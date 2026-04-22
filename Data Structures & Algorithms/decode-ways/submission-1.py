class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        memo = {}

        def backtrack(ptr):
            if ptr == n:
                return 1
            if s[ptr] == '0':
                return 0
            if ptr in memo:
                return memo[ptr]
            res = backtrack(ptr+1)
            if ptr < n-1 and int(s[ptr:ptr+2]) <= 26:
                res += backtrack(ptr+2)
            memo[ptr] = res
            return res
        
        return backtrack(0)