class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        left = 0
        right = n
        subset = Counter(s1)
        while right <= len(s2):
            sliding_set = Counter(s2[left:right])
            if sliding_set == subset:
                return True
            else:
                left += 1
                right += 1
        return False