import logging
import glob
import csv

logger = logging.getLogger(__name__)

def prepare_graph_data(nodes_file, relations_file):    
    """Read Nodes and Relations file and returns
    nodes_labels dictionary with key as node name/beauty entity and value as its label
    edges list with every element a list further having source and target as directed relationship
    """
    nodes_labels = dict()       
    all_nodes_files = glob.glob('./' + nodes_file + '*')   
    
        
    for n_file in all_nodes_files:
        with open(n_file, 'r', newline='\n') as nodes_file_handle:
            rows = csv.reader(nodes_file_handle, delimiter=',')
            next(rows,None) #skip the header row
            for row in rows:
                if row[0] not in nodes_labels:                
                    nodes_labels[row[0]] = row[1]  
                    
    logger.info("# of nodes: {}".format(len(nodes_labels)))
       
    edges = []    
    all_relations_files = glob.glob('./' + relations_file + '*')     
            
    for r_file in all_relations_files:
        with open(r_file, 'r', newline='\n') as rel_file_handle:
            rows = csv.reader(rel_file_handle, delimiter=',')
            next(rows,None)     #skip the header
            for row in rows:            
                edges.append([row[0], row[1]]) 
    
    logger.info("# of edges: {}".format(len(edges)))
    return (nodes_labels, edges)
    