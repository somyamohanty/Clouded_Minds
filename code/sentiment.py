import requests
import json

json_file = open("../data/arsliv.json").read() #TODO: Switch to a for loop to populate tweet_data, since request limit may be less than a file
tweet_data = json.loads(json_file)

url = "http://www.sentiment140.com/api/bulkClassifyJson?appid=wwc77@msstate.edu"
tweet_req = requests.post(url, json=tweet_data)
if tweet_req.status_code == 200:
	senti_out = open("../data/arsliv_sentiment.json", 'w')
	for line in tweet_req.iter_lines():
		senti_out.write(line)
else:
	print "ERROR: " + tweet_req.status_code
