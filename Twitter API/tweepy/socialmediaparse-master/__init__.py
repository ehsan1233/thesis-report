__author__ = 'seandolinar'

import os
import pandas as pd

from emoji_parse import EmojiDict
from hashtag_parse import HashtagParse
from twitter_parse import TweetAnalysis
import MySQLdb
import mysql.connector
import re

def main():
	cnx = mysql.connector.connect(user='root', password='root', database='tweettable')
	cursor = cnx.cursor(buffered=True)

	query = ("SELECT tweet FROM taula4bitDefault WHERE 1")

	cursor.execute(query)

	numrows = cursor.rowcount
	print "numrows = ", numrows

	smileys = """:-) :) :o) :] :3 :c) :> =] 8) =) :} :^) :D 8-D 8D x-D xD X-D XD =-D =D =-3 =3 B^D""".split()
	pattern = "|".join(map(re.escape, smileys))
	cnt = 0
	#Get and display the rows one at a time
	for i in cursor:
		text = str(i)
		if (re.findall(pattern, text)):
			cnt +=1
	print "Number of tweets with smilies =", cnt
	cursor.close()
	cnx.close()

main()


