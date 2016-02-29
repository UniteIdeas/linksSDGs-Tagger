#!/usr/bin/env python

# Setting up the environment

import subprocess
import sys

#List commands to execute here.

OPEN_SSH = "sudo ufw allow ssh"
OPEN_WEBAPP = "sudo ufw allow 8080"
OPEN_SOLR = "sudo ufw allow 8081"   #use during development or to test access to Solr server
ENABLE_FIREWALL = "sudo ufw enable"
DISABLE_FIREWALL = "sudo ufw disable" #use to stop the firewall and alow all traffic
FIREWALL_STATUS = "sudo ufw status" #use to view the firewall status

#order commands in sequence
cmds = [OPEN_SSH, OPEN_WEBAPP, ENABLE_FIREWALL, FIREWALL_STATUS]

#Iterates over list, running statements for each item in the list
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)