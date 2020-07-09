file = r"chk.txt"
words = open(file).read().split('\n')
print 'No. of total lines : '+str(len(words))

temp = 0
for i in words:
	if i.strip():
		temp+=1

print 'No. of Blank lines : ' + str(len(words) - temp)

print 'No. of Non empty lines : ' + str(temp)

print 'No. of Tabs : ' + str(open(file).read().count('\t'))

print 'No. of New lines : ' + str(open(file).read().count('\n'))

print repr(open(file).read()).replace(' ',r'')