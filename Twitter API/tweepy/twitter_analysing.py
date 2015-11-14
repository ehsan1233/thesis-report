import json
import pandas as pd
import matplotlib.pyplot as plt
import re


def main():


	#Reading Tweets
	print 'Reading Tweets\n'
	tweets_data_path = 'example.txt'

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        tweets_text = tweet["text"]
	        print tweets_text + "\n" 

	    except:
	        continue


if __name__=='__main__':
	main()

