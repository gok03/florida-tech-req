# to find url of all companies in florida
import urllib
import lxml.html
import json
from  more_itertools import unique_everseen

jsonfile = open('eight.json', 'w')
jsonfile.write('[')

with open('seven.json') as data_file:    
    data = json.load(data_file)
    for x in range(len(data)):
    	if(1 < len(data[x][0]) or 1 < len(data[x][1])):
    		data[x][0] = list(unique_everseen(data[x][0]))
    		data[x][1] = list(unique_everseen(data[x][1]))
    		json.dump(data[x], jsonfile)
    		jsonfile.write(',')
jsonfile.write(']')


