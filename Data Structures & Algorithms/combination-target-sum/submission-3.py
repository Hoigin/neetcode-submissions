class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comset = []
        nums.sort()
        n = len(nums)
        def dfs(i, total):
            for j in range(i, n):
                num = nums[j]
                new_total = total + num
                if new_total > target:
                    break
                if new_total == target:
                    comset.append(num)
                    res.append(comset.copy())
                    comset.pop()
                else:
                    comset.append(num)
                    dfs(j, new_total)
                    comset.pop()
        dfs(0, 0)
        return res