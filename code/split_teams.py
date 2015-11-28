#Split teams based on team hashtag for individual team analysis

import csv
import json

#Config
gamename = 'chears'
t1 = "Arsenal" #AFC
t2 = "Chelsea" #CFC

#Open Game
reader = csv.DictReader(open("../data/" + gamename + "_sent.csv", 'rb'), delimiter=',', quotechar='"')

#Write game split into teams
with open("../data/" + gamename + "_sent_" +t1 + ".csv", 'w') as team1_f:
    with open("../data/" + gamename + "_sent_" + t2 + ".csv", 'w') as team2_f:
        fieldnames = ['text', 'user', 'created_at','timestamp', 'geo','polarity']
        t1_writer = csv.DictWriter(team1_f, delimiter=',', fieldnames=fieldnames)
        t1_writer.writeheader()
        t2_writer = csv.DictWriter(team2_f, delimiter=',', fieldnames=fieldnames)
        t2_writer.writeheader()

        for row in reader:
            #Team 1
                if row['text'].find("#AFC") >= 0:
                    t1_writer.writerow({
                                'text': row['text'],
                                'user': row['user'],
                                'created_at': row['created_at'],
                                'timestamp': row['timestamp'],
                                'geo': row['geo'],
                                'polarity' : row['polarity'],
                            })
                #Team 2
                if row['text'].find("#CFC") >= 0: 
                     t2_writer.writerow({
                                'text': row['text'],
                                'user': row['user'],
                                'created_at': row['created_at'],
                                'timestamp': row['timestamp'],
                                'geo': row['geo'],
                                'polarity' : row['polarity'],
                            })
team1_f.close()
team2_f.close()
reader.close()