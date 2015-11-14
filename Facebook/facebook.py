import urllib2
import urllib.request
import json
import MySQLdb

def connect_db():
	connection = MySQLdb.connect("localhost","root","root","dumps_facebook" )
	return connection

def create_post_url(graph_url, APP_ID, APP_SECRET): 
	#create authenticated post URL
	post_args = "/posts/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
	post_url = graph_url + post_args

	return post_url
	
def render_to_json(graph_url):
	#render graph url call to JSON
	web_response = urllib2.urlopen(graph_url)
	readable_page = web_response.read()
	json_data = json.loads(readable_page)
	
	return json_data

	
def main():
	#simple data pull App Secret and App ID
	APP_SECRET = "72b92f83ca614b697f38d27ddec3a873"
	APP_ID = "1068141439876846"
	
	#to find go to page's FB page, at the end of URL find username
	#e.g. http://facebook.com/walmart, walmart is the username
	list_companies = ["walmart", "cisco", "pepsi", "facebook"]
	graph_url = "https://graph.facebook.com/"
	

	#create db connection
	connection = connect_db()
	cursor = connection.cursor()
	
	#SQL statement for adding Facebook page data to database
	insert_info = ("INSERT INTO status "
					"(fb_id, likes, talking_about, username)"
					"VALUES (%s, %s, %s, %s)")

	for company in list_companies:
		#make graph api url with company username
		current_page = graph_url + company
		
		#open public page in facebook graph api
		json_fbpage = render_to_json(current_page)
		

		#gather our page level JSON Data
		page_data = (json_fbpage["id"], json_fbpage["likes"],
				     json_fbpage["talking_about_count"],
				     json_fbpage["username"])
		print page_data
		
		#extract post data
		post_url = create_post_url(current_page, APP_ID, APP_SECRET)
		json_postdata = render_to_json(post_url)
		json_fbposts = json_postdata['data']
		
		
		#print post messages and ids
		for post in json_fbposts:
			
			try:
				#try to print out data
				print post["id"]
				print post["message"]
				
			except Exception:
				print "Key error"
			
			
		#insert the data we pulled into db
		cursor.execute(insert_info, page_data)
		
		#commit the data to the db
		connection.commit()
		
	connection.close()

if __name__ == "__main__":
	main()    