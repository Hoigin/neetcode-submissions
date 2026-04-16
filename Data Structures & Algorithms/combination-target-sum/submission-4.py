class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)
        def backtracking(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            for i in range(start, length):
                new_total = total + nums[i]
                if new_total > target:
                    return
                path.append(nums[i])
                backtracking(i, path, new_total)
                path.pop()
        backtracking(0, [], 0)
        return res
