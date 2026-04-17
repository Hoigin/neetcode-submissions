class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res = []
        n = len(digits)
        dic = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], 
               '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
               '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        def dfs(rep, i):
            if i == n:
                res.append(rep)
                return
            for letter in dic[digits[i]]:
                dfs(rep + letter, i + 1)
        dfs("", 0)
        return res