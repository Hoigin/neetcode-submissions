class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        par = []
        length = len(s)
        dp=[[False]*(length) for i in range(length)]      
        for end in range(length):
            for start in range(end, -1, -1):
                if s[start] == s[end] and (end-start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True
        def dfs(i):
            if i == length:
                res.append(par[:])
                return 
            for j in range(i, length):
                if dp[i][j]:
                    par.append(s[i:j+1])
                    dfs(j + 1)
                    par.pop()
        dfs(0)
        return res