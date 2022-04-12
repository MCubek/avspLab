import math
from decimal import Decimal, ROUND_HALF_UP

import numpy as np


def format_num(x):
    return Decimal(Decimal(x).quantize(Decimal('.001'), rounding=ROUND_HALF_UP))


def main():
    line = input()

    N, M = list(int(x) for x in line.split(' '))

    matrix_source = read_matrix(M, N)

    matrix_item_item = matrix_source
    matrix_user_user = matrix_source.T

    matrix_item_item_norm = matrix_item_item - np.nanmean(matrix_item_item, axis=1)
    matrix_user_user_norm = matrix_user_user - np.nanmean(matrix_user_user, axis=1)

    Q = int(input())
    assert 1 <= Q <= 100

    queries = read_queries(M, N, Q)

    for query in queries:
        I, J, T, K = query
        item_item = T == 0

        matrix = matrix_item_item_norm if item_item else matrix_user_user_norm

        handleQuery(matrix, matrix_source, I, J, item_item, K)


def handleQuery(matrix_norm, matrix_source, I, J, item_item, K):
    if not item_item:
        I, J = J, I

    similarities = []
    first = matrix_norm[I, :]
    for i in range(matrix_norm.shape[0]):
        second = matrix_norm[i, :]
        similarities.append(corr_coeff(first, second))

    top = []
    for i, simmilarity in enumerate(similarities):
        if simmilarity < 0:
            continue
        elif i == I:
            continue

        value = matrix_source[i, J]
        if math.isnan(value):
            continue

        top.append((value, simmilarity))

    top_limit = len(top) if len(top) < K else K

    top.sort(reverse=True, key=lambda x: x[1])
    top = top[0:top_limit]

    score = predict_value(top)

    print(format_num(score))


def predict_value(top):
    a = 0
    b = 0
    for weight, sim in top:
        a += weight * sim
        b += sim
    return a / b


def corr_coeff(A, B):
    difference = ~np.logical_or(np.isnan(A), np.isnan(B))
    a_same = np.compress(difference, A)
    b_same = np.compress(difference, B)

    A_mA = A[np.logical_not(np.isnan(A))]
    B_mB = B[np.logical_not(np.isnan(B))]

    ssA = (A_mA ** 2).sum()
    ssB = (B_mB ** 2).sum()

    return np.dot(a_same, b_same.T) / np.sqrt(ssA * ssB)


def read_matrix(M, N):
    matrix = np.empty(shape=(N, M))
    for i in range(N):
        matrix[i, :] = list(float(x) for x in input().replace('X', 'nan').split(' '))

    return matrix


def read_queries(M, N, Q):
    queries = []
    for i in range(Q):
        query = list(int(x) for x in input().split(' '))  # I, J, T, K
        assert 1 <= query[0] <= N  # I
        assert 1 <= query[1] <= M  # J
        assert query[2] == 1 or query[2] == 0  # T
        assert 1 <= query[3] <= N and query[3] <= M  # K

        I, J, T, K = query

        queries.append((I - 1, J - 1, T, K))
    return queries


if __name__ == '__main__':
    main()
