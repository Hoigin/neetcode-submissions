class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = [char.lower() for char in s if char.isalpha()==True or char.isdigit()==True]
        result = (cleaned_s[::-1]==cleaned_s)
        return result