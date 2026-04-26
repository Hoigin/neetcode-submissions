class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = curr_max = curr_min = nums[0]
        n = len(nums)
        for i in range(1, n):
            num = nums[i]
            temp = curr_max
            curr_max = max(num, temp*num, curr_min*num)
            curr_min = min(num, temp*num, curr_min*num)
            res = max(res, curr_max)
        return res

