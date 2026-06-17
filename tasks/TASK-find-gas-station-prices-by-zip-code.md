# Task publish sheet: Find gas station prices by ZIP code

Paste-ready values for the Apify Console Publication tab. Public copy in this sheet is clean per the
Immutable Rules (no em dash, no vendor name, no hard price, no "Scraper" identity noun).

## Parent Actor

- **Actor name:** FuelPrices API (display: FuelPrices | Pay Per Result, Easy to Use, No Cookies)
- **Store link:** https://apify.com/johnvc/fuelprices?fpr=9n7kx3
- **Repo:** /Users/johncole/Github/Apify-Fuel-Prices-Scraper
- **Username / slug:** johnvc / fuelprices

## Target keyword

`gas prices by zip code`

## Display information (Publication tab)

- **Slug:** `find-gas-station-prices-by-zip-code` (auto-derived from the task Title)
- **SEO task title:** `Find gas station prices by ZIP code` (35/60)
- **SEO description:** `Find gas station prices for any US ZIP code. Get station name, address, distance, cash and credit prices, and ratings. Pay only for results.` (140/160)

Final public URL: `https://apify.com/johnvc/fuelprices/examples/find-gas-station-prices-by-zip-code?fpr=9n7kx3`

## Input (visible fields)

The task runs with its full input config; the fields below are the ones shown on the landing page.

| Field (property name) | Value | Visible? |
|-----------------------|-------|----------|
| search                | 11507 | yes |
| fuel                  | 4 (Diesel) | yes |
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

- **Run status:** Succeeded, "Actor succeeded with 3 results in the dataset" (Albertson NY 11507 diesel: BP, Sunoco, CITGO)
- **Verified output matches description:** yes, name/address/city/state/ZIP/priceUnit/price_cash/price_credit present
- **Actor ID:** 0wi38CtP5zEKifljx
- **Task ID:** So4z4V0mKbZ6YpkDo
- **Published:** pending
- **Landing page:** https://apify.com/johnvc/fuelprices/examples/find-gas-station-prices-by-zip-code?fpr=9n7kx3
- **AI-readable (.md):** same URL + .md

## Internal notes (NOT public)

- Upstream source: crowd-reported US gas station price data (see actor source repo). Keep generic in public copy.
- Fuel type is Diesel (4) to vary coverage across the three fuelprices tasks (city Regular / GPS Premium / ZIP Diesel). Diesel returns fewer stations per ZIP, which is expected.

Last Updated: 2026.06.10
