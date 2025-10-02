import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_infected_airports(airports, infection_vector, id_to_index, title="Infection Spread"):
    """
    Plot infected airports on a scatter plot using Lat/Lon.
    """
    index_to_id = {v: k for k, v in id_to_index.items()}

    infected_indices = [i for i, val in enumerate(infection_vector) if val > 0]
    infected_ids = [index_to_id[i] for i in infected_indices]
    infected_airports = airports[airports["AirportID"].isin(infected_ids)]

    plt.figure(figsize=(12, 6))
    plt.scatter(
        airports["Lon"], airports["Lat"],
        c="lightgray", s=10, alpha=0.5, label="Healthy Airports"
    )

    if not infected_airports.empty:
        plt.scatter(
            infected_airports["Lon"], infected_airports["Lat"],
            c="red", s=30, alpha=0.8, label="Infected Airports"
        )

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title(title)
    plt.legend()
    plt.show()


def animate_spread(airports, spread_results, id_to_index, interval=1000, save_path="infection.gif"):
    """
    Animate infection spread across airports step by step and save as GIF.
    
    airports: DataFrame of airports
    spread_results: list of infection vectors from epidemic_spread()
    id_to_index: dict mapping AirportID -> index
    interval: delay between frames in ms
    save_path: filename to save animation (e.g., 'infection.gif')
    """
    index_to_id = {v: k for k, v in id_to_index.items()}

    fig, ax = plt.subplots(figsize=(12, 6))

    # plot background
    ax.scatter(
        airports["Lon"], airports["Lat"],
        c="lightgray", s=10, alpha=0.5, label="Healthy Airports"
    )
    infected_scatter = ax.scatter([], [], c="red", s=30, alpha=0.8, label="Infected Airports")

    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("Epidemic Spread Simulation")
    ax.legend()

    def update(frame):
        v = spread_results[frame]
        infected_indices = [i for i, val in enumerate(v) if val > 0]
        infected_ids = [index_to_id[i] for i in infected_indices]
        infected_airports = airports[airports["AirportID"].isin(infected_ids)]
        infected_scatter.set_offsets(infected_airports[["Lon", "Lat"]].values)
        ax.set_title(f"Epidemic Spread - Step {frame}")
        return infected_scatter,

    anim = FuncAnimation(fig, update, frames=len(spread_results), interval=interval, repeat=False)

    # Save as GIF instead of showing (works in headless environments)
    anim.save(save_path, writer="pillow")
    print(f"Animation saved as {save_path}")

    return anim

