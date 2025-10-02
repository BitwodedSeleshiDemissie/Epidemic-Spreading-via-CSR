import numpy as np
from scipy.sparse import csr_matrix

def build_csr_matrix(airports, routes):
    """
    Build CSR adjacency matrix from OpenFlights data
    """
    airport_ids = airports["AirportID"].dropna().astype(int).tolist()
    id_to_index = {aid: idx for idx, aid in enumerate(airport_ids)}
    n_airports = len(airport_ids)

    edges_src = []
    edges_dst = []

    for _, row in routes.iterrows():
        src = row["SourceAirportID"]
        dst = row["DestAirportID"]
        if src in id_to_index and dst in id_to_index:
            edges_src.append(id_to_index[src])
            edges_dst.append(id_to_index[dst])

    data = np.ones(len(edges_src), dtype=np.int8)
    A = csr_matrix((data, (edges_src, edges_dst)), shape=(n_airports, n_airports))

    return A, id_to_index

