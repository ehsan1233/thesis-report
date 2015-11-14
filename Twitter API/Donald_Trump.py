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

        if not all_data['retweeted'] and 'RT @' not in all_data['text']:
            tweet = all_data["text"].encode('utf-8')
        
            username = all_data["user"]["screen_name"]

            c.execute("INSERT INTO Donald_Trump (time, username, tweet) VALUES (%s,%s,%s)",
            (time.strftime("%H:%M:%S", time.localtime(None)), username, tweet))

            conn.commit()
            print(time,username,tweet)
        
        return True

    def on_error(self, status):
        if status==420:
            print("Disconnected because of excided number of attempts")
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Donald Trump"], languages=["en"], async=True)
