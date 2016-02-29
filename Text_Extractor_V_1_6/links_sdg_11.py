# -*- coding: utf-8 -*-

"""This program takes a list of .txt files and extracts all sentences which mention any SDG, 
    based on the list of keywords below for each SDG.
    Also it categorize the sentences."""

import os
import glob
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import datetime
import solr
from random import randint

############# CONFIGURATION #############
#file and folders
source = './text/'
destination = './output/'
results_filename = 'results_' + str(datetime.datetime.now()) + '.txt'
file_filter = '*.txt'
search_collection = 'linksdgs'
search_server = 'http://your_solr_host__/solr/' + str(search_collection)

#########################################

#Lists of keywords
sdg_1 = ['poverty']
sdg_2 = ['hunger' , 'starve']
sdg_3 = ['health' , 'well-being']
sdg_4 = ['education' , 'school']
sdg_5 = ['gender' , 'equality']
sdg_6 = ['water' , 'sanitation']
sdg_7 = ['energy' , 'fuel']
sdg_8 = ['work' , 'employment' , 'growth']
sdg_9 = ['industry' , 'innovation' , 'infrastructure']
sdg_10 = ['inequality']
sdg_11 = ['cities' , 'city' , 'urban']
sdg_12 = ['consumption' , 'production']
sdg_13 = ['climate']
sdg_14 = ['sea' , 'oceans' , 'river' , 'fish']
sdg_15 = ['animals' , 'plants' , 'deforestation']
sdg_16 = ['peace' , 'justice' , 'institutions']
sdg_17 = ['partnership' , 'sdg']

causal = ['causes' , 'cause' , 'causal' ,'causing' ,'drives' , 'driver' , 'driving' ,'generates' , 'generate' , 'generating' ,'effect']
constraint = ['barrier' , 'barriers' ,'constraint' , 'constraints' , 'challenge' , 'challenges' ,'obstacle' , 'obstacles' , 'limit' , 'limits' , 'limiting' ,'prevent' ,'prevents' , 'preventing' ,'hamper' ,'hampers' , 'hampering' ,'blocks' , 'blocking']
recommendation = ['recommend' ,'recommendation' , 'recommends' , 'recommending' , 'recommended' ,'policy' , 'policymaker' , 'government' ]
    
##########################################

#This obtains the list of files to process
os.chdir(source)                    #move to source dir
file_list = glob.glob(file_filter)  
os.chdir("..")                      #return to starting dir

#This checks if a sentence contains keywords for a given SDG
def sdg_belong (goal_keywords, sentence):
    if set(goal_keywords).intersection(set(word_tokenize(sentence))):
        return True
    else:
        return False

#This checks which SDGs are mentioned in each sentence
def sdg_check (sent):
    matches = []
    if sdg_belong(sdg_1, sent): matches.append('SDG 1')
    if sdg_belong(sdg_2, sent): matches.append('SDG 2')
    if sdg_belong(sdg_3, sent): matches.append('SDG 3')
    if sdg_belong(sdg_4, sent): matches.append('SDG 4')
    if sdg_belong(sdg_5, sent): matches.append('SDG 5')
    if sdg_belong(sdg_6, sent): matches.append('SDG 6')
    if sdg_belong(sdg_7, sent): matches.append('SDG 7')
    if sdg_belong(sdg_8, sent): matches.append('SDG 8')
    if sdg_belong(sdg_9, sent): matches.append('SDG 9')
    if sdg_belong(sdg_10, sent): matches.append('SDG 10')
    if sdg_belong(sdg_11, sent): matches.append('SDG 11')
    if sdg_belong(sdg_12, sent): matches.append('SDG 12')
    if sdg_belong(sdg_13, sent): matches.append('SDG 13')
    if sdg_belong(sdg_14, sent): matches.append('SDG 14')
    if sdg_belong(sdg_15, sent): matches.append('SDG 15')
    if sdg_belong(sdg_16, sent): matches.append('SDG 16')
    if sdg_belong(sdg_17, sent): matches.append('SDG 17')
    
    ##match types
    match_types = []
    if sdg_belong(causal, sent): match_types.append('Causal')
    if sdg_belong(constraint, sent): match_types.append('Constraint')
    if sdg_belong(recommendation, sent): match_types.append('Recommendation')
    
    return matches , match_types
    
            
#This function will be executed in each file    
def sent_extract (filename):
    f = open(source+filename , 'rU')    #Source text files
    raw = f.read().decode('utf8')
    all_sent = sent_tokenize(raw)
    sentences_to_save = []
    s = solr.SolrConnection(search_server)  # Search server details 
    for sentence in all_sent:
        sdg_check_this = sdg_check(sentence)
        ####### Conditions: Keep sentences mentioning SDG11 and at least another SDG, must be shorter than 1000 characters
        #if len(sdg_check_this)>1 and 'SDG_11' in sdg_check_this and len(sentence)<1000:
        if len(sdg_check_this[0])>1 and len(sentence)<1000:  #these conditions accept all sdgs not only 11
            
            ####### Use this to display results on screen
            print 'Matches : ', sdg_check_this , '\n' , sentence , '\n'
            
            ####### Use the two lines below to generate a human readable file.
            str_to_write = '\n\nFile of Origin : ' + filename + '\nSentence Matches : ' + str(sdg_check_this[0]) + '\nType : ' + str(sdg_check_this[1]) + '\nFull sentence : \n' + sentence.encode('utf8')
            open(destination + results_filename , 'a+').write(str_to_write)
            
            ####### Use the lines below to inject results to solr
            # print 'Match found : ', sdg_check_this , '\n'
            # try:
            #     #s.add ( Publication = str(filename) , SDG = sdg_check_this , Sentence = sentence )
            #     s.add ( Publication = str(filename) , SDG = sdg_check_this[0] , Sentence = sentence , Type = sdg_check_this[1])
            #     s.commit()           
            # except:
            #     print 'Error'
                
#This is where the magic happens
def iterdir(function):
    for i in range(len(file_list)):
        function(file_list[i]) #
        print '........done parsing file : ' + str(file_list[i]) + ' File : ' + str(i+1) + ' of ' + str(len(file_list)) + '.\n'
    print (' ......All done ...')
    
#run-it calling the function you want to run
iterdir(sent_extract)