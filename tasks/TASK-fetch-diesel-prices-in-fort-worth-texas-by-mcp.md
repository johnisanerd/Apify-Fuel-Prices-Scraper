# Task publish sheet: Fetch diesel prices in Fort Worth, Texas by MCP

Paste-ready values for the Apify Console Publication tab. Public copy in this sheet is clean per the
Immutable Rules (no em dash, no vendor name, no hard price, no "Scraper" identity noun).

## Parent Actor

- **Actor name:** FuelPrices API (display: FuelPrices | Pay Per Result, Easy to Use, No Cookies)
- **Store link:** https://apify.com/johnvc/fuelprices?fpr=9n7kx3
- **Repo:** /Users/johncole/Github/Apify-Fuel-Prices-Scraper
- **Username / slug:** johnvc / fuelprices

## Target keyword

`fetch diesel prices in fort worth texas`

## Display information (Publication tab)

- **Slug:** `fetch-diesel-prices-in-fort-worth-texas-by-mcp` (auto-derived from the task Title)
- **SEO task title:** `Fetch diesel prices in Fort Worth, Texas by MCP` (47/60)
- **SEO description:** `Fetch live diesel prices in Fort Worth, Texas via the MCP server for AI assistants: station, address, distance, and prices. Pay per result.` (139/160)

Final public URL: `https://apify.com/johnvc/fuelprices/examples/fetch-diesel-prices-in-fort-worth-texas-by-mcp?fpr=9n7kx3`

## Input (visible fields)

The task runs with its full input config; the fields below are the ones shown on the landing page.

| Field (property name) | Value | Visible? |
|-----------------------|-------|----------|
| search                | Fort Worth, TX | yes |
| fuel                  | 4 (Diesel) | yes |
| lang                  | en | no (noise) |

Secrets confirmed `isSecret` in the Actor schema: none present (no credential-shaped fields).

## Dataset schema

- **View chosen:** `Overview`
- **Why it matches the description:** Overview exposes ID, Station, Address, City, State, ZIP,
  Distance (mi), Price Unit, Cash Price, Cash Posted, Credit Price, Credit Posted, Ratings, and Stars,
  which covers the promised station, address, distance, and prices.

## Test run + publish status

- **Run status:** Succeeded (run TJYXCWUvVgiiveo65), Fort Worth stations returned
- **Verified output matches description:** yes. Every row resolved to address_locality "Fort Worth" and
  prices are in the diesel band, confirming fuel 4 took effect. Sample: Walmart Neighborhood Market,
  5301 Sycamore School Rd, credit 4.83; Stop & Save #3, 3301 White Settlement Rd, credit 4.79
- **Actor ID:** 0wi38CtP5zEKifljx
- **Task ID:** Wl4lEo2g54G3VHTSF
- **Published:** pending
- **Landing page:** https://apify.com/johnvc/fuelprices/examples/fetch-diesel-prices-in-fort-worth-texas-by-mcp?fpr=9n7kx3
- **AI-readable (.md):** same URL + .md

## Internal notes (NOT public)

- Upstream source: crowd-reported US gas station price data (see actor source repo). Keep generic in
  public copy.
- Created 2026-08-03 to complete the Fort Worth pair. Every other city in the series ships a gas
  `-by-api` page and a diesel `-by-mcp` page; Fort Worth had only the gas half.
- `fuel: 4` is Diesel per the Actor input schema (1=Regular, 2=Midgrade, 3=Premium, 4=Diesel, 5=E85,
  12=Unleaded88). Seven published diesel pages in this series were sending fuel 1 and were corrected
  on 2026-08-03; this one was built correct from the start.

Last Updated: 2026.08.03
