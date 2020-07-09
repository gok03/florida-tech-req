import urllib
import json
import lxml.html
import re
from bs4 import BeautifulSoup


ul = 'http://businessdirectory.bizjournals.com'
connection = urllib.urlopen(ul+"/southflorida/information_technology/3384106/561-media.html")
soup = BeautifulSoup(connection.read(), 'lxml')
if len(soup.find_all("script")) < 14:
	print soup.find_all("script")
else:
            data  = soup.find_all("script")[14].string

            re1='((?:[a-z][a-z]+))' # Word 1
            re2='(\\s+)'    # White Space 1
            re3='(google\\.maps\\.LatLng)'  # Fully Qualified Domain Name 1
            re4='(\\()' # Any Single Character 1
            re5='(\\s+)'    # White Space 2
            re6='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 1
            re7='(,)'   # Any Single Character 2
            re8='(\\s+)'    # White Space 3
            re9='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 2
            re10='(\\))'    # Any Single Character 3
            re11='(;)'  # Any Single Character 4

            rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11,re.IGNORECASE|re.DOTALL)

            js_text = re.findall(rg, data)
            for i in js_text:
                for j in range(len(i)):
                    if j == 5 or j == 8:
                        print i[j]