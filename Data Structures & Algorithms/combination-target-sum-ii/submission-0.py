class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        com = []
        sum_com = 0
        length = len(candidates)
        candidates.sort()
        def backtracking(start, path, total):
            if total == target:
                result.append(path.copy())
                return
            if total > target:
                return
            for i in range(start, length):
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtracking(i+1, path, total+candidates[i])
                path.pop()
        backtracking(0, [], 0)
        return result