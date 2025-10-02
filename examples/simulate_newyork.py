from src.load_data import load_airports, load_routes
from src.build_csr import build_csr_matrix
from src.epidemic import epidemic_spread
from src.visualize import animate_spread

# Load data
airports = load_airports("data/airports.dat")
routes = load_routes("data/routes.dat")

# Build adjacency matrix
A, id_to_index = build_csr_matrix(airports, routes)

# start infection at New_York 
hongkong_id = airports[airports["IATA"] == "JFK"]["AirportID"].values[0]

# Run simulation for 5 steps
spread = epidemic_spread(A, id_to_index, jfk_id, steps=5)

# Print infection counts
for step, v in enumerate(spread):
    print(f"Step {step}: {int(sum(v))} airports infected")

# Animate infection spread
animate_spread(airports, spread, id_to_index, interval=1000)

