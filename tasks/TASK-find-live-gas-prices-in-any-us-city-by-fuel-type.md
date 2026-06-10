# Task publish sheet: Find live gas prices in any US city by fuel type

Paste-ready values for the Apify Console Publication tab. Public copy in this sheet is clean per the
Immutable Rules (no em dash, no vendor name, no hard price, no "Scraper" identity noun).

## Parent Actor

- **Actor name:** FuelPrices API (display: FuelPrices | Pay Per Result, Easy to Use, No Cookies)
- **Store link:** https://apify.com/johnvc/fuelprices?fpr=9n7kx3
- **Repo:** /Users/johncole/Github/Apify-Fuel-Prices-Scraper
- **Username / slug:** johnvc / fuelprices

## Target keyword

`gas prices by city`

## Display information (Publication tab)

- **Slug:** `find-live-gas-prices-in-any-us-city-by-fuel-type` (auto-derived from the task Title)
- **SEO task title:** `Find live gas prices in any US city by fuel type` (48/60)
- **SEO description:** `Find live gas station prices in any US city. Get station name, address, distance, cash and credit prices, and ratings. Pay only for results.` (140/160)

Final public URL: `https://apify.com/johnvc/fuelprices/examples/find-live-gas-prices-in-any-us-city-by-fuel-type?fpr=9n7kx3`

## Input (visible fields)

The task runs with its full input config; the fields below are the ones shown on the landing page.

| Field (property name) | Value | Visible? |
|-----------------------|-------|----------|
| search                | Houston, TX | yes |
| fuel                  | 1 (Regular) | yes |
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

- **Run status:** Succeeded, "Actor succeeded with 20 results in the dataset" (Houston-area stations, e.g. Cypress TX 77433)
- **Verified output matches description:** yes, name/address/city/state/ZIP/distance/priceUnit/price_cash/price_credit/ratings present
- **Actor ID:** 0wi38CtP5zEKifljx
- **Task ID:** Lzjpxlhz9pOrgFoYn
- **Published:** pending
- **Landing page:** https://apify.com/johnvc/fuelprices/examples/find-live-gas-prices-in-any-us-city-by-fuel-type?fpr=9n7kx3
- **AI-readable (.md):** same URL + .md

## Internal notes (NOT public)

- Upstream source: crowd-reported US gas station price data (see actor source repo). Keep generic in public copy.
- This is the first of three planned tasks for fuelprices (city / GPS coordinate / ZIP code).

Last Updated: 2026.06.10
