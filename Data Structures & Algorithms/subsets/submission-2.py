class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()
        n = len(nums)
        def backtrack(start):
            result.append(subset[:])
            for i in range(start, n):
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
        backtrack(0)
        return result