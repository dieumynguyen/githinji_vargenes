import numpy as np

def check_symmetric(A, tol=1e-8):
    return np.allclose(A, A.T, atol=tol)

def generate_adjaceny_list(N=100, factor=1.01, add_weight=False, random_weight=True):

    # Adjaceny Matrix
    A_matrix = np.floor(np.random.uniform(size=(N, N)) * factor)
    A_matrix = A_matrix + A_matrix.T
    A_matrix[A_matrix > 0] = 1

    if check_symmetric(A_matrix):
        # Get upper triangle
        # See https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.triu_indices.html
        # This avoids double counts
        A_matrix[np.tril_indices(N)] = 0

    A_list = []
    for row_i in range(A_matrix.shape[0]):
        for col_i in range(A_matrix.shape[1]):
            if A_matrix[row_i][col_i] > 0:
                if add_weight:
                    link_weight = np.abs(np.random.normal(0, 2)) if random_weight else 1
                    new_row = [row_i, col_i, link_weight]
                else:
                    new_row = [row_i, col_i]
                    
                A_list.append(new_row)

    return A_list
