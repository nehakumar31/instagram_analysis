# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 12:59:29 2022

@author: nehkumar
"""

#import os
import logging
import logging.config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("network_analysis.log"),
        logging.StreamHandler()
    ]
)

import argparse

from InstagramNetwork import InstagramNetwork
from Helper import *

def main():    
    print("Argument parsing....")
    parser = argparse.ArgumentParser(description=("Arguments to persist and analyse Instagram beauty entities"))   
    parser.add_argument("--host", "--host", default=None, help="host to connect neo4j server")
    parser.add_argument("--username", "--username", default=None, help="username to connect to graph database")
    parser.add_argument("--password", "--password", default=None, help="password to connect to graph database")
    parser.add_argument("--nodes-file", "--nodes_file", default=None, help="file to read nodes Id and label")
    parser.add_argument("--relations-file", "--relations_file", default=None, help="file to read relations between a beauty entity and its suggested account")
    
    args = parser.parse_args()
    
    if args.username is None or args.password is None:
        print("username and password is mandatory to connect to Neo4j")
        parser.print_help()
        sys.exit(1)
        
    if args.nodes_file is None or args.relations_file is None:
        print("Nodes and Relations file is mandatory to prepare graph data")
        parser.print_help()
        sys.exit(1)
        
    logger = logging.getLogger(__name__)
        
    logger.info("Start processing...")       
    try:                
        (nodes, edges) = prepare_graph_data(args.nodes_file, args.relations_file)
        insta_network = InstagramNetwork(args)
        insta_network.populate_nodes(nodes)
        insta_network.populate_edges(edges)
                 
    except Exception as exc:
        logger.error("Exception: {}".format(exc))
        
    logger.info("Application exiting...")    
    
if __name__ == '__main__':
    main()