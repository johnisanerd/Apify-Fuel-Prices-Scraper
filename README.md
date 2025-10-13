https://apify.com/johnvc/fuelprices?fpr=9n7kx3

# 🚀 Fuel Prices Scraper

> **The most efficient, reliable, and developer-friendly Fuel Prices scraper**

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- An Apify account and API key

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Apify-Fuel-Prices-Scraper
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Using venv (Python 3.3+)
   python -m venv venv
   
   # Activate the virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Install from requirements.txt
   pip install -r requirements.txt

   ```

4. **Configure your API key**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Apify API key
   # Get your API key from: https://apify.com?fpr=9n7kx3
   ```

5. **Run the example**
   ```bash
   python fuel-prices-scraper.py
   ```

### Alternative: Direct API Key Usage
If you prefer not to use a `.env` file, you can set the environment variable directly:
```bash
export APIFY_API_TOKEN="your_api_key_here"
python fuel-prices-scraper.py
```

# Fuel Price Scraper

**Real-time gas station prices and details by ZIP, city, or place name.**

Get current prices and station metadata from data source using a simple, reliable Actor. Designed for quick setup, robust scraping, and clean outputs for analysis or downstream automation.

The coverage of this app is mostly in the United States, but does include some international locations such as Canada.

### What this Actor does
- **Scrapes live prices** for a location and fuel type
- **Returns clean station data** (name, address, distance, ratings, cash/credit prices, timestamps)
- **Exports CSV automatically** with an optional custom filename

Common use cases:
- **Price monitoring** across cities/ZIP codes
- **Competitive analysis** for fuel retail
- **Data pipelines** feeding dashboards or alerts

### Features
- **Simple input**: just provide `search` (ZIP/city).  This is the only mandatory input required.
- **Fuel selection**: `fuel` numeric code (see Inputs).  This is optional, but the default will be "1" (Regular Gasoline).
- **Freshness control**: `maxAge` in days.  This is optional, but the default will be "0" (any age).
- **Localized badges/text**: `lang`.  This is optional, but the default will be "en" (English).
- **CSV export**: set `output_file`, or we generate a timestamped name.  This is optional, but the default will be a timestamped name.

### Quick start
1) Add the Actor to your Apify account and open it.
2) Provide minimal input and run.

Example minimal input:
```json
{
  "search": "11507"
}
```

Example with options:
```json
{
  "search": "New York, NY",
  "fuel": 1,
  "lang": "en",
  "maxAge": 0,
  "output_file": "stations_nyc.csv"
}
```

### Input parameters
- **search** (string, required): Location query such as ZIP, city, or free text (e.g., "11507", "Los Angeles").
- **fuel** (integer, optional, default: 1): Fuel type code. Current mapping in this Actor UI is: 1 = Regular, 2 = Midgrade, 3 = Premium.
- **lang** (string, optional, default: "en"): Language code for localized fields.
- **maxAge** (integer, optional, default: 0): Maximum age of price data in days. Use 0 for the freshest data available.
- **output_file** (string, optional): Custom CSV filename. If omitted, a timestamped filename is auto-generated (e.g., `gas_stations_11507_2025-08-19_11-01-12_1.csv`).

### Output
Results are stored in the Actor dataset and a CSV file is written to the run storage. The dataset schema includes the following key fields:

- `id`, `name`, `distance`, `priceUnit`, `ratingsCount`, `starRating`
- Address: `address_line1`, `address_line2`, `address_locality`, `address_region`, `address_postalCode`
- Prices: `price_cash`, `price_cash_postedTime`, `price_credit`, `price_credit_postedTime`

Sample dataset item:
```json
{
  "id": 123456,
  "name": "USA",
  "distance": 1.2,
  "priceUnit": "USD/GAL",
  "ratingsCount": 65,
  "starRating": 4.5,
  "address_line1": "222-33 Braddock Ave",
  "address_line2": null,
  "address_locality": "Queens Village",
  "address_region": "NY",
  "address_postalCode": "11428",
  "price_cash": 2.85,
  "price_cash_postedTime": "2025-08-19T10:58:00Z",
  "price_credit": 2.95,
  "price_credit_postedTime": "2025-08-19T10:58:00Z"
}
```

CSV export
- A CSV is always written. Control the name via `output_file`, otherwise a timestamped default is used.
- Columns include: `id,name,distance,priceUnit,ratingsCount,starRating,address_line1,address_line2,address_locality,address_region,address_postalCode,price_credit,price_credit_postedTime,price_cash,price_cash_postedTime`.

### Support
- First, check your run logs in the **Apify Console** for diagnostics.  
- If you need help, open a discussion and we will try to respond as quickly as possible.  Please include your run ID so we can quickly review the issue.

### Roadmap
1. Brand filtering:  Search by brand or filter by brand name.
2. More fuel types and payment filters:  Add more fuel types and payment filters.
3. Price freshness filters by hours:  Add a freshness filter by hours.
4. Alerts and notifications:  Add alerts and notifications.
5. Search by distance:  Search by distance.
6. Business metadata:  Business metadata.
- category (e.g., gas station vs. convenience store)
- website URL, phone number
- opening hours
- neighborhood field
- Geo data
- latitude/longitude fields
- operational status and ads
- “temporarily closed” / “permanently closed”
- “is advertisement” flag
- reviews and media
- review distribution (1–5 stars breakdown)
- individual reviews
- station images
7. Output formats:  explicitly export Excel (XLSX) or HTML; we write CSV and dataset items (JSON via Apify dataset export)
8. Provenance: explicit “scrape timestamp” and “search query used” fields in each record (only price postedTime from source, not scrape time)

[**Made with ❤️**](https://apify.com/johnvc?fpr=9n7kx3)

*Transform your search automation with the most reliable and efficient Fuel and Gasoline price scraper available.*
Last Updated: 2025.10.13
