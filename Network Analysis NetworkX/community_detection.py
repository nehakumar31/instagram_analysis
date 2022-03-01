import logging
from helper_functions import *
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def set_node_community(G, communities):
    """"assign community to nodes as attribute"""
    for c, v_c in enumerate(communities):
        for v in v_c:
            # Add 1 to save 0 for external edges(connecting one community to another)
            G.nodes[v]['community'] = c + 1

def set_edge_community(G):
    """Find internal edges and add their community as an attribute"""
    for v, w, in G.edges:
        if G.nodes[v]['community'] == G.nodes[w]['community']:
            # Internal edge, mark with community
            G.edges[v, w]['community'] = G.nodes[v]['community']
        else:
            # External edge, mark as 0
            G.edges[v, w]['community'] = 0
            
def get_color(i, r_off=1, g_off=1, b_off=1):    
        """"Assign a color to a node based on i - its community index"""
        r0, g0, b0 = 0, 0, 0
        n = 16
        low, high = 0.1, 0.9
        span = high - low
        r = low + span * (((i + r_off) * 3) % n) / (n - 1)
        g = low + span * (((i + g_off) * 5) % n) / (n - 1)
        b = low + span * (((i + b_off) * 7) % n) / (n - 1)
        return (r, g, b)
            
def get_nodes_color(G):   
    """Get color of all the nodes in a list"""
    nodes_color = []
    for v in G.nodes:
        community_idx = G.nodes[v]['community']
        nodes_color.append(get_color(community_idx))
        
    return nodes_color  


def community_detection(G): 
    logger.info("run community detection...")
    communities_generator = nx.algorithms.community.girvan_newman(G)
    communities_newman = next(communities_generator)
    
    logger.info("Partition Girvan-Newman {} clusters detected".format(len(communities_newman)))
    
    # modularity score     
    logger.info("Modularity score Girvan-Newman method: ".format(round(nx.algorithms.community.modularity(G, communities_newman), 2)))
    
    logger.info("Assign communities to nodes")
    set_node_community(G, communities_newman)
    
    logger.info("Assign communities to edges")
    set_edge_community(G)
    nodes_color = get_nodes_color(G)
    
    external_edges = [(v, w) for v, w in G.edges if G.edges[v, w]['community'] == 0]
    internal_edges = [(v, w) for v, w in G.edges if G.edges[v, w]['community'] > 0]
    
    internal_edges_color = ['black' for e in internal_edges]
    
    #node_labels = nx.get_node_attributes(G, "label")
    
    G_pos = nx.spring_layout(G)
    
    logger.info("Construct network with communities")
    #draw nodes and external edges
    #nx.draw_networkx(G, pos=G_pos, node_size=0, edgelist=external_edges, edge_color="silver")
    nx.draw_networkx(G, pos=G_pos, node_color=nodes_color, edgelist=external_edges, 
                     edge_color="silver", with_labels=False)
    
    # Draw nodes and internal edges
    nx.draw_networkx(G, pos=G_pos, node_color=nodes_color, edgelist=internal_edges, 
                     edge_color=internal_edges_color, with_labels=False)
        
    plt.savefig('./network.png')
    
    #export the network to a gephi file 
    nx.write_gexf(G, 'insta_network.gexf')



