# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:01:42 2015

@author: jmmnn
"""

> Use python 2.7. Note: Recomment to use Anaconda python and for IDE use Spyder
> Install packages pdfminer nltk scikit-learn nltk.punkt
Notes: to have the full NTK you might need to run at the Python console "nltk.download()" 

You can also use the istall_dependencies.py scipt by running:

$sudo python install_dependencies.py

>Create folders:
    originals
    fixed_name
    text

1) Obtain the full text of files by running from linux command line:
cd to folder "text"
"wget https://preview.c9users.io/jmmnn_1/python-nltk/release1/text/all_text_linksSDG.zip"
"unzip all_text_linksSDG.zip"

Alternative: If you want to extract your own text, do:
    > Save original .pdfs into folder "originals"
    > From python console Run rename-files.py
    > From python console Run extract_text.py  # This can take a while

2) Finally to get the results, open the file:
"links_sdg_11.py" and run it or from linux: "python links_sdg_11.py"
This will either 
> save the results in: ./output/results.txt
or
> store the results in an Apache Solr server

Note: Before running links_sdg_11.py open it in an editor and configure 
whether you want the output to text file or Solr (for this option enter your server name).


