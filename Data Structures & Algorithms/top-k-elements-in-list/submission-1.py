class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return [value for value, freq in sorted_items[:k]]