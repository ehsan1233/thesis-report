
import string, json, pprint
import urllib
from datetime import timedelta
from datetime import date
from time import *
import string, os, sys, subprocess, time
import simplejson as json

from time import time, sleep
startTime = time()

from colorama import init
init() #init colorama (needed on win32, not in *nix)
from colorama import Fore, Back, Style

from scrapemark import scrape

import MySQLdb

pp = pprint.PrettyPrinter(indent=3)

conn = MySQLdb.connect(host='localhost',  user='root', db='dump_facebook', passwd='fsdfsdfsdf') #, passwd='fsdfsdfsdf'
conn.autocommit(True)
cur = conn.cursor()

cur.execute("select ifnull((select ifnull(run_id,0) from searchbank order by run_id desc limit 0,1),0)")
run_id = cur.fetchall()[0][0]+1
print 'BatchRun #' + str(run_id)

newones = 100
keywords = ['metallica','james hetfield', 'lars ulrich', 'kirk hammett', 'rob trujillo', 'jason newsted','cliff burton','garyvee','vaynerchuk','tsoukalos','ancient aliens','bigfoot','vaynermedia']
# put yer keywords here!

for keyword in keywords:

	sleep(1)
	nextpage = 'https://graph.facebook.com/search?q="'+str(keyword)+'"&type=post&limit=100'
	newones = 100

	while newones > 0 and nextpage <> 'NO':
		sleep(1)
		f = urllib.urlopen(nextpage)
		s = f.read()
		f.close()
		ss = json.loads(s)
		#pp.pprint(ss)

		try:
			for num in range(0,len(ss['data'])):
				#print '*************************'
				#for majorkey, subdict in ss['data'][num].iteritems(): #'paging' or 'data'?
				#	print majorkey
				#	print subdict
				#	for subkey, value in subdict.iteritems():
				#		print subkey, value
				#print '  '+str(ss['data'][num]['created_time'].encode('ascii', 'ignore'))
				createdtime = str(ss['data'][num]['created_time'].encode('ascii', 'ignore'))
				#print '  '+str(ss['data'][num]['type'].encode('ascii', 'ignore'))+'!'
				fbtype = str(ss['data'][num]['type'].encode('ascii', 'ignore'))
				try:
					#print ' msg '+str(ss['data'][num]['message'].replace("'","''").replace(';','').encode('ascii', 'ignore'))+'!'
					fbmessage = str(ss['data'][num]['message'].replace("'","''").replace(';','').encode('ascii', 'ignore'))
				except:
					fbmessage = ''
				try:
					#print ' sty '+str(ss['data'][num]['story'].replace("'","''").replace(';','').encode('ascii', 'ignore'))+'!'
					fbstory = str(ss['data'][num]['story'].replace("'","''").replace(';','').encode('ascii', 'ignore'))
				except:
					fbstory = ''

				try:
					#print '  '+str(ss['data'][num]['comments']['count'])+'.'
					fbcomments = str(ss['data'][num]['comments']['count'])
				except:
					fbcomments = 0
				try:
					#print '  '+str(ss['data'][num]['likes']['count'])+'.'
					fblikes = str(ss['data'][num]['likes']['count'])
				except:
					fblikes = 0
				try:
					#print '  '+str(ss['data'][num]['shares']['count'])+'.'
					fbshares = str(ss['data'][num]['shares']['count'])
				except:
					fbshares = 0
				try:
					namee = str(ss['data'][num]['from']['name'])
				except:
					namee = ''
				try:
					#print '  '+str(ss['data'][num]['link'])+'.'
					link = str(ss['data'][num]['link']).replace("'","''")
				except:
					link = ''
				#print '*************************'

				#print str(ss['data'][num]['id'])
				fid = str(ss['data'][num]['id'])
				print str(ss['data'][num]['id']) + ' - ' + namee + ' (' + fbtype + ')'
				from_name = namee.replace("'","''").encode('ascii', 'ignore')
				#print str(ss['data'][num]['from']['id'])
				from_id = str(ss['data'][num]['from']['id'])

				query = """insert into searches (fid, from_id, from_name, keyword, type, link, posted, message, story, likes, comments, shares, harvested, run_id) 
					values ('"""+str(fid)+"""', '"""+str(from_id)+"""', '"""+str(from_name)+"""', '"""+str(keyword)+"""', '"""+str(fbtype)+"""', '"""+str(link)+"""',cast('"""+str(createdtime).replace('+0000','')+"""' as datetime), '"""+str(fbmessage)+"""', '"""+str(fbstory)+"""', '"""+str(fblikes)+"""', '"""+str(fbcomments)+"""', '"""+str(fbshares)+"""', now(), '"""+str(run_id)+"""')"""
				#print query
				try:
					cur.execute(query)
				except:
					print '#################### SQL ISSUE ###########################'
					print query
					print '#################### SQL ISSUE ###########################'
				#print '  '+str(ss['data'][num]['message'].encode('ascii', 'ignore'))+' '
				conn.commit()
			#print ss['paging']['next']
			print str(len(ss['data'])) + ' = element "data" length'
			#sleep(1)

			cur.execute("""insert into searchbank (fid, from_id, from_name, keyword, type, link, posted, message, story, likes, comments, shares, harvested, run_id)
			select distinct fid, from_id, from_name, keyword, type, link, posted, message, story, likes, comments, shares, harvested, run_id from searches where fid NOT in
			(select distinct fid from searchbank)""")

			cur.execute("""delete from searches where keyword = '"""+str(keyword)+"""'""")

			cur.execute("select ifnull((select ifnull(TotalHarvested,0) from fbsearchlog where keyword = '"+str(keyword)+"' order by rundate desc limit 0,1),0)")
			total_harvested = cur.fetchone()[0]

			cur.execute("""insert into fbsearchlog (BatchId, keyword, RunDate, HarvestedThisRun, TotalHarvested) values
			(
			'"""+str(run_id)+"""',
			'"""+str(keyword)+"""',
			now(),
			((select count(*) from searchbank where keyword = '"""+str(keyword)+"""')-"""+str(total_harvested)+"""),
			(select count(*) from searchbank where keyword = '"""+str(keyword)+"""')
			)""")

			conn.commit()

			cur.execute("""select ifnull(HarvestedThisRun,TotalHarvested) from fbsearchlog where BatchId = '"""+str(run_id)+"""' and keyword = '"""+str(keyword)+"""' order by RUnDate desc limit 0,1""") 
			harvienum = cur.fetchone()
			newones = harvienum[0]
			print Fore.GREEN + Style.BRIGHT + str(keyword) + Style.RESET_ALL
			print str(newones) + ' actually kept'

			try:
				nextpage = ss['paging']['next']
				print nextpage
			except:
				nextpage = 'NO'
				print 'No next page avail'
		except:
			print 'Some kind of API errors - invalid data JSON returned maybe?'
			nextpage = 'NO'
			newones = 0
			print 'ERROR'
			print sys.exc_info()[0]
			print sys.exc_info()[1]
			sleep(2)
	#sleep(2)



elapsed = time() - startTime
print "Finished. Total time: " + strftime('%H:%M:%S', gmtime(elapsed))
done_time = strftime('%H:%M:%S', gmtime(elapsed))