class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        n = len(sorted_nums)
        for i in range(n):
            search_set = {}
            for j in range(i+1,n):
                complement = -sorted_nums[i]-sorted_nums[j]
                if complement in search_set:
                    result.append([sorted_nums[i], complement, sorted_nums[j]])
                else:
                    search_set[sorted_nums[j]] = j
        return list(set(tuple(row) for row in result))