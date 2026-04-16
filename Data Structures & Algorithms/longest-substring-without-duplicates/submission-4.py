class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        
        max_length = 0
        l = 0
        r = 1
        subset = {s[l]}
        while r < len(s):
            if s[r] not in subset:
                subset.add(s[r])
                max_length = max(max_length, r-l+1)
                r += 1
            else:
                subset.remove(s[l])
                l += 1
        return max_length