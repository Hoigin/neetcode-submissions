class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            if q and q[0][1]==time:
                res, _ = q.popleft()
                heapq.heappush(maxHeap, res)
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt < 0:
                    q.append([cnt, time+n+1])
        return time