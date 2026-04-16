class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comset = []
        def dfs(i, total):
            if i >= len(nums):
                return
            if total == target:
                res.append(comset.copy())
            for j in range(i, len(nums)):
                if total > target:
                    break
                comset.append(nums[j])
                dfs(j, total+nums[j])
                comset.pop()
        dfs(0, 0)
        return res