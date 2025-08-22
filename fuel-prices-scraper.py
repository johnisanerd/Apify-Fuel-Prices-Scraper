"""
Fuel Prices Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/fuelprices?fpr=9n7kx3

This script demonstrates how to use the Fuel Prices Scraper Actor
to search fuel prices and retrieve structured search results.
"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "search": "11507",
    "fuel": 1,
    "lang": "en",
    "maxAge": 0,
    "output_file": "gas_stations.csv",
}

# Run the Actor and wait for it to finish
run = client.actor("0wi38CtP5zEKifljx").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)