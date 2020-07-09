#links to find the explanation for tech words
import urllib
import lxml.html
import json

jsonfile = open('five.json', 'w')

ul = 'http://www.computerhope.com/jargon/program.htm'
jsonfile.write('[')
connection = urllib.urlopen(ul)
dom=lxml.html.fromstring(connection.read())
for link in dom.xpath("//tr[@class='tcw']/td/p/a/@href"):
    json.dump(link, jsonfile)
    jsonfile.write(',')
jsonfile.write(']')

