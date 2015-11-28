import requests
import json
import os

url = "http://www.sentiment140.com/api/bulkClassifyJson?appid=wcarter312@gmail.com"
gamename = 'chears'
fn = 1
path, dirs, files = os.walk("../data/json/" + gamename + "/senti/").next()
max_files = len(files) - 1 #Mac creates invisible file for - 1

while fn <= max_files:
    try:
        json_data = open("../data/json/" + gamename + "/orig/" + gamename + "_" + str(fn) + ".json").read()
    except IOError:
        print "Error opening file: " + str(fn)
        break
    tweet_data = json.loads(json_data)
    tweet_req = requests.post(url, json=tweet_data)
    if tweet_req.status_code == 200:
        senti_out = open("../data/json/"+gamename +"/senti/"+ gamename +"_" + str(fn) + ".json", 'w')
        for line in tweet_req.iter_lines():
            senti_out.write(line)         
    else:
        print "ERROR: " + tweet_req.status_code
        break   
    print fn
    fn = fn + 1  
print "Finished"
