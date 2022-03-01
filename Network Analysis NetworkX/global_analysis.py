import logging
import matplotlib.pyplot as plt
import numpy as np
from helper_functions import *

logger = logging.getLogger(__name__)

def global_analysis(G):    
    logger.info("run global analysis...")
    
    # get density of network:
    logger.info("network density: {}".format(nx.density(G)))

    #in_and out degree 
    in_degree_sequence = sorted([d for n, d in G.in_degree()], reverse=True)  # in_degree sequence    
    in_degree_count = collections.Counter(in_degree_sequence)

    
    in_deg, in_cnt = zip(*in_degree_count.items())
    logger.info("average in_degree: {}".format((sum(in_degree_sequence) / len(in_degree_sequence))))
    
    out_degree_sequence = sorted([d for n, d in G.out_degree()], reverse=True)  # out_degree sequence
    out_degree_count = collections.Counter(out_degree_sequence)
    out_deg, out_cnt = zip(*out_degree_count.items())
    logger.info("average out_degree: {}".format((sum(out_degree_sequence) / len(out_degree_sequence))))
    
    # get average shortest path length
    path_lengths = []
    for v in G.nodes():
        spl = dict(nx.single_source_shortest_path_length(G, v))
        for p in spl:
            path_lengths.append(spl[p])

    logger.info("average shortest path length: {}".format((sum(path_lengths) / len(path_lengths))))