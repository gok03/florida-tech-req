# to find url of all companies in florida
import httplib2
import json
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str

http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)

ed = []

edpath = r"seg_words.txt"
words = open(edpath).read().split()
for  word in words:
       ed.append(word)

td = []
with open('seg_techwords.json') as data_file:    
    data = json.load(data_file)
    for x in data:
    	td.append(x)

misl_words = []
jsonfile = open('nine1.json', 'w')
jsonfile.write('[')

with open('finished/eight.json') as data_file:    
    data = json.load(data_file)
    for i in range(len(data)):
    	print str(i)+"/"+str(len(data))
    	if len(data[i][0]) > 1:
    		for j in data[i][0]:
    				status, response = http.request(j)
    				if status.status==200:
							site = BeautifulSoup (response.decode('utf-8', 'ignore'))
							[s.extract() for s in site(['style', 'script', '[document]', 'head', 'title'])]
							visible_text = site.getText()
							found = visible_text.encode('ascii','ignore').split()
							fnd_list = []
							tch_list = []
							tch_list.append(data[i][0][0])
							for wd in found:
								wd = ''.join(e for e in wd if e.isalpha())
								if wd.lower() not in ed and wd.lower() not in fnd_list:
									if wd.lower() in td:
										if wd.lower() not in tch_list:
											tch_list.append(wd.lower())
									else:
										if wd.lower() not in misl_words:
											misl_words.append(wd.lower())
							json.dump(tch_list, jsonfile)
							jsonfile.write(',')

jsonfile.write(']')
jsonfile1 = open('misl_words.json', 'w')
json.dump(misl_words, jsonfile1)
