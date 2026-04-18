---
name: weather-report
description: >
  Generate a professional weather report for any location and create a Gmail draft ready to send.
  The report includes a 72-hour forecast (3-hour intervals) and a 14-day daily forecast, both
  displayed as horizontal scrollable card rows. Each card shows temperature, weather icon,
  wind speed range (steady → gust km/h), and wind direction with compass arrow and ±15° model
  uncertainty. A location map banner image is embedded in the email using a CID reference in a
  separate MIME part.

  Use this skill whenever the user asks for a weather forecast, weather report, weather email,
  or wants to send weather information for a location — even if they don't use the word "skill"
  or "report". Trigger examples: "weather for Tokyo", "send me the forecast for Berlin",
  "make a weather email for Sydney", "what's the weather like in Paris this week".
---

# Weather Report Skill

Generate a polished HTML weather report for a user-specified location and deliver it as a
Gmail draft with a properly embedded location banner image.

## Step 1 — Get the location

If the user hasn't specified a location, ask: **"Which location should I generate the weather
report for?"**

Accept any form: city name, "City, Country", airport code, landmark, etc. The geocoder
handles disambiguation.

## Step 2 — Run the Python script

```bash
python3 ~/.claude/skills/weather-report/scripts/weather_report.py "<LOCATION>"
```

The script outputs a single JSON object to stdout. Parse it. Key fields:

| Field | Description |
|---|---|
| `location_name` | Resolved display name, e.g. "Munich, Bavaria, Germany" |
| `lat` / `lon` | Coordinates |
| `subject` | Email subject line |
| `html_draft` | Full HTML with banner image embedded as a **data URI** — use this for the Gmail draft |
| `html_content` | Full HTML with `cid:` reference — used in the `.eml` file |
| `eml_path` | Path to the saved `.eml` file (multipart/related with inline CID image) |
| `html_path` | Path to a local HTML preview file |
| `image_cid` | The Content-ID string for the inline image |
| `image_base64` | Base64-encoded map image |
| `image_mime_type` | MIME type of the image (`image/png`, `image/svg+xml`, etc.) |

If the script exits with an error key in the JSON, tell the user what went wrong and stop.

## Step 3 — Create the Gmail draft

Use the Gmail MCP tool `gmail_create_draft` to create the draft.

**Important — image embedding strategy:**
- Gmail drafts created via the API cannot directly reference inline CID attachments.
- Use `html_draft` (data URI version) as the email body. The banner image is embedded
  directly in the HTML via a base64 data URI, so it renders correctly in Gmail's preview.
- The `.eml` file at `eml_path` contains the proper multipart/related structure with a
  separate MIME image part referenced by `Content-ID`. This file is suitable for import
  into a desktop mail client (Apple Mail, Thunderbird) if the user wants to send via one
  of those instead.

Call the draft tool with:
- **subject**: the `subject` field from the script output
- **body**: the `html_draft` field (full HTML string)
- Any other parameters the MCP tool requires (to, cc, etc.) — if not provided by the user,
  leave recipient fields empty or omit them.

## Step 4 — Open the draft directly in Gmail

The `gmail_create_draft` response includes a draft `id` (and usually a nested `message.id`).
Use the message ID to open that specific draft in Gmail's compose window:

```bash
open "https://mail.google.com/mail/u/0/#drafts/<MESSAGE_ID>"
```

- If the response has a `message` object with an `id`, use `message.id` as `<MESSAGE_ID>`.
- If only a top-level `id` is present, use that.
- If no ID is available, fall back to `open "https://mail.google.com/mail/u/0/#drafts"`.

This opens the draft directly in Gmail's compose window so the user can review and send it
without having to search through the Drafts folder.

Then confirm to the user:
- Gmail has been opened with the draft ready to send.
- The subject line and resolved location name.
- The local `.eml` file path for Apple Mail / Thunderbird (map renders correctly there too).

## Notes on the report layout

- **72-hour section**: 24 cards (every 3 hours), horizontally scrollable. Shows hour, temp,
  weather icon, wind compass arrow, direction label, ±15° uncertainty, and speed–gust range.
- **14-day section**: 14 cards (one per day), horizontally scrollable. Shows weekday+date,
  temp max/min, weather icon, wind compass arrow, direction, ±15° uncertainty, max speed–gust.
- Weather data: Open-Meteo (free, no API key). Map image: OpenStreetMap static map (fallback
  to SVG placeholder if the tile server is unavailable).
- Wind direction uncertainty of ±15° reflects typical NWP model spread; gust vs. sustained
  speed gives the wind speed uncertainty range.

## Error handling

- **Location not found**: Tell the user the geocoder couldn't find the location and ask them
  to be more specific (e.g., add country name).
- **Network failure**: Retry once; if it still fails, tell the user and suggest checking
  internet connectivity.
- **Gmail MCP failure**: Save the `.eml` file path and tell the user they can open it
  directly in Apple Mail or Thunderbird.
