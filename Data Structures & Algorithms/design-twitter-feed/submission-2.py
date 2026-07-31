class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetmap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.count, tweetId))
        self.count+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweetmap[userId][:]
        for followeeId in self.followMap[userId]:
            feed.extend(self.tweetmap[followeeId])
        
        feed.sort(key = lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
