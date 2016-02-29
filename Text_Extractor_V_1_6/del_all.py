# -*- coding: utf-8 -*-

"""This program takes a list of .txt files and extracts all sentences which mention any SDG, 
    based on the list of keywords below for each SDG."""

import solr
from random import randint

############# CONFIGURATION #############
#file and folders

search_collection = 'linksdgs'
search_server = 'http://your_solr_host__/solr/' + str(search_collection)

#########################################


s = solr.SolrConnection(search_server)  # Search server details 

#s.add(sentence = phrase, sdg = SDGs , publication = pub_name)

s.delete_query('*:*')
s.commit()

# response = s.query('*:*')

# for hit in response.results:
#     #print hit['sentence']
#     print hit
