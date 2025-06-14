import scipy as sp
import numpy as np

def minimize_k_dominating_set(matrix, dominating_set, k): #Assumes "matrix" is a scipy.sparse CSR matrix
    ordered_set = order_set_by_neighbours(matrix, dominating_set) #this is a list, ordered in increasing order of num. of neighbours
    for node in ordered_set:
        dominating_set.remove(node)
        if not is_dominating_set(matrix, dominating_set, k):
            dominating_set.add(node) #Add the node back
    return dominating_set

def order_set_by_neighbours(matrix, dominating_set):
    ls = [(node, num_of_neighbours(node, matrix, dominating_set)) for node in dominating_set]
    ls_sorted = sorted(ls, key=lambda x: x[1])
    return [x[0] for x in ls_sorted]

def num_of_neighbours(node, matrix, dominating_set):
    start = matrix.indptr[node]
    end = matrix.indptr[node+1] # look only at row "node" of the matrix
    neighbors = matrix.indices[start:end] #all "1" indices
    return sum(1 for neighbor in neighbors if neighbor != node and neighbor not in dominating_set)

def is_dominating_set(matrix, checked_set, k):
    for node in range(matrix.shape[0]):
        start = matrix.indptr[node]
        end = matrix.indptr[node+1]
        neighbors = matrix.indices[start:end]
        if not ( node in checked_set or sum(1 for neighbor in neighbors if neighbor in checked_set) >= k):
            return False # there is a node that is not dominated
    return True