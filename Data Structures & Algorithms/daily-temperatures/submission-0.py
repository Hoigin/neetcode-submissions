class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        n = len(temperatures)
        for i in range(n):
            curr = temperatures[i]
            count = 0
            for j in range(i, n):
                if temperatures[j] > curr:
                    count = j - i
                    break
            days.append(count)
        return days

