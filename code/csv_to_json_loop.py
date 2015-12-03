#converts the CSV format to the Sentiment140 compatible json
#Note that it would be better to use the MongoDB directly
import csv, sys, os

gamenames = {"mcinew"} #lang tagged games
for gamename in gamenames:
    
    lang_avail = True #This field indicates if this CSV has the lang column, currently manual entry
    file_num = 1
    inname = "../data/" + gamename + ".csv"
    outname = "../data/json/" +gamename + "/orig/" + gamename
    reader = csv.DictReader(open(inname), delimiter=',', quotechar='"')
    
    
    if not os.path.exists("../data/json/"+gamename+"/orig/"):
	os.makedirs("../data/json/"+gamename+"/orig/")
    outfile = open(outname + '_' + str(file_num) + '.json', 'w')

    linenum = 2
    act_linenum = 0

    outfile.write('{"language": "auto", "data": [')
for row in reader:
    if(act_linenum == 5000): #5000 is based on API's recommendation for 60 second timeout window
        outfile.write("]}")
        outfile.close()
        file_num += 1
        outfile = open(outname + '_' + str(file_num) + '.json', 'w')
        outfile.write('{"language": "auto", "data": [')
        act_linenum = 0

    cleantext = row['text'].strip().translate(None,'"\/\\\r\t\n\b\f\t')
    clearlang = row['lang'].strip().translate(None,'"\/\\\r\t\n\b\f\t')
    
    
    if len(cleantext) > 3: #Prevent empty text field ("text": "")
        if lang_avail == True:
            if clearlang == 'en' or clearlang =='es': #Sentiment140 only supports these two langs
                if linenum > 1 and act_linenum != 0:
                    outfile.write(',') #Writes the closing comma of {"text": "I love Titanic.", "id": 1234}, 
                    
                outfile.write('{"text": "'+ cleantext + '", "id": '+ __builtins__.str(linenum) +'}')
                act_linenum += 1
        #else:
        #    if linenum > 1 and act_linenum != 0:
        #        outfile.write(',')
        #    outfile.write('{"text": "'+ cleantext +'", "id": '+ __builtins__.str(linenum) +'}')
        #    act_linenum += 1
    
    linenum += 1

outfile.write("]}")
outfile.close()
    
