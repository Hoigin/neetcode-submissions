class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = list(zip(position, speed))
        l.sort(key=lambda x: x[0])
        stack = []
        fleet_num = len(position)
        for pos, s in l:
            time = (target - pos) / s
            while stack and stack[-1] <= time:
                stack.pop()
                fleet_num -= 1
            stack.append(time)
        return fleet_num