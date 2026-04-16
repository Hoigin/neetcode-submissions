class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
            self.following[userId] = set()
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        Idset = self.following[userId].copy()
        Idset.add(userId)
        Idset = list(Idset)
        for Id in Idset:
            if Id in self.tweets:
                news.extend(self.tweets[Id])
        news.sort(key=lambda x: x[0], reverse=True)
        news = [x[1] for x in news]
        if len(news) > 10:
            news = news[:10]
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
