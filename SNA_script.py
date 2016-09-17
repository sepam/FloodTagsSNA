import csv
from igraph import *
import pandas as pd


# function that generates four lists of network features
def generate_influencers():

    # open up the csv and convert it into a graph object
    # reader = csv.DictReader(open('edges2.csv'), dialect='excel')
    reader = csv.DictReader(open('edge_list.csv'), dialect='excel')
    g = Graph.DictList(edges=reader, vertices=None, directed=True)

    # calculate in-degree
    in_degree = g.degree(type='in')
    g.vs['in-degree'] = in_degree

    # calculate out-degree
    out_degree = g.degree(type='out')
    g.vs['out-degree'] = out_degree

    # calculate betweenness
    btw_score = g.betweenness()
    g.vs['betweenness'] = btw_score

    # calculate page rank
    pr_score = g.pagerank()
    g.vs['page_rank'] = pr_score

    # to put everything into a pandas dataframe gather the different columns
    series = pd.Series(g.vs['name'])
    df1 = pd.DataFrame(series, columns=['name'])
    df1['indegree'] = g.vs['in-degree']
    df1['outdegree'] = g.vs['out-degree']
    df1['pagerank'] = g.vs['page_rank']
    df1['betweenness'] = g.vs['betweenness']

    # sorting the dataframe to different columns and selecting the top 10 rows, and writing it to a csv file
    top_indegree = df1[['name', 'indegree']].sort_values(by='indegree', ascending=False)
    top_indegree[0:50].to_csv('top_indegree.csv', index=None)
    top_50_indegree = top_indegree[0:50]

    top_outdegree = df1[['name', 'outdegree']].sort_values(by='outdegree', ascending=False)
    top_outdegree[0:50].to_csv('top_outdegree.csv', index=None)
    top_50_outdegree = top_outdegree[0:50]

    top_pagerank = df1[['name', 'pagerank']].sort_values(by='pagerank', ascending=False)
    top_pagerank[0:50].to_csv('top_pagerank.csv', index=None)
    top_50_pagerank = top_pagerank[0:50]

    top_betweenness = df1[['name', 'betweenness']].sort_values(by='betweenness', ascending=False)
    top_betweenness[0:50].to_csv('top_betweenness.csv', index=None)
    top_50_betweenness = top_betweenness[0:50]

    print(top_50_indegree)
    print(top_50_outdegree)
    print(top_50_pagerank)

    return top_50_betweenness

# PRINTS OUT THE EDGELIST OF A GRAPH OBJECT OF VERTEX ID TO VERTEX ID
# print(g.get_edgelist())
# SAVE GRAPH OBJECT TO SPECIFIC GRAPH FILE FORMAT, TO BE USED IN GEPHI FOR EXAMPLE
# save(g, "trial.graphml")
# GET THE ID OF AN EDGE GIVEN TWO NODES
# specific_edge_id = g.get_eid('sagalajoel', 'iyussitumorang')
# print(specific_edge_id)
# GET THE ATTRIBUTES OF A SPECIFIC VERTEX
# g.vs.attributes()
# g.vs[0].attributes()
# GET THE ATTRIBUTES OF A SPECIFIC EDGE
# g.es[0].attributes()
# SET THE ATTRIBUTE OF A SPECIFIC VERTEX OR EDGE
# g.es[0]["is_formal"] = True
# PRINT OUT ALL THE NAMES OF A LIST OF VERTICES IN THE GRAPH
# for i in range(len(g.vs)):
#     print(g.vs[i]['name'])
# GET THE INDEGREE AND OUTDEGREE FOR ALL OBJECTS, OR SPECIFIC VERTEX IDS OR LIST OF IDS
# g.degree(6)
# g.degree[2,3,4])
# g.degree(type="in")
# g.degree(type="out")
