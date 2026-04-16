class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in dic:
                return [dic[complement], i+1]
            else:
                dic[num] = i+1
            