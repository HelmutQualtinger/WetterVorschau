# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A browser-based weather app (`wetter.html`) and a reusable Python weather-report skill. The skill generates HTML email drafts; the HTML page is a standalone client-side app.

## Key Files

- **`wetter.html`** — Self-contained single-file web app. All logic is inline JavaScript; no build step, no dependencies. Open directly in a browser.
- **`weather-report/scripts/weather_report.py`** — Python script that fetches weather data, generates the HTML report, and saves an IMAP draft. Run with `python3 weather-report/scripts/weather_report.py "<location>"`.
- **`weather-report/SKILL.md`** — Skill definition (loaded by Claude Code skills system).

## Architecture: wetter.html

Pure client-side, no server. Data flows:

1. **Geolocation** — `autoDetectLocation()` runs on load via `navigator.geolocation`; falls back to Shanghai if denied. Reverse-geocodes via Nominatim.
2. **Geocoding** — `geocode()` tries Open-Meteo geocoding API first, Nominatim as fallback.
3. **Weather data** — `fetchWeather()` calls `api.open-meteo.com/v1/forecast` for 72h hourly + 14-day daily data.
4. **Banner photo** — `fetchBannerPhoto()` queries Wikipedia `pageimages` API (en/de), falls back to Wikimedia Commons search.
5. **Rendering** — `buildReport()` assembles an HTML table with horizontally scrollable card rows for both forecast sections.

## Architecture: weather_report.py

Stdlib-only Python script (no pip installs). Saves the draft via IMAP (`smtp.1und1.de:587`, credentials in environment). The email uses `multipart/related` MIME with the banner image as a separate CID-referenced part — Gmail requires this structure for inline images; `data:` URIs and external URLs are blocked.

## Weather Data Source

Open-Meteo (free, no API key). Wind direction uncertainty shown as ±15° (NWP model spread). Speed range shown as steady wind → gust in km/h.

## Deployment

The page is deployed to GitHub Pages at:
`https://helmutqualtinger.github.io/WetterVorschau/wetter.html`

The OG/Twitter preview image is `Rebstein-Panormam.jpg` (committed to repo).
