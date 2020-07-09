#to find the url and phone numbers of all companies
import urllib
import lxml.html
import json

jsonfile1 = open('four-1.json', 'w')
jsonfile2 = open('four-2.json', 'w')

ul = 'http://businessdirectory.bizjournals.com'
jsonfile1.write('[')
jsonfile2.write('[')
with open('one.json') as data_file:    
    data = json.load(data_file)
    for x in range(754):
		connection = urllib.urlopen(ul+data[x])
		dom=lxml.html.fromstring(connection.read())
		for link in dom.xpath("//div[@class='b2secDetails-URL']/ul/li/a/@href"):
		    if(link != ''):
			    json.dump(link, jsonfile1)
			    jsonfile1.write(',')
		    else:
		    	json.dump(('+'+data[x]), jsonfile1)
		        jsonfile1.write(',')
		for link in dom.xpath("//p[@class='b2Local-greenTextmed']"):
		    link = link.text.strip()
		    if(link != ''):
			    json.dump(link, jsonfile2)
			    jsonfile2.write(',')
		    else:
		    	json.dump(('+'+data[x]), jsonfile2)
		        jsonfile2.write(',')

jsonfile1.write(']')
jsonfile2.write(']')
    
