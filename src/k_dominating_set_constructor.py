import numpy as np
import random
from typing import Set


def randomized_k_dominating_set(matrix, k: int, seed: int = None) -> Set[int]:
    # use seed if reproducibility is desired in debugging/testing
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    n = matrix.shape[0]
    max_degree = get_max_degree(matrix)
    if k > max_degree or n == 0 or k == 0:
        return set()
    p = .1
    A = set()
    for v in range(n):
        if random.random() < p:
            A.add(v)
    B = set()
    for v in range(n):
        if v not in A:
            neighbors_v = get_neighbors(matrix, v)
            neighbors_in_A = neighbors_v.intersection(A)
            if len(neighbors_in_A) < k:
                B.add(v)
    D = A.union(B)
    return D


def get_max_degree(matrix) -> int:
    degrees = np.diff(matrix.indptr)
    return int(np.max(degrees)) if len(degrees) > 0 else 0


def get_neighbors(matrix, vertex: int) -> Set[int]:
    start = matrix.indptr[vertex]
    end = matrix.indptr[vertex + 1]
    neighbors = matrix.indices[start:end]
    return set(neighbors)
