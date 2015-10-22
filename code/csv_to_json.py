#Converts the CSV format to the Sentiment140 compatible json
#Note that it would be better to use the MongoDB directly

inname = "../data/arsliv.csv"
outname = "../data/arsliv.json"

infile = open(inname, 'r')
outfile = open(outname, 'w')

linenum = 0
outfile.write("{\"data\": [")
for line in infile:
	if linenum == 0: #Ignore the column headers
		linenum += 1
		continue
	if linenum > 1:
		outfile.write(',') #Writes the closing comma of {"text": "I love Titanic.", "id": 1234}, 
	text = line.split(',')[0]
	outfile.write("{\"text\": \""+text+ "\", \"id\": "+str(linenum)+"}")
	linenum += 1
outfile.write("]}")
	
