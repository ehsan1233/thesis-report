from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time
import json

conn = MySQLdb.connect("localhost","root","root","dumps_tweets" )

c = conn.cursor()

#consumer key, consumer secret, access token, access secret.
ckey = "WGLnKpYsK3hhOYSupYiLVSui5"
csecret = "75NhnD0B2rLP7QKj3bV2Q6ljrn2xtRU3Fjyp5ap2JhfZNScFTH"
atoken = "3686382076-Ycyc5oDfyFpUtEV46TcP1faWc3JHaXa1OBF9APs"
asecret = "RgeZbdVff3uv8RXBaNzpFLA9W3x2j4o2g81L6DcZJINYC"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"].encode('utf-8')
        
        username = all_data["user"]["screen_name"]
        
        c.execute("INSERT INTO user (time, username, tweet) VALUES (%s,%s,%s)",
            (time.strftime("%H:%M:%S", time.localtime(None)), username, tweet))

        conn.commit()

        print((username,tweet))
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(follow="moudiol")
