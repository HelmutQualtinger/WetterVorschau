# Weather Report Skill — Development Chat

## User Request

> Create a skill creating a weather report. It should show a forecast for the next 72h in 3h periods and a 14-day forecast with daily frequency. The three-hour intervals and the days of the 14-day forecast should be organised horizontally side by side. It should include the wind speed and direction with an error. The user should specify the location for which the report should be prepared. A header image should be included showing the location. The HTML report should open in Gmail to be reviewed before sending. Be careful on how to include the banner in the email — separate MIME file to be referenced in the HTML. The skill should be implemented in a reusable Python script.

---

## Implementation

**Session initialized.** 7 commands executed, tools loaded, to-do list updated.

Script works. Now adding a data-URI HTML variant (for the Gmail draft which can't use CID references via the MCP), then writing `SKILL.md`.

### Files Created

| File | Purpose |
|------|---------|
| `~/.claude/skills/weather-report/SKILL.md` | Skill definition (auto-loaded by Claude Code) |
| `~/.claude/skills/weather-report/scripts/weather_report.py` | Self-contained Python script (stdlib only) |
| `~/.claude/skills/weather-report/evals/evals.json` | 3 test cases |

### How It Works

- Trigger by saying e.g. *"weather report for Paris"* or *"forecast email for Tokyo"*
- Python script geocodes the location (Open-Meteo), fetches 72h hourly + 14-day daily weather, downloads an OpenStreetMap static map, and generates two HTML variants
- **Gmail draft**: banner image embedded as a base64 data URI in `<img>` (Gmail MCP can't handle `multipart/related` CID references)
- **.eml file** saved locally — proper `multipart/related` MIME with image as a separate MIME part referenced by `Content-ID: cid:...` (use with Apple Mail or Thunderbird)
- **Wind uncertainty**: each card shows compass direction ±15° (NWP model spread) plus a speed range from steady wind to gust (km/h)

> To use it: say *"weather report for Salzburg"* in a new conversation.

---

## Bug Report

> **Change the skill:** no banner is visible. Only 1 day in a row for the 72h forecast, and only one week in a row for the 14-day forecast.

**Investigation:** Cards use `display:inline-block` inside a table cell — the table constrains the width and overflow doesn't scroll as expected. Also need to fix the banner.

**Fix planned:** Switch both to proper table-row layout and replace the broken static map with OSM tiles assembled as a strip.
