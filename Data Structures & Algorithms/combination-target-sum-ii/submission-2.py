class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        length = len(candidates)
        candidates.sort()
        def backtracking(start, path, total):
            if total == target:
                result.append(path.copy())
                return
            for i in range(start, length):
                # 同一层调用同一个数字可以跳过，不同层调用同一个数字则可以接受
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                new_total = total + candidates[i]
                if new_total > target:
                    return
                path.append(candidates[i])
                backtracking(i+1, path, new_total)
                path.pop()
        backtracking(0, [], 0)
        return result