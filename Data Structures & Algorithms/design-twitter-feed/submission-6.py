class Twitter:

    def __init__(self):
        self.tweetMap = {}
        self.followMap = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
            self.followMap[userId] = set()
            self.followMap[userId].add(userId)
        self.tweetMap[userId].append( (self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        result = []
        self.followMap[userId].add(userId)
        followees = self.followMap[userId]
        for followee in followees:
            if followee in self.tweetMap:
                tweets = self.tweetMap[followee]
                index = len(self.tweetMap[followee]) - 1
                timestamp, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minHeap, [timestamp, tweetId, followee, index])
        while minHeap and len(result) < 10:
            timestamp, tweetId, followee, index = heapq.heappop(minHeap)
            result.append(tweetId)
            if index > 0:
                next_timestamp, next_tweetId = self.tweetMap[followee][index-1]
                heapq.heappush(minHeap, [next_timestamp, next_tweetId, followee, index-1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
            self.followMap[followerId].add(followerId)
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
