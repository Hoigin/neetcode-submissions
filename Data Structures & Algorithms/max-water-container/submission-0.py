class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        volumes = []
        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            volumes.append(volume)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max(volumes)