# -*- coding: utf-8 -*-
#### Version includes network viz and links to text and pdf originals
from flask import Flask
from flask import render_template
from flask import request
import os
import json
#import time
#import urllib2
import solr

#### Configuring this app and its associated servers
search_host = 'http://localhost:8081/solr/'   # Full address of the solr search server
flask_port = 8080   #port for the web app

#### Begins web app
app = Flask(__name__)

def get_result(raw_query , fquery): 
    query = '+'.join(raw_query.split())
    fquery = fquery
    search_collection = 'linksdgs'
    search_server = search_host + str(search_collection)
    s = solr.SolrConnection(search_server)
    response = s.select(query , facet='true' , facet_field=['SDG' , 'Publication'] , rows=75 , fq=fquery)
    sdg_facet = response.facet_counts['facet_fields']['SDG']
    publication_facet = response.facet_counts['facet_fields']['Publication']
    result_list = response.results
    numFound = response.numFound
    header = response.header
    chart_data = json.dumps(sdg_facet)
        
    serie = []
    for hit in sdg_facet:
        serie.append(sdg_facet[hit])
        
    label = []
    for hit in sdg_facet:
        label.append(hit.encode('utf8'))

    return {'header': header , 'numFound' : numFound , 'sdg_facet' : sdg_facet , 'publication_facet' : publication_facet , 'result_list' : result_list , 'chart_data': chart_data, 'serie' : serie , 'label' : label}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    fquery = request.args.get("fquery")
    search = request.args.get("search")
    if not search:
        search = "*"
    if not fquery:
        fquery = ""
    data = get_result(search , fquery)
    return render_template("search.html", data=data)

@app.route("/data/<rows_returned>")
def data(rows_returned):
    search = request.args.get("search")
    query = search
    search_collection = 'linksdgs'
    search_server = search_host + str(search_collection)
    s = solr.SolrConnection(search_server)
    response = s.select(query , rows=rows_returned)
    return render_template("data.json", response=response)

@app.route("/data2")
def data2():
    row = request.args.get("row")
    query = request.args.get("query")
    search_collection = 'linksdgs'
    search_server = search_host + str(search_collection)
    s = solr.SolrConnection(search_server)
    response = s.select('india' , rows=10)
    return render_template("data2.json", response=response)

@app.route("/sigma")
def sigma():
    return render_template("sigma.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', flask_port))
    app.run(host='0.0.0.0', port=port, debug=True)