# Task publish sheet: Fetch gas prices in Fort Worth, Texas by API

Paste-ready values for the Apify Console Publication tab. Public copy in this sheet is clean per the
Immutable Rules (no em dash, no vendor name, no hard price, no "Scraper" identity noun).

## Parent Actor

- **Actor name:** FuelPrices API (display: FuelPrices | Pay Per Result, Easy to Use, No Cookies)
- **Store link:** https://apify.com/johnvc/fuelprices?fpr=9n7kx3
- **Repo:** /Users/johncole/Github/Apify-Fuel-Prices-Scraper
- **Username / slug:** johnvc / fuelprices

## Target keyword

`fetch gas prices in fort worth texas`

## Display information (Publication tab)

- **Slug:** `fetch-gas-prices-in-fort-worth-texas-by-api` (auto-derived from the task Title)
- **SEO task title:** `Fetch gas prices in Fort Worth, Texas by API` (44/60)
- **SEO description:** `Fetch live gas prices in Fort Worth, Texas from a REST API: station name, address, distance, cash and credit prices. Clean JSON, pay per result.` (144/160)

Final public URL: `https://apify.com/johnvc/fuelprices/examples/fetch-gas-prices-in-fort-worth-texas-by-api?fpr=9n7kx3`

## Input (visible fields)

The task runs with its full input config; the fields below are the ones shown on the landing page.

| Field (property name) | Value | Visible? |
|-----------------------|-------|----------|
| search                | Fort Worth, TX | yes |
| fuel                  | 1 (Regular) | yes |
| lang                  | en | no (noise) |

Secrets confirmed `isSecret` in the Actor schema: none present (no credential-shaped fields).

## Dataset schema

- **View chosen:** `Overview`
- **Why it matches the description:** Overview exposes ID, Station, Address, City, State, ZIP,
  Distance (mi), Price Unit, Cash Price, Cash Posted, Credit Price, Credit Posted, Ratings, and Stars,
  which covers the promised station name, address, distance, and cash and credit prices.

## Test run + publish status

- **Run status:** Succeeded (run ZwtXwFSRoqEfng4dI), Fort Worth stations returned
- **Verified output matches description:** yes. Every row resolved to address_locality "Fort Worth".
  Sample: Sam's Club, 8351 Anderson Blvd, Fort Worth, credit 3.20; Sam's Club, 4400 Bryant Irvin Rd,
  credit 3.23
- **Actor ID:** 0wi38CtP5zEKifljx
- **Task ID:** HJlSz6dwwUcEnOh1m
- **Published:** pending
- **Landing page:** https://apify.com/johnvc/fuelprices/examples/fetch-gas-prices-in-fort-worth-texas-by-api?fpr=9n7kx3
- **AI-readable (.md):** same URL + .md

## Internal notes (NOT public)

- Upstream source: crowd-reported US gas station price data (see actor source repo). Keep generic in
  public copy.
- **This task's saved input was wrong until 2026-08-03.** It was created by copying the Austin task and
  the `search` value was never changed, so it returned Austin stations under a Fort Worth name. Fixed to
  "Fort Worth, TX" and re-verified before publishing. The same copy-paste defect was found on 12 already
  published tasks in this series and fixed the same day.
- City page in the per-metro PSEO series. Each city ships a gas `-by-api` page and a diesel `-by-mcp`
  page; the diesel twin for Fort Worth was created 2026-08-03 to complete the pair.

Last Updated: 2026.08.03
