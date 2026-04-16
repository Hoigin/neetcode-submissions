class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_list = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hash_list:
                return [hash_list[complement], index]
            else:
                hash_list[num] = index