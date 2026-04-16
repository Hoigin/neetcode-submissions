class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minus_stones = [-stone for stone in stones]
        heapq.heapify(minus_stones)
        while len(minus_stones) > 1:
            one = -heapq.heappop(minus_stones)
            two = -heapq.heappop(minus_stones)
            if one == two:
                continue
            elif one > two:
                heapq.heappush(minus_stones, -(one-two))
        return -minus_stones[0] if len(minus_stones)==1 else 0