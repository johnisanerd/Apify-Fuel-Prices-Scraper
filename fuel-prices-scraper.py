"""
Fuel Prices API: A Quick Start Example
See more at: https://apify.com/johnvc/fuelprices?fpr=9n7kx3
Input schema: https://apify.com/johnvc/fuelprices/input-schema?fpr=9n7kx3

This script shows how to call the Fuel Prices API on Apify from Python and read its
structured JSON output. It exercises the input parameters so you can see what is
configurable, while keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Billing is per result returned, so a single location keeps this first run cheap.
# Raise the scope once you have your own API key and know your budget.
run_input = {
    "search": "11507",   # ZIP code, city name, or "lat, lng" coordinates
    "fuel": 1,           # 1=Regular, 2=Midgrade, 3=Premium, 4=Diesel, 5=E85, 12=Unleaded88
    "lang": "en",        # only English is currently supported
    "maxAge": 0,         # max data age in days; 0 = freshest available
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/fuelprices").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset (one station per item)
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} station(s).\n")

# Show a few key fields from each station.
for item in items[:10]:
    location = f"{item.get('address_locality')}, {item.get('address_region')}"
    print(
        f"{item.get('name')}  |  {location}  |  "
        f"cash={item.get('price_cash')} credit={item.get('price_credit')} {item.get('priceUnit')}  |  "
        f"{item.get('distance')} mi"
    )
