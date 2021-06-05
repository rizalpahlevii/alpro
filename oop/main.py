class Twitter:
    def __init__(self, name, username, follower, following):
        self.name = name
        self.username = username
        self.follower = follower
        self.following = following

    def showInfo(self):
        print(
            f'\n Nama : {self.name} \n Username : {self.username} \n Following : {self.following} \n Follower : {self.follower}'
        )

    def tweet(self, content):
        self.content = content
        print(f"\n Berhasil Melakukan Tweet dengan isi :  {self.content}")

    def replyTweet(self, parentTweet, content):
        self.content = content
        self.parentTweet = parentTweet
        print(
            f'\n Balasan Tweet Pada Tweet : {self.parentTweet} dengan isi : {self.content}')

    def retweet(self, tweet):
        self.tweet = tweet
        print(f"\n Berhasil Melakukan Retweet Pada Tweet {self.tweet}")

    def likeTweet(self, tweet):
        self.tweet = tweet
        print(f"\n Berhasil Melakukan Like Pada Tweet {self.tweet}")

    def follow(self, user):
        self.user = user
        print(f"\n Berhasil Melakukan Follow Pada User :  {self.user}")


myTwitter = Twitter("Muhammad Rizal Pahlevi", "@rizalpahlevi", 1000, 1000)

myTwitter.showInfo()
myTwitter.tweet(
    "Whatever we plant in our subconscious mind and nourish with repetition and emotion will one day become a reality.")

myTwitter.replyTweet("All About Udinus", "Bagus Sekali Yaaaaa")

myTwitter.retweet("Informasi Tentang Udinus")

myTwitter.likeTweet("Informasi Tentang Udinus")

myTwitter.follow("@dinussmg")
