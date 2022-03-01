import logging
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from helper_functions import *
import numpy as np

logger = logging.getLogger(__name__)

def local_analysis(G):
    logger.info("run local analysis...")
    
    # Betweenness centrality
    bet_cen = nx.betweenness_centrality(G)
    bet_cen = sort_and_small_dict(bet_cen, 5)
    # Closeness centrality
    clo_cen = nx.closeness_centrality(G)
    clo_cen = sort_and_small_dict(clo_cen, 5)
    # Degree centrality
    in_deg_cen = nx.in_degree_centrality(G)
    in_deg_cen = sort_and_small_dict(in_deg_cen, 5)
    # Degree centrality
    out_deg_cen = nx.out_degree_centrality(G)
    out_deg_cen = sort_and_small_dict(out_deg_cen, 5)
    # Page rank
    page_rank = nx.pagerank(G)
    page_rank = sort_and_small_dict(page_rank, 5)

    # print bet_cen, clo_cen, eig_cen, page_rank
    logger.info("Betweenness centrality: {}".format(bet_cen))
    logger.info("Closeness centrality: {}".format(clo_cen))
    logger.info("In-Degree centrality: {}".format(in_deg_cen))
    logger.info("Out-Degree centrality: {}".format(out_deg_cen))
    logger.info("Page rank: {}".format(page_rank))
    
    # Table summarising results
    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    data = [centrality_to_str_arr(bet_cen),
                           centrality_to_str_arr(clo_cen),
                           centrality_to_str_arr(in_deg_cen),
                           centrality_to_str_arr(out_deg_cen),
                           centrality_to_str_arr(page_rank)]        
     
    data = np.transpose(data) 
    
    table = ax.table(colLabels=['Betweenness Centrality', 'Closeness Centrality', 'In-Degree Centrality', 'Out-Degree Centrality', 'PageRank'],
                     cellText=data,
                     loc='center')
    for (row, col), cell in table.get_celld().items():
        if (row == 0) or (col == -1):
            cell.set_text_props(fontproperties=FontProperties(weight='bold'))
    fig.tight_layout()
    plt.savefig("./centrality.png", dpi=300)
    plt.show()


