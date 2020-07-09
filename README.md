# florida-tech-req

## Readme not updated yet. Will do it soon

## Plan

1. get the links of company websites from a local directory
2. get the phone number and address of each company
3. figure out the career like pages
4. scrap the requirement of the jobs
5. create syn set of the req. list
6. plot on map


## Completed 

 ### Scripts
 - one.py
 	- The directory i m using to find the links of company has a seperate page for each company which inturn containes the deatils.
 	- So, this script is used to find the relative links within the directory for each company.

 - two.py
 	- This is used to find the address of each company from the directory.

 - three.py
 	- This is used to find the company website urls from relative links.

 - four.py
 	- Same as above it finds the website urls and also the phone numbers of the company.
 	- Just to have a relation of index between urls and phone number json (four-1.json & four-2.json resp.)

 - six.py
 	- This is used to find all computer related terms.
 	- will be used to scrap the requirement of jobs.

 - five.py
 	- links to all the tech terms description.


 ### Dbs.

 - one.json
 	- relative links to company details.

 - two.json
 	- address of companies.

 - three.json
 	- the company's website url.

 - four-1.json
 	- same as above.
 - four-2.json
 	- phone numbers of the company.

 - six.py
 	- computer tech terms.

 - five.py
 	- description of tech terms.
 

 ### Inwords

 - Company details like urls, address, phone numbers are obatined.
 - computer tech terms list obtained.




## To complete

 - Find the terms that are related to careers.
 - Find the terms that are realted to technical job titles
 - crawl each of the link in three.json and find the absolute url list of their career like pages.
 - go through those pages stored above, prepare a word list from the page.
 - compare the word list with job titles/technical requirements and obtain the match.(A lot of process involved in it)
 - store the url with name of the company, tech terms, lat-lng, address and phone number.
 - put on map

 The above steps are written in short.<br/>
 When i complete each task, there will be a description coming along with it.

