class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_list = {}
        for index, num in enumerate(nums):
            counter = target - num
            if counter in hash_list:
                return [hash_list[counter], index]
            else:
                hash_list[num] = index