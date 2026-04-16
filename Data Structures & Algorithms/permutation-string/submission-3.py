class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        left = 0
        right = n
        subset = Counter(s1)
        sliding_set = Counter(s2[left:right])
        # iteration -> O(m)
        while True:
            if sliding_set == subset:
                return True
            elif right == len(s2):
                break
            else:
                sliding_set[s2[left]] -= 1
                sliding_set[s2[right]] += 1
                left += 1
                right += 1
        return False