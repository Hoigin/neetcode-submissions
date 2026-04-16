class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comset = []
        def dfs(i):
            if i >= len(nums):
                return
            if sum(comset) == target:
                res.append(comset.copy())
            for j in range(i, len(nums)):
                if sum(comset) > target:
                    break
                comset.append(nums[j])
                dfs(j)
                comset.pop()
        dfs(0)
        return res