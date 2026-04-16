class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        def per(i, nums):
            if i == length:
                return [[]]
            res = []
            perms = per(i+1, nums)
            for p in perms:
                for j in range(len(p)+1):
                    copy = p.copy()
                    copy.insert(j, nums[i])
                    res.append(copy)
            return res
        return per(0, nums)