#Converts the CSV format to the Sentiment140 compatible json
#Note that it would be better to use the MongoDB directly

gamename = "chears"

inname = "../data/" + gamename + ".csv"
outname = "../data/json/" +gamename + "/orig/" + gamename

file_num = 1

infile = open(inname, 'r')
lang_avail = False #This field indicates if this CSV has the lang column, currently manual entry
outfile = open(outname + '_' + str(file_num) + '.json', 'w')

linenum = 0
act_linenum = 0

outfile.write('{"language": "auto", "data": [')
for line in infile:
	if linenum == 0: #Ignore the column headers
		linenum += 1
		continue

	if(act_linenum == 5000): #5000 is based on API's recommendation for 60 second timeout window
		outfile.write("]}")
		outfile.close()
		file_num += 1
		outfile = open(outname + '_' + str(file_num) + '.json', 'w')
		outfile.write('{"language": "auto", "data": [')
		act_linenum = 0

	line_split = line.split(',')
	text = line_split[0].strip().translate(None,'"\/\\\r\t\n\b\f\t')
		
	if len(text) > 3: #Prevent empty text field ("text": "")
		if lang_avail == True:
			lang = line_split[5]
			if lang.startswith('en') or lang.startswith('es'): #Sentiment140 only supports these two langs
				if linenum > 1:
					outfile.write(',') #Writes the closing comma of {"text": "I love Titanic.", "id": 1234}, 
				
				outfile.write('{"text": "'+ text + '", "id": '+ __builtins__.str(linenum) +'}')
				act_linenum += 1
		else:
			if linenum > 1:
				outfile.write(',')
			outfile.write('{"text": "'+ text +'", "id": '+ __builtins__.str(linenum) +'}')
			act_linenum += 1
	
	linenum += 1

infile.close()
outfile.write("]}")
outfile.close()
	
