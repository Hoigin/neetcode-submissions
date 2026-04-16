class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l < r:
            # l < m < r -> between l and m
            # m < r < l -> between l and m
            # r < l < m -> between m and r
            mid = (l + r) // 2
            if l==mid:
                break
            elif nums[r] < nums[l] < nums[mid]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])