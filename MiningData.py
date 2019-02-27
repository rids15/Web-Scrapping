import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = "bBEdjfR6AcAYZbXDes3jMFMVS"
consumer_secret = "Lv12pEIU4fQDXJdNVFAdaz5gdEdAjwQXjCWM2qm7VsPLxTDyWl"

access_key = "2270562236-lCYFqY2TYe6fs1rgyCOFpLqwU6xco9kmi2BCHt8"
access_token = "jF4egKg0HLyEHwcjwzUFepTDLZMteDpn6kax29esLtGSF"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_token)

api = tweepy.API(auth)


class MyListner(StreamListener):
    def on_data(self, data):
        try:
            with open("python.json", "a") as f:
                f.write(data)
                return True
        except BaseException as e:
            print(str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListner())
twitter_stream.filter(track=["#football"])

# Get data from user timeline
# for status in tweepy.Cursor(api.home_timeline).items(5):
#     print(status.text)
#     print(status._json)
#     print("\n")

# Get data of friends
# for friend in tweepy.Cursor(api.friends).items():
#     print(friend._json)

# Get data of user tweets
# for tweet in tweepy.Cursor(api.user_timeline).items():
#     print(tweet._json)

