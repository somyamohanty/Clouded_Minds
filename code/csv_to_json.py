#Converts the CSV format to the Sentiment140 compatible json
#Note that it would be better to use the MongoDB directly

inname = "../data/arsliv.csv"
outname = "../data/arsliv.json"

infile = open(inname, 'r')
lang_avail = False #This field indicates if this CSV has the lang column, currently manual entry
outfile = open(outname, 'w')

linenum = 0
outfile.write('{"language": "auto", "data": [')
for line in infile:
	if linenum == 0: #Ignore the column headers
		linenum += 1
		continue

	line_split = line.split(',')
	text = line_split[0].strip('"').rstrip()
	text = text.replace('"',' ')
	text = text.replace('\'',' ')
	text = text.replace('\\',' ')
	text = text.replace('\r',' ')
	text = text.replace('\t',' ')
	text = text.replace('\n',' ')
	text = text.replace('\b',' ')
	text = text.replace('\/',' ')
	text = text.replace('\f',' ')
	text = text.replace('\t',' ')
	if len(text) > 3: #Prevent empty text field ("text": "")
		if lang_avail == True:
			lang = line_split[5]
			if lang.startswith('en') or lang.startswith('es'): #Sentiment140 only supports these two. They can be en-US, etc. so we check the first part
				if linenum > 1:
					outfile.write(',') #Writes the closing comma of {"text": "I love Titanic.", "id": 1234}, 
				outfile.write('{"text": "'+ text + '", "id": '+ __builtins__.str(linenum) +'}')
		else:
			if linenum > 1:
				outfile.write(',')
			outfile.write('{"text": "'+ text +'", "id": '+ __builtins__.str(linenum) +'}')
	linenum += 1

infile.close()
outfile.write("]}")
outfile.close()
	
