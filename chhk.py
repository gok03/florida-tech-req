import urllib2
import json

jsonfile = open('chhk.json', 'w')
jsonfile.write('[')

with open('misl_words.json') as data_file:    
    data = json.load(data_file)
    for x in range(len(data)):
    	temp = data[x].split()
    	for i in temp:
    		tmp = raw_input( i + " : y or n")
    		if tmp == 'y':
    			json.dump(i, jsonfile)
    			jsonfile.write(',')
jsonfile.write(']')	


