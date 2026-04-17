class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        length = len(s)
        def dfs(par, start):
            if start == length:
                res.append(par[:])
            for j in range(start + 1, length + 1):
                substring = s[start:j]
                if substring == substring[::-1]:
                    par.append(substring)
                    dfs(par, j)
                    par.pop()
        dfs([], 0)
        return res
            