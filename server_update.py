#!/usr/bin/env python

# Setting up the environment

import subprocess
import sys
import os

#List commands to execute here.

#Server setup
UPDATE = "sudo apt-get update"

#order commands in sequence ## Uncomment these for 1st install
cmds = [
    UPDATE
    ]

#Iterates over list, running statements for each item in the list
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)