from pymongo import MongoClient
from operator import itemgetter
import csv
import sys
db = MongoClient()[sys.argv[1]]
filename = ("../data/%s.csv") %(sys.argv[1])
with open(filename, 'w') as outfile:
  fieldnames = ['text', 'user', 'created_at','timestamp', 'geo','lang']
  writer = csv.DictWriter(outfile, delimiter=',', fieldnames=fieldnames)
  writer.writeheader()

  for data in db.Tweets.find():
    writer.writerow({ 
      'text': data['text'].encode('utf-8'), 
      'user': data['user'].encode('utf-8'), 
      'timestamp': data['timestamp'],
      'created_at':data['created_at'],
      'geo': data['geo'],
      'lang':data['lang']
    })

  outfile.close()
