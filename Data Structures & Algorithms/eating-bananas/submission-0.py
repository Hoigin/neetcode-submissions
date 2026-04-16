class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            rate = (l + r) // 2
            time = sum([math.ceil(pile / rate) for pile in piles])
            if time > h:
                l = rate + 1
            else:
                r = rate
        return l