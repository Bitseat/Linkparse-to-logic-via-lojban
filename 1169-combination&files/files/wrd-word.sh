#!/bin/bash



for f in {1..1158}
do
sed 's/WrdInstanceNode/WordInstanceNode/g' newfile$f.scm > /home/bitseat/Desktop/edited/newfile$f.scm
done