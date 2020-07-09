import urllib2
import json

jsonfile = open('chhk1.json', 'w')

lst = []
with open('chhk.json') as data_file:    
    data = json.load(data_file)
    for x in data:
    	if x.lower() not in lst:
    		lst.append(x.lower())

json.dump(lst, jsonfile)
    			


