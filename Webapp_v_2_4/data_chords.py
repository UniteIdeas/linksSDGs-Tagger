import solr

#This file produces the matrix for the chord visualization

def link_count(sdg="SDG 3"):
    search_collection = 'linksdgs'
    search_server = 'http://solr4-jmmnn-1.c9users.io/solr/' + str(search_collection)
    s = solr.SolrConnection(search_server)
    response = s.select('*', facet='true' , facet_field=['SDG'] , rows=2 , fq='SDG:"'+sdg+'"'+"'")
    row = response.facet_counts['facet_fields']['SDG']
    result_list = []
    for val in sorted(row):
        result_list.append(row[val])
    return result_list

# use for testing
#print link_count("SDG 2") 


data = [
    link_count("SDG 1"),
    link_count("SDG 2"),
    link_count("SDG 3"),
    link_count("SDG 4"),
    link_count("SDG 5"),
    link_count("SDG 6"),
    link_count("SDG 7"),
    link_count("SDG 8"),
    link_count("SDG 9"),
    link_count("SDG 10"),
    link_count("SDG 11"),
    link_count("SDG 12"),    
    link_count("SDG 13"),
    link_count("SDG 14"),
    link_count("SDG 15"),  
    link_count("SDG 16"),
    link_count("SDG 17")
    ]
    
print data   #copy the results from the screen into the file ../static/d3_chord/matrix.json , configure the colors in the file cities.csv in that same folder.