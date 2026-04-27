from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set(wordDict)
        n = len(s)
        @cache
        def backtrack(start):
            if start == n:
                return True
            for i in range(start, n):
                if s[start:i+1] in dic:
                    if backtrack(i+1):
                        return True
            return False
        return backtrack(0)