class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        set_nums = set(nums)
        count_list = []
        for element in set_nums:
            if (element-1) not in set_nums:
                count = 1
                current_num = element
                while (current_num+1) in set_nums:
                    current_num += 1
                    count += 1
                count_list.append(count)
        
        return max(count_list)
