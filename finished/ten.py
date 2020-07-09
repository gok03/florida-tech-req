import urllib2
import json

dic={}

with open('nine.json') as data_file:    
    data = json.load(data_file)
    for x in data:
    	if len(x) > 1:
	    	if x[0] not in dic:
	    		temp = x[0]
	    		x = x[1:]
	    		dic[temp] = x
	    	else:
		    	temp = x[0]
		    	x = x[1:]
		    	tmp = dic[temp]
		    	for i in x:
		    		if i not in tmp:
		    			tmp.append(i)
		    	dic[temp] = tmp

with open('latlng.json') as data_file:    
    data = json.load(data_file)
    for x in data:
    	if x[0] in dic:
    		temp = dic[x[0]]
    		x1 = x[1:]
    		temp = x1 + temp
    		dic[x[0]] = temp

jsonfile = open('ten.json', 'w')
jsonfile.write('[')

for i in dic:
	jsonfile.write('[')
	json.dump(i, jsonfile)
	for j in dic[i]:
		jsonfile.write(',')
		json.dump(j, jsonfile)
	jsonfile.write(']')
	jsonfile.write(',')
jsonfile.write(']')