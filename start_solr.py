#!/usr/bin/env python

# Setting up the environment

import subprocess
import sys
import os

#List commands to execute here.

#Solr start and config
solr_port = '8081'
STARTSOLR = "linksSDGs/solr-5.4.0/bin/solr start -p " + solr_port

#order commands in sequence ## Uncomment these for 1st install
cmds = [ 
    STARTSOLR
    ]

#Iterates over list, running statements for each item in the list
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)
    
