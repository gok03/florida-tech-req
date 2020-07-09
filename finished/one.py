# to find the urls containing company information
import urllib
import lxml.html
import json

jsonfile = open('one.json', 'w')

ul = 'http://businessdirectory.bizjournals.com/southflorida/information_technology/page/'
jsonfile.write('[')
for i in range(1,52):
    connection = urllib.urlopen(ul+str(i))
    dom=lxml.html.fromstring(connection.read())
    for link in dom.xpath('//a/@href'):
        lnk = link
        link = link.split("/") 
        if(3 < len(link)):
            if(link[3].isdigit()):
                if(int(link[3]) > 0):
                    json.dump(lnk, jsonfile)
                    jsonfile.write(',')
jsonfile.write(']')

