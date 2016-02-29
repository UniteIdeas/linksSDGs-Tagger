#!/usr/bin/env python

# Setting up the environment

import subprocess
import sys

#List commands to execute here.

#firewall and clock
NLTK = "sudo pip install -U nltk"
SCIKIT_LEARN = "sudo pip install -U scikit-learn"
PDFMINER = "sudo pip install -U pdfminer"
PUNKT = "sudo python -m nltk.downloader punkt"
SOLRPY = "sudo pip install -U solrpy"

#order commands in sequence
cmds = [NLTK, SCIKIT_LEARN, PDFMINER, PUNKT, SOLRPY]

#Iterates over list, running statements for each item in the list
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)