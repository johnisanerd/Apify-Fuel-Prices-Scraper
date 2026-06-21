# ⛽ Fuel Prices API: Live US Gas Station Prices in Clean JSON

> The most efficient, reliable, and developer-friendly way to use the Fuel Prices API.

**Actor page:** [apify.com/johnvc/fuelprices](https://apify.com/johnvc/fuelprices?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/fuelprices/input-schema](https://apify.com/johnvc/fuelprices/input-schema?fpr=9n7kx3)

The Fuel Prices API returns live, crowd-reported gas station prices and station metadata for any US location (with some Canadian coverage) as clean, structured JSON. Search by ZIP code, city name, or GPS coordinates and get one record per station: name, full address, distance from your search point, cash and credit prices with posting timestamps, price unit, and ratings. Choose the fuel type (regular, midgrade, premium, diesel, E85, or unleaded 88) and filter by data freshness.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Fuel-Prices-Scraper.git
   cd Apify-Fuel-Prices-Scraper
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python fuel-prices-scraper.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python fuel-prices-scraper.py
```

## Why Use This Fuel Prices API?

**Station-level detail.** Each result is one gas station with its name, full address, distance from your search point, cash and credit prices, price unit, and ratings, so you can compare stations directly.

**Search any way you like.** Query by ZIP code, city name, or GPS coordinates pasted straight from a map. Coordinates resolve to the nearest area.

**Fuel-type and freshness controls.** Pick regular, midgrade, premium, diesel, E85, or unleaded 88, and use the freshness filter to keep only recently reported prices.

**Pay only for results.** Billing is per station returned, with no setup fee, no subscription, and no charge for runs that return nothing. A typical city or ZIP search costs a couple of cents.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can pull live fuel prices for you on demand.

## Features

### Core Capabilities
- **Search by ZIP, city, or coordinates** across US locations (some Canadian coverage)
- **Fuel-type selection**: regular, midgrade, premium, diesel, E85, unleaded 88
- **Freshness filtering** by maximum data age in days
- **Cash and credit prices** with per-price posting timestamps
- **Station metadata**: name, address, distance, ratings

### Data Quality
- **One record per station** with a stable structure
- **Cash and credit prices** reported separately, each with a posted time
- **Full address components** (line 1/2, city, region, postal code)
- **Distance and ratings** for ranking and comparison
- **Consistent JSON** shape across every query

## Usage Examples

### Basic Example
The cheapest way to try the API: one ZIP code, regular fuel.
```json
{
  "search": "11507"
}
```

### Advanced Example
A city search for diesel, freshest data only.
```json
{
  "search": "New York, NY",
  "fuel": 4,
  "lang": "en",
  "maxAge": 3
}
```

### By coordinates
Paste GPS coordinates straight from a map.
```json
{
  "search": "36.0816642, -115.0534345",
  "fuel": 1
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `search` | `string` | Yes | - | Location query: ZIP code, city name, or `lat, lng` coordinates. |
| `fuel` | `integer` | No | `1` | Fuel type: `1` Regular, `2` Midgrade, `3` Premium, `4` Diesel, `5` E85, `12` Unleaded 88. |
| `lang` | `string` | No | `en` | Language code for localized fields (only `en` is currently supported). |
| `maxAge` | `integer` | No | `0` | Maximum age of price data in days. `0` returns all stations regardless of when prices were reported. |
| `output_file` | `string` | No | (none) | Optional CSV filename; a timestamped name is generated if omitted. |

## Output Format

One station per dataset item. A real result for ZIP `11507`:

```json
{
  "id": "56437",
  "name": "Sunoco",
  "distance": null,
  "priceUnit": "dollars_per_gallon",
  "ratingsCount": 45,
  "starRating": 4.4,
  "address_line1": "993 Willis Ave",
  "address_line2": "",
  "address_locality": "Albertson",
  "address_region": "NY",
  "address_postalCode": "11507",
  "price_credit": 4.47,
  "price_credit_postedTime": "2026-05-28T10:04:12.551Z",
  "price_cash": 4.25,
  "price_cash_postedTime": "2026-05-28T10:04:12.536Z"
}
```

---

## Use as an MCP tool

You can load the Fuel Prices API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/fuelprices
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Fuel Prices API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/fuelprices"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Fuel Prices API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/fuelprices"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/fuelprices" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Fuel Prices API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/fuelprices`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/fuelprices`, using OAuth when prompted.
5. Ask Claude to run the Fuel Prices API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/fuelprices"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/fuelprices",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Fuel Prices API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/fuelprices`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

## n8n integration

Available as an n8n community node, **[n8n-nodes-fuel-prices-api](https://www.npmjs.com/package/n8n-nodes-fuel-prices-api)**. In n8n, open Settings, Community Nodes, install `n8n-nodes-fuel-prices-api`, then use the Fuel Prices node in any workflow (it also works as an AI Agent tool).

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Fuel Prices API to power price monitoring, comparison apps, and analytics with reliable, structured results.*

## Featured Tasks

Ready-to-run examples that show this API solving a specific problem. Each opens its own setup so you can run it on your account in one click.

- [Find live gas prices in any US city by fuel type](https://apify.com/johnvc/fuelprices/examples/find-live-gas-prices-in-any-us-city-by-fuel-type?fpr=9n7kx3) - Search any US city and get one row per station with name, full address, distance, cash and credit prices, and ratings.
- [Find gas prices near GPS map coordinates](https://apify.com/johnvc/fuelprices/examples/find-gas-prices-near-gps-map-coordinates?fpr=9n7kx3) - Paste latitude and longitude from a map and get nearby stations with prices, distance, and ratings.
- [Find gas station prices by ZIP code](https://apify.com/johnvc/fuelprices/examples/find-gas-station-prices-by-zip-code?fpr=9n7kx3) - Look up stations for any US ZIP code with full address, cash and credit prices, and ratings.

Last Updated: 2026.06.21
