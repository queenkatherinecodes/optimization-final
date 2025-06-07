import numpy as np
import networkx as nx
import scipy as sp
import random


def setup_toy_matrix(size=100, weight_mu= 5.0, weight_sigma = 5.0, p = .5):
    G = nx.erdos_renyi_graph(size, p)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.gauss(weight_mu, weight_sigma)
    return G


if __name__ == "__main__":
    G = setup_toy_matrix(10)
    print(G)
    print("=== Adjacency List ===")
    for node in G.adjacency():
        print(node)

    print("=== Degree View ===")
    print(dict(G.degree()))

    print("=== Edges with Weights ===")
    for u, v, data in G.edges(data=True):
        print(f"({u}, {v}): {data}")