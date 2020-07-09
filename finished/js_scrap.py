import urllib2
import json
import re
import lxml.html
from lxml.etree import tostring
from bs4 import BeautifulSoup

jsonfile = open('latlng.json', 'w')
jsonfile.write('[')
ul = 'http://businessdirectory.bizjournals.com'
with open('finished/one.json') as data_file:    
    data = json.load(data_file)
    for x in range(len(data)):
    	print str(x)+'/'+str(len(data))
    	jsonfile.write('[')
    	web = urllib2.urlopen(ul+data[x])
    	dom=lxml.html.fromstring(web.read())
    	for link in dom.xpath("//div[@class='b2secDetails-URL']/ul/li/a/@href"):
    		json.dump(link, jsonfile)

    	rg = re.compile('((?:[a-z][a-z]+))(\\s+)(google\\.maps\\.LatLng)(\\()(\\s+)([+-]?\\d*\\.\\d+)(?![-+0-9\\.])(,)(\\s+)([+-]?\\d*\\.\\d+)(?![-+0-9\\.])(\\))(;)',re.IGNORECASE|re.DOTALL)
    	js_text = re.findall(rg, dom.xpath("//script")[14].text)
    	for i in js_text:
    		for j in range(len(i)):
				if j == 5 or j == 8:
					jsonfile.write(',')
					json.dump(i[j], jsonfile)
		jsonfile.write(']')
		jsonfile.write(',')
jsonfile.write(']')