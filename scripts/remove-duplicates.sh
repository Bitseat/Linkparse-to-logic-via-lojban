#!/bin/bash



for f in {1..1169}
do
	sed '$!N; /^\(.*\)\n\1$/!P; D' /path/to/file$f.scm > /path/to/new/file$f.scm
done
