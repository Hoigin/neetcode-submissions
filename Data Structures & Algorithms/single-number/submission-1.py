class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        if length == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[length-2] != nums[length-1]:
            return nums[length-1]
        for i in range(1, length-1):
            if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                return nums[i]
            