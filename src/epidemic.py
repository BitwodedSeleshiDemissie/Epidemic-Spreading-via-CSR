import numpy as np

def epidemic_spread(A, id_to_index, start_airport, steps=5):
    """
    Simulate epidemic spread across airports.
    A: CSR adjacency matrix
    id_to_index: map from AirportID to matrix index
    start_airport: AirportID where infection starts
    steps: number of propagation steps
    """
    v = np.zeros(A.shape[0])
    v[id_to_index[start_airport]] = 1  # infection starts here

    results = [v.copy()]

    for _ in range(steps):
        v = A.dot(v)            # CSR matrix-vector multiplication
        v = np.where(v > 0, 1, 0)  # infected = 1
        results.append(v.copy())

    return results

