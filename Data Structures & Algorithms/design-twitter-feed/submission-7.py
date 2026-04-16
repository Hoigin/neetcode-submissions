class Twitter:

    def __init__(self):
        # 使用 defaultdict 减少 if 判断
        self.tweetMap = {} 
        self.followMap = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
            self.followMap[userId] = {userId} # 使用集合字面量更快
        
        self.tweetMap[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # 1. 局部变量优化：把字典赋值给局部变量，访问速度更快
        tweet_map = self.tweetMap
        follow_map = self.followMap
        
        if userId not in follow_map:
            return []
            
        minHeap = []
        result = []
        
        # 2. 减少属性访问：直接操作集合
        followees = follow_map[userId]
        followees.add(userId) # 确保关注自己
        
        # 3. 初始化堆
        for followee in followees:
            if followee in tweet_map:
                tweets = tweet_map[followee]
                # 获取最后一条
                idx = len(tweets) - 1
                ts, tid = tweets[idx]
                heapq.heappush(minHeap, [ts, tid, followee, idx])
        
        # 4. 归并
        while minHeap and len(result) < 10:
            ts, tid, user, idx = heapq.heappop(minHeap)
            result.append(tid)
            
            if idx > 0:
                # 减少字典查找次数
                next_tweets = tweet_map[user]
                next_ts, next_tid = next_tweets[idx - 1]
                heapq.heappush(minHeap, [next_ts, next_tid, user, idx - 1])
                
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = {followerId}
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # discard 比 remove 安全且不需要 if 判断
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
