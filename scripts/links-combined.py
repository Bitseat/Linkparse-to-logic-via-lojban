import os
import sys
import fileinput
import re
import linecache
j=1
while j<=1169:
  try:
    newFile = open ("/home/bitseat/Desktop/see/parallel-files/result3/links"+str(j)+".scm", 'w')
    with open('/home/bitseat/Desktop/see/parallel-files/english/eng-file'+str(j)+'.scm') as g:
       for line3 in g:
           line_cont1 = line3
           with open('/home/bitseat/Documents/tatoeba/dataset') as file:
               for i, line3 in enumerate(file):
               	   if line3 == line_cont1:
               	   	    print i
               	   	    value = i+1 
               	   	    thefile = open ("/home/bitseat/Desktop/all-in-one/exp/hh/here/"+str(value)+".scm", 'r')
               	   	    newFile.write(";")
               	   	    newFile.write(line3)
              
               	   	    for line3 in thefile:
               	   	    	newFile.write(line3)
                          with open('/home/bitseat/Desktop/see/parallel-files/lojban/file'+str(j)+'.scm') as f:
                            for line in f:
                              line_cont = line
                              newFile.write(";")
                              newFile.write(line)
                              flag=0
                              with open('/home/bitseat/Desktop/see/parallel-files/4.scm') as file:
                                for m, line1 in enumerate(file):
                                  if line1.strip() == line_cont.strip():
                                    print m + 1
                                    k= m + 1
                                    with open('/home/bitseat/Desktop/see/parallel-files/4.scm') as file2:
                                      for n, line2 in enumerate(file2):
                                        if n>=k and not re.match(r'\w', line2):
                                          newFile.write(line2)
                                        else:
                                          if n>=k and re.match(r'\w', line2):
                                            flag = 1
                                            break
                                 if flag==1:
                                  break
                      break
  except IOError:
    print "file doesn't exist"
  j+=1
                   