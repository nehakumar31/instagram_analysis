# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 12:59:29 2021

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

import sys
import argparse

from global_analysis import global_analysis
from local_analysis import local_analysis
from helper_functions import *
from community_detection import community_detection

def main():    
    print("Start Argument parsing....")
    parser = argparse.ArgumentParser(description=("Arguments to start Network Analysis"))
    parser.add_argument("--nodes_file", "--nodes_file", default=None, help="File name to read node Id and label")
    parser.add_argument("--relations_file", "--relations_file", default=None, help="file name to read directed relations")
    
    args = parser.parse_args()
    if( (args.nodes_file is None) or (args.relations_file is None) ):   
            print("Nodes file and relations file is mandatory")
            parser.print_help()
            sys.exit(1)
    
    logger = logging.getLogger(__name__)
    logger.info("Instantiate graph...")
    
    G = create_graph(args.nodes_file, args.relations_file)
    logger.info("# of nodes in graph: {}".format(G.order()))
    logger.info("in-degree view of graph: {}".format(G.in_degree()))
    logger.info("out-degree view of graph: {}".format(G.out_degree()))
    
    global_analysis(G)
    local_analysis(G)
    community_detection(G)
    
    logger.info("Application exiting...")
    
    
if __name__ == '__main__':
    main()