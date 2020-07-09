# to find url of all companies in florida
import urllib
import lxml.html
import json

jsonfile = open('three.json', 'w')

ul = 'http://businessdirectory.bizjournals.com'
jsonfile.write('[')
with open('one.json') as data_file:    
    data = json.load(data_file)
    for x in range(len(data)):
		connection = urllib.urlopen(ul+data[x])
		dom=lxml.html.fromstring(connection.read())
		for link in dom.xpath("//div[@class='b2secDetails-URL']/ul/li/a/@href"):
		    json.dump(link, jsonfile)
	        jsonfile.write(',')
jsonfile.write(']')
    
