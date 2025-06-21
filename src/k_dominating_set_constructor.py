import numpy as np
import random
from typing import Set


def randomized_k_dominating_set(matrix, k: int, delta_prime: float = 0.1, seed: int = None) -> Set[int]:
    dominating_set = construct_initial_dominating_set(
        matrix, k, delta_prime, seed
    )
    return dominating_set


def construct_initial_dominating_set(matrix, k: int, delta_prime: float = 0.1, seed: int = None) -> Set[int]:
    # use seed if reproducibility is desired in debugging/testing
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    
    n = matrix.shape[0]
    if n == 0:
        return set()
    max_degree = get_max_degree(matrix)
    if k > max_degree:
        k = max_degree
    if k == 0:
        return set()
    p = calculate_selection_probability(max_degree, k, delta_prime)
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


def compute_binomial_coefficient(n: int, k: int) -> int:
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    prev_row = [0] * (k + 1)
    prev_row[0] = 1
    for i in range(1, n + 1):
        curr_row = [0] * (k + 1)
        curr_row[0] = 1
        for j in range(1, min(i + 1, k + 1)):
            curr_row[j] = prev_row[j] + (prev_row[j-1] if j-1 >= 0 else 0)
        prev_row = curr_row
    return prev_row[k]


def calculate_selection_probability(max_degree: int, k: int, delta_prime: float = 0.1) -> float:
    if k == 0 or max_degree == 0:
        return 0.5
    binomial_coeff = compute_binomial_coefficient(max_degree, k - 1)
    if binomial_coeff == 0:
        return 0.5
    p_prime = 1.0 / (max_degree * binomial_coeff * (1 + delta_prime))
    p = 1 - p_prime
    return max(0.0, min(1.0, p))


def get_max_degree(matrix) -> int:
    degrees = np.diff(matrix.indptr)
    return int(np.max(degrees)) if len(degrees) > 0 else 0


def get_neighbors(matrix, vertex: int) -> Set[int]:
    start = matrix.indptr[vertex]
    end = matrix.indptr[vertex + 1]
    neighbors = matrix.indices[start:end]
    return set(neighbors)