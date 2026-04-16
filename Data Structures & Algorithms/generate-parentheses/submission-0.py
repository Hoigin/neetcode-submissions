class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, open_num, close_num):
            if open_num == close_num == n:
                res.append("".join(curr))
                return
            if open_num < n:
                curr.append("(")
                backtrack(curr, open_num+1, close_num)
                curr.pop()
            if close_num < open_num:
                curr.append(")")
                backtrack(curr, open_num, close_num+1)
                curr.pop()
        backtrack([], 0, 0)
        return res