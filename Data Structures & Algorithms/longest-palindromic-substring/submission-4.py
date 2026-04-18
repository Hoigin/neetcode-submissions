class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        length = 0
        for i in range(n+1):
            for j in range(n+1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    if len(substring) > length:
                        length = len(substring)
                        longest = substring
        return longest