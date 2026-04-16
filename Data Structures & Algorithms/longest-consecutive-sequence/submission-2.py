class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count_list = [0]
        for element in nums:
            count = 0
            length = len(nums)
            for i in range(length+1):
                if (element+i) in nums:
                    count += 1
                else:
                    count_list.append(count)
                    break
        return max(count_list)