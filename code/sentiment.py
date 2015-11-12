import requests
import json

gamename = 'chears'

json_data = open("../data/json/" + gamename + "/orig/" + gamename + "_1.json").read() #TODO: For loop through each file in a directory, use the filename as a variable, and provide it to the output filename
tweet_data = json.loads(json_data)

url = "http://www.sentiment140.com/api/bulkClassifyJson?appid=wcarter312@gmail.com"
tweet_req = requests.post(url, json=tweet_data)
if tweet_req.status_code == 200:
	senti_out = open("../data/json/"+gamename +"/senti/"+ gamename +"_1.json", 'w')
	for line in tweet_req.iter_lines():
		senti_out.write(line)
else:
	print "ERROR: " + tweet_req.status_code
