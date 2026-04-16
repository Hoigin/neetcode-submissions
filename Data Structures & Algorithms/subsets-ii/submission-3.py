class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        def backtrack(start, subset):
            result.append(subset)
            for i in range(start, n):
                if i > start and nums[i]==nums[i-1]:
                    continue
                backtrack(i+1, subset+[nums[i]])
        backtrack(0, [])
        return result  