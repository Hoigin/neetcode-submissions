class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        reverse = digits[::-1]
        carry = 1
        for i in range(n):
            if reverse[i] != 9:
                reverse[i] += carry
                break
            else:
                reverse[i] = 0
                if i == n-1:
                    reverse.append(1)
        return reverse[::-1]
