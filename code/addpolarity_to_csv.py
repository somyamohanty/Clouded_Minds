#This takes the sentiment polarity in JSON and adds it back to the CSV.

import csv
import json
import os

#Config
gamename = 'mcinew'
fn = 1

#Open files / load JSON
reader = csv.DictReader(open("../data/" + gamename + ".csv", 'rb'), delimiter=',', quotechar='"')
json_data = open("../data/json/" + gamename + "/senti/" + gamename + "_" + str(fn) + ".json").read()
sent = json.loads(unicode(json_data, "ISO-8859-1"))

#Variables and setup
rc_id = 2
jid = 0
path, dirs, files = os.walk("../data/json/" + gamename + "/senti/").next()
max_files = len(files)

#!!!!IMPORTANT!!!!!!! CHECK WHEN RUNNING IN MAC
#max_files = max_files - 1  #Mac creates invisible file 


#Write
with open("../data/" + gamename + "_sent.csv", 'w') as outfile:
    fieldnames = ['text', 'user', 'created_at','timestamp', 'geo', 'lang','polarity']
    writer = csv.DictWriter(outfile, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()
    
    
    
    for row in reader:
            if sent['data'][jid]['id'] == rc_id:
                writer.writerow({
                        'text': row['text'],
                        'user': row['user'],
                        'created_at': row['created_at'],
                        'timestamp': row['timestamp'],
                        'geo': row['geo'],
                        'lang' : row['lang'],
                        'polarity' : sent['data'][jid]['polarity'],
                    })
                jid = jid + 1
                
            rc_id = rc_id + 1
        
            if jid == 5000 or jid == len(sent['data']):
                fn = fn+1
                if fn <= max_files:
                    try:
                        print fn
                        json_data = open("../data/json/" + gamename + "/senti/" + gamename + "_" + str(fn) + ".json").read()
                    except IOError:
                        print "Error opening JSON file or no more files exist " + str(fn)
                        break
                    sent = json.loads(unicode(json_data, "ISO-8859-1"))
                jid = 0

    outfile.close()

