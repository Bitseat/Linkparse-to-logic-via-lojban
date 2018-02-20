import os
import sys
import fileinput
import re
import linecache

fileToSearch  = "/home/bitseat/Desktop/see/parallel-files/parse-replaced3.scm"

someFile = open( fileToSearch, 'r+' )
tempFile = open ("/home/bitseat/Desktop/see/parallel-files/bit1.txt", 'w')
newfile = open ("/home/bitseat/Desktop/see/parallel-files/parse-replaced-left1.scm", 'w')


#pattern = r'"([A-Za-z0-9_\./\\-]*)"'
 
tempFile.writelines([l for l in open("/home/bitseat/Desktop/see/parallel-files/parse-replaced3.scm").readlines()])     
print "made bit"
tempFile.close()

tempFile = open ("/home/bitseat/Desktop/see/parallel-files/bit1.txt", 'r+')
ineval = False
inpredicate = False
inlistlink = False
inlistnode1 = False
inlistnode2 = False
inimp= False
inimpnode1 = False
inimpnode2 = False
for line in tempFile:
	if line.startswith(";\"") or line.startswith(";P"):
		newfile.write(line)
	if "(EvaluationLink" in line:
		ineval = True
		evalfirst = line
		print "first"
	if ineval and "PredicateNode" in line and "sumti" in line and not "(SimpleTV" in line:
		inpredicate = True
		evalsecond = line
		print "second"
	if inpredicate and "(ListLink" in line:
		inlistlink = True
		evalthird =line
		print "third"
	if inlistlink and "(PredicateNode" in line and not "(SimpleTV" in line:
		inlistnode1 = True
		evalfourth =line
		print "fourth"
	if inlistnode1 and "(ConceptNode" in line:
		inlistnode2 = True
		evalfifth =line
		print "fifth"
	if inlistnode2:
		newfile.write(evalfirst)
		#newfile.write("\n")
		newfile.write(evalsecond)
		newfile.write("  ")
		newfile.write(evalthird)
		#newfile.write("\n")
		newfile.write(evalfourth)
		#newfile.write("\n")
		newfile.write(evalfifth)
		#newfile.write("\n")
		newfile.write("                       )\n")
		newfile.write("                )\n")
		ineval = False
		inpredicate = False
		inlistlink = False
		inlistnode1 = False
		inlistnode2 = False
		continue
	if "(ImplicationLink" in line:
		inimp = True
		imp1 = line
		print "in imp"
	if inimp and "___" in line and not "(SimpleTV" in line:
		inimpnode1 = True
		impnode1 = line
		print "in imp node 1"
	if inimpnode1 and "(PredicateNode" in line and not "___" in line and not "(SimpleTV" in line:
		inimpnode2 = True
		impnode2 = line
		print "in imp node 2"
	if inimp and inimpnode1 and inimpnode2:
		newfile.write(imp1)
		newfile.write(impnode1)
		newfile.write(impnode2)
		newfile.write(")\n")
		inimp= False
		inimpnode1 = False
		inimpnode2 = False
		#continue




	