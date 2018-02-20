import os
import sys
import fileinput
import re
import linecache
import collections

j = 1
while j <= 1169:
	newFile = open ("/home/bitseat/Desktop/see/the-lojbans/dups-removed/line-numbers/line-numbers-for-newfile"+str(j)+".scm", 'w')
	try:
		with open('/home/bitseat/Desktop/see/the-lojbans/dups-removed/file'+str(j)+'.scm') as f:
			for line in f:
				line_cont = line
				i=0
				with open('/home/bitseat/Documents/tatoeba/lojban-dataset.scm') as file:
					for line in file:
						if line == line_cont:
							newFile.write(str(i))
							newFile.write('\n')
							break
						i+=1
	except IOError:
		print "file not found"
	j +=1

