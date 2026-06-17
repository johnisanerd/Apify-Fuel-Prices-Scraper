# Task publish sheet: Find gas prices near GPS map coordinates

Paste-ready values for the Apify Console Publication tab. Public copy in this sheet is clean per the
Immutable Rules (no em dash, no vendor name, no hard price, no "Scraper" identity noun).

## Parent Actor

- **Actor name:** FuelPrices API (display: FuelPrices | Pay Per Result, Easy to Use, No Cookies)
- **Store link:** https://apify.com/johnvc/fuelprices?fpr=9n7kx3
- **Repo:** /Users/johncole/Github/Apify-Fuel-Prices-Scraper
- **Username / slug:** johnvc / fuelprices

## Target keyword

`gas prices near coordinates`

## Display information (Publication tab)

- **Slug:** `find-gas-prices-near-gps-map-coordinates` (auto-derived from the task Title)
- **SEO task title:** `Find gas prices near GPS map coordinates` (40/60)
- **SEO description:** `Find gas station prices near any GPS coordinates. Get station name, address, distance, cash and credit prices, and ratings. Pay only for results.` (145/160)

Final public URL: `https://apify.com/johnvc/fuelprices/examples/find-gas-prices-near-gps-map-coordinates?fpr=9n7kx3`

## Input (visible fields)

The task runs with its full input config; the fields below are the ones shown on the landing page.

| Field (property name) | Value | Visible? |
|-----------------------|-------|----------|
| search                | 36.0816642, -115.0534345 | yes |
| fuel                  | 3 (Premium) | yes |
| lang                  | en | no (noise) |
| maxAge                | 0 | no (noise) |
| output_file           | (unset) | no (noise) |

Secrets confirmed `isSecret` in the Actor schema: none present (no credential-shaped fields).

## Dataset schema

- **View chosen:** `Overview`
- **Why it matches the description:** Overview exposes ID, Station, Address, City, State, ZIP,
  Distance (mi), Price Unit, Cash Price, Cash Posted, Credit Price, Credit Posted, Ratings, and Stars.
  These line up with the promised output: station name, full address, distance, cash and credit prices,
  and ratings.

## Test run + publish status

- **Run status:** Succeeded, "Actor succeeded with 20 results in the dataset" (Las Vegas-area stations, e.g. Henderson NV)
- **Verified output matches description:** yes, name/address/city/state/ZIP/distance/priceUnit/price_cash/price_credit/ratings present
- **Actor ID:** 0wi38CtP5zEKifljx
- **Task ID:** aJmdSn3stZ6sPmER0
- **Published:** pending
- **Landing page:** https://apify.com/johnvc/fuelprices/examples/find-gas-prices-near-gps-map-coordinates?fpr=9n7kx3
- **AI-readable (.md):** same URL + .md

## Internal notes (NOT public)

- Upstream source: crowd-reported US gas station price data (see actor source repo). Keep generic in public copy.
- Coordinate used is the schema's example point (Las Vegas, NV). Second of three fuelprices tasks (city / GPS / ZIP).

Last Updated: 2026.06.10
