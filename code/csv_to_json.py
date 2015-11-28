#Converts the CSV format to the Sentiment140 compatible json
#Note that it would be better to use the MongoDB directly

#Config variables
gamename = "chears"

#Output File and Input File
outname = "../data/json/" +gamename + "/orig/" + gamename
reader = csv.DictReader(open("../data/" + gamename + ".csv", 'rb'), delimiter=',', quotechar='"')
outfile = open(outname + '_' + str(file_num) + '.json', 'w')

#Variables to operate
file_num = 1
lang_avail = False #This field indicates if this CSV has the lang column, currently manual entry
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
    
    if len(cleantext) > 3: #Prevent empty text field ("text": "")
        if lang_avail == True:
            lang = line_split[5]
            if lang.startswith('en') or lang.startswith('es'): #Sentiment140 only supports these two langs
                if linenum > 1 and act_linenum != 0:
                    outfile.write(',') #Writes the closing comma of {"text": "I love Titanic.", "id": 1234}, 
                
                outfile.write('{"text": "'+ cleantext + '", "id": '+ __builtins__.str(linenum) +'}')
                act_linenum += 1
        else:
            if linenum > 1 and act_linenum != 0:
                outfile.write(',')
            outfile.write('{"text": "'+ cleantext +'", "id": '+ __builtins__.str(linenum) +'}')
            act_linenum += 1
    
    linenum += 1

infile.close()
outfile.write("]}")
outfile.close()
    
