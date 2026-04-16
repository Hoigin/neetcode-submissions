class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)
        def backtracking(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            for i in range(start, length):
                path.append(nums[i])
                backtracking(i, path, total+nums[i])
                path.pop()
        backtracking(0, [], 0)
        return res