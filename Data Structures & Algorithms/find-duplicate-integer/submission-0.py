class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        result = [value for value, freq in c.most_common(1)]
        return result[0]