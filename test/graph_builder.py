import numpy as np
import networkx as nx
import scipy as sp

def setup_toy_matrix(size=100, weight_mu= 5.0, weight_sigma = 5.0, p = .5):
    G = nx.erdos_renyi_graph(size, p)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.gauss(weight_mu, weight_sigma)
    return G
