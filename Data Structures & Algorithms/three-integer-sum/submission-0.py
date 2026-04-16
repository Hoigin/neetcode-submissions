class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = [[nums[i], nums[j], nums[k]]
                    for i in range(n)
                    for j in range(i+1,n)
                    for k in range(j+1,n)
                    if nums[i]+nums[j]+nums[k]==0]
        result = list(set(tuple(sorted(row)) for row in result))
        return result