class Solution:
    def search(self, nums: List[int], target: int) -> int:
        indices = [i for i in range(len(nums)) if nums[i]==target]
        return indices[0] if indices else -1