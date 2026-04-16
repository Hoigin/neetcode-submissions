class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, state):
            if state == 2*n:
                res.append(path)
                return
            for choice in ['(', ')']:
                new_path = path + choice
                count = Counter(list(new_path))
                if count[')'] > count['('] or count['('] > n:
                    continue
                new_state = state + 1
                backtrack(new_path, new_state)
        backtrack("", 0)
        return res