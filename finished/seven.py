import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
import json
from urlparse import urljoin

http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
word =  ['Candidates','careers','career','job','listing','join','venture','employment']
word1 = ['reach','contact']

jsonfile = open('seven.json', 'w')
jsonfile.write('[')

with open('finished/three.json') as data_file:    
	data = json.load(data_file)
	for x in range(len(data)):
		try:	
			status, response = http.request(data[x])
			if status.status==200:
				jsonfile.write('[[')
				json.dump(data[x], jsonfile)
				for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
					if link.has_key('href'):
						for j in range(len(word)):
							if word[j].lower() in link['href'].lower() or word[j].lower() in link.text.lower():
								jsonfile.write(',')
								json.dump(urljoin(data[x],link['href']), jsonfile)
				jsonfile.write('],[')
				json.dump(data[x], jsonfile)
				for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
					if link.has_key('href'):
						for j in range(len(word1)):
							if word1[j].lower() in link['href'].lower() or word1[j].lower() in link.text.lower():
								jsonfile.write(',')
								json.dump(urljoin(data[x],link['href']), jsonfile)
				jsonfile.write(']],')
		except :
			print "Site is Down -> "+ data[x]
jsonfile.write(']')