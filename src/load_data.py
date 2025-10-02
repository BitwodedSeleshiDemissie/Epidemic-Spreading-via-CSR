import pandas as pd
import numpy as np

def load_airports(file_path="data/airports.dat"):
    """Load airports dataset from OpenFlights"""
    airports = pd.read_csv(
        file_path,
        header=None,
        names=[
            "AirportID", "Name", "City", "Country", "IATA", "ICAO",
            "Lat", "Lon", "Altitude", "Timezone", "DST",
            "Tz_database_time_zone", "Type", "Source"
        ]
    )
    return airports

def load_routes(file_path="data/routes.dat"):
    """Load routes dataset from OpenFlights"""
    routes = pd.read_csv(
        file_path,
        header=None,
        names=[
            "Airline", "AirlineID", "SourceAirport", "SourceAirportID",
            "DestAirport", "DestAirportID", "Codeshare", "Stops", "Equipment"
        ]
    )

    # Replace \N with NaN
    routes.replace("\\N", np.nan, inplace=True)

    # Drop rows where IDs are missing
    routes = routes.dropna(subset=["SourceAirportID", "DestAirportID"])

    # Convert IDs to integers safely
    routes["SourceAirportID"] = routes["SourceAirportID"].astype(int)
    routes["DestAirportID"] = routes["DestAirportID"].astype(int)

    return routes

