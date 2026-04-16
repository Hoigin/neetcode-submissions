class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if j != i:
                    result[i] *= num2
        return result