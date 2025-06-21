import numpy as np
import networkx as nx
import scipy as sp
import random


def setup_toy_matrix(size=100, min_weight=1.0, max_weight=10.0, p=.3):
    G = nx.erdos_renyi_graph(size, p)
    for (u, v) in G.edges():
        G[u][v]['length'] = random.uniform(min_weight, max_weight)
    return G

def setup_reachability_graph(G, t=2.0):
    distances = dict(nx.all_pairs_dijkstra_path_length(G, weight='length'))
    reachability_graph = nx.Graph()
    reachability_graph.add_nodes_from(G.nodes())
    
    nodes = list(G.nodes())
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i < j:
                try:
                    if distances[u][v] <= t:
                        reachability_graph.add_edge(u, v)
                except KeyError:
                    pass
    # return nx.to_scipy_sparse_matrix(reachability_graph, format = 'coo')
    return nx.to_scipy_sparse_matrix(reachability_graph, format='csr') #Good for "squeezing" a row to only it's 1 indices

if __name__ == "__main__":
    G = setup_toy_matrix()
    print(G)
    RG = setup_reachability_graph(G)
    print(RG)