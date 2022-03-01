import logging
import networkx as nx
import collections
import csv
import glob
import pprint

logger = logging.getLogger(__name__)

def sort_and_small_dict(d, n):
    sorted_dict = collections.OrderedDict(sorted(d.items(), key=lambda x: -x[1]))
    firstnpairs = list(sorted_dict.items())[:n]
    return firstnpairs


def centrality_to_str_arr(centrality):
    """helper function to convert entries as (spehora, 0.05) to sephora|0.05"""
    str_arr = []
    for item in centrality:
        str_arr.append(item[0] + ' | ' + str(round(item[1], 2)))
    return str_arr

def create_graph(nodes_file, relations_file):
    logger.info("Create a directed graph...")
    nodes_labels = dict()
    G = nx.DiGraph()
    
    all_nodes_files = glob.glob('./' + nodes_file + '*')     
    for n_file in all_nodes_files:
        with open(n_file, 'r', newline='\n') as nodes_file_handle:
            rows = csv.reader(nodes_file_handle, delimiter=',')
            next(rows,None) #skip the header row
            for row in rows:
                if row[0] not in nodes_labels:                
                    nodes_labels[row[0]] = row[1] 
        
    
    logger.info("Adding {} nodes to the graph".format(len(nodes_labels)))
        
    for node, label in nodes_labels.items():
       G.add_node(node, label=label)        
       
    edges = []    
    all_relations_files = glob.glob('./' + relations_file + '*')    
    
    for r_file in all_relations_files:
        with open(r_file, 'r', newline='\n') as rel_file_handle:
            rows = csv.reader(rel_file_handle, delimiter=',')
            next(rows,None)     #skip the header
            for row in rows:            
                edges.append([row[0], row[1]])    
    
    logger.info("Adding {} edges to the graph".format(len(edges)))
    for edge in edges:
        G.add_edge(edge[0], edge[1])

    return G