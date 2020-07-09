# to find the address of all companies in florida
import urllib
import lxml.html
import json

jsonfile = open('two.json', 'w')

ul = 'http://businessdirectory.bizjournals.com/southflorida/information_technology/page/'
jsonfile.write('[')
for i in range(1,52):
	connection = urllib.urlopen(ul+str(i))
	dom=lxml.html.fromstring(connection.read())
	for link in dom.xpath("//td[@class='results_td_address']/ul/li/p"):
	    link = link.text.strip()
	    json.dump(' '.join(link.split()), jsonfile)
        jsonfile.write(',')
jsonfile.write(']')
    
