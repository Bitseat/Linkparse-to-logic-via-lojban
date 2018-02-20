#!/bin/bash
#gnome-terminal    # launch a new terminal
#kill -9 $PPID
#gnome-terminal -e guile --version
#gnome-terminal -x ls
#kill -9 $PPID
gnome-terminal -x sh -c "cd ../../kukucog/opencog/build && ./opencog/cogserver/server/cogserver -c ../lib/opencog_patternminer_nlp.conf; bash" 
sleep 2
gnome-terminal -x sh -c "cd ../.. && rlwrap telnet localhost 17001 && scm; bash"
