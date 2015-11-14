# import requests
# url = 'http://search.twitter.com/search.json?q=usa'
# results = requests.get(url)
# better_results = results.json()
# print(len(better_results))
# #print(better_results['results'][0]['text'].encode('utf-8'))


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time
import json



#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
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
        
        c.execute("INSERT INTO Jeb_Bush (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()

        print((username,tweet))
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Jeb Bush"])
