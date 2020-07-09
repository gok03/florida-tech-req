#scraping tech words
import urllib
import lxml.html
import json

jsonfile = open('six.json', 'w')

ul = 'http://www.computerhope.com/jargon/program.htm'
jsonfile.write('[')
connection = urllib.urlopen(ul)
dom=lxml.html.fromstring(connection.read())
for link in dom.xpath("//tr[@class='tcw']/td/p/a"):
    json.dump(link.text.strip(), jsonfile)
    jsonfile.write(',')
jsonfile.write(']')

