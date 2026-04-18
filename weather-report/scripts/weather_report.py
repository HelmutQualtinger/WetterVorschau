#!/usr/bin/env python3
"""
Wetterbericht-Generator (Deutsch)
Fetches weather for a location and generates a German-language HTML report.

Usage: python3 weather_report.py "Stadt, Land"

Outputs JSON to stdout:
  location_name, lat, lon, subject,
  html_content, html_draft, html_path, eml_path
"""

import sys
import json
import urllib.request
import urllib.parse
import urllib.error
import ssl
import base64
import os
import tempfile
import math
from datetime import datetime, timezone

# SSL – avoids macOS "CERTIFICATE_VERIFY_FAILED"
_SSL_CTX = ssl.create_default_context()
try:
    import certifi
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    _SSL_CTX.check_hostname = False
    _SSL_CTX.verify_mode = ssl.CERT_NONE

# ── German WMO weather descriptions ────────────────────────────────────────────
WMO_CODES = {
    0:  ("Klarer Himmel",        "☀️"),
    1:  ("Überwiegend klar",     "🌤️"),
    2:  ("Teilweise bewölkt",    "⛅"),
    3:  ("Bedeckt",              "☁️"),
    45: ("Nebel",                "🌫️"),
    48: ("Gefrierender Nebel",   "🌫️"),
    51: ("Leichter Nieselregen", "🌦️"),
    53: ("Nieselregen",          "🌦️"),
    55: ("Starker Nieselregen",  "🌧️"),
    61: ("Leichter Regen",       "🌧️"),
    63: ("Regen",                "🌧️"),
    65: ("Starker Regen",        "🌧️"),
    71: ("Leichter Schneefall",  "🌨️"),
    73: ("Schneefall",           "❄️"),
    75: ("Starker Schneefall",   "❄️"),
    77: ("Schneekörner",         "🌨️"),
    80: ("Leichte Schauer",      "🌦️"),
    81: ("Schauer",              "🌦️"),
    82: ("Heftige Schauer",      "⛈️"),
    85: ("Leichte Schneeschauer","🌨️"),
    86: ("Starke Schneeschauer", "❄️"),
    95: ("Gewitter",             "⛈️"),
    96: ("Gewitter mit Hagel",   "⛈️"),
    99: ("Gewitter mit Hagel",   "⛈️"),
}

def wmo_label(code):
    return WMO_CODES.get(code, ("Unbekannt", "🌡️"))

# ── German date helpers ─────────────────────────────────────────────────────────
DE_WEEKDAYS = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
DE_MONTHS   = ["Jan","Feb","Mär","Apr","Mai","Jun",
               "Jul","Aug","Sep","Okt","Nov","Dez"]

def format_date_de(date_str):
    """'2025-04-15' → 'Di 15. Apr'"""
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        wd = DE_WEEKDAYS[dt.weekday()]
        mo = DE_MONTHS[dt.month - 1]
        return f"{wd} {dt.day}. {mo}"
    except Exception:
        return date_str

# ── Wind helpers ────────────────────────────────────────────────────────────────
COMPASS = ["N","NNO","NO","ONO","O","OSO","SO","SSO",
           "S","SSW","SW","WSW","W","WNW","NW","NNW"]

def deg_to_compass(deg):
    return COMPASS[round(deg / 22.5) % 16]

def wind_arrow_svg(deg, size=22):
    rad = math.radians(deg)
    cx = cy = size / 2
    r  = size / 2 - 2
    tx = cx + r * math.sin(rad)
    ty = cy - r * math.cos(rad)
    bx = cx - r * 0.55 * math.sin(rad)
    by = cy + r * 0.55 * math.cos(rad)
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
        f'style="vertical-align:middle;display:inline-block;">'
        f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="#e8f4fd" stroke="#aed6f1" stroke-width="1"/>'
        f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" '
        f'stroke="#2471a3" stroke-width="2" stroke-linecap="round"/>'
        f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="2.5" fill="#2471a3"/>'
        f'</svg>'
    )

# ── HTTP ────────────────────────────────────────────────────────────────────────
def http_get(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "WetterberichtBot/1.0"})
    with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as r:
        return r.read()

# ── Geocoding ───────────────────────────────────────────────────────────────────
def geocode(location):
    url = ("https://geocoding-api.open-meteo.com/v1/search?"
           + urllib.parse.urlencode({"name": location, "count": 1,
                                     "language": "de", "format": "json"}))
    data = json.loads(http_get(url))
    results = data.get("results")
    if not results:
        raise ValueError(f"Ort nicht gefunden: {location!r}")
    r = results[0]
    display = ", ".join(filter(None, [r.get("name",""), r.get("admin1",""), r.get("country","")]))
    return r["latitude"], r["longitude"], display

# ── Weather fetch ───────────────────────────────────────────────────────────────
def fetch_weather(lat, lon):
    hourly = "temperature_2m,weathercode,windspeed_10m,windgusts_10m,winddirection_10m"
    daily  = ("weathercode,temperature_2m_max,temperature_2m_min,"
              "windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant")
    params = urllib.parse.urlencode({
        "latitude": lat, "longitude": lon,
        "hourly": hourly, "daily": daily,
        "timezone": "auto", "forecast_days": 14,
        "wind_speed_unit": "kmh", "temperature_unit": "celsius",
    })
    return json.loads(http_get(f"https://api.open-meteo.com/v1/forecast?{params}"))

# ── OSM tile banner ─────────────────────────────────────────────────────────────
def _lat_lon_to_tile(lat, lon, zoom):
    lat_r = math.radians(lat)
    n = 2 ** zoom
    x = int((lon + 180.0) / 360.0 * n)
    y = int((1.0 - math.asinh(math.tan(lat_r)) / math.pi) / 2.0 * n)
    return x, y

def fetch_map_tiles(lat, lon, zoom=10, cols=5, rows=2):
    cx, cy = _lat_lon_to_tile(lat, lon, zoom)
    half_c, half_r = cols // 2, rows // 2
    tile_grid = []
    for dy in range(-half_r, rows - half_r):
        row = []
        for dx in range(-half_c, cols - half_c):
            tx = (cx + dx) % (2 ** zoom)
            ty = cy + dy
            url = f"https://tile.openstreetmap.org/{zoom}/{tx}/{ty}.png"
            try:
                data = http_get(url, timeout=10)
                row.append(base64.b64encode(data).decode())
            except Exception:
                row.append(None)
        tile_grid.append(row)
    return tile_grid

def tiles_to_html(tile_grid, tile_size=256):
    rows_html = []
    for row in tile_grid:
        cells = []
        for b64 in row:
            if b64:
                cells.append(
                    f'<td style="padding:0;line-height:0;font-size:0;">'
                    f'<img src="data:image/png;base64,{b64}" '
                    f'width="{tile_size}" height="{tile_size}" style="display:block;filter:brightness(0.75) saturate(0.7);" border="0"/></td>'
                )
            else:
                cells.append(
                    f'<td style="padding:0;background:#1a2233;'
                    f'width:{tile_size}px;height:{tile_size}px;"></td>'
                )
        rows_html.append(f'<tr>{"".join(cells)}</tr>')
    return (
        '<table cellpadding="0" cellspacing="0" border="0" '
        'style="border-collapse:collapse;line-height:0;font-size:0;">'
        + "".join(rows_html) + "</table>"
    )

# ── Dark-mode colour palette ────────────────────────────────────────────────────
# Background layers (darkest → lightest)
C_BG_PAGE   = "#0d1117"   # page background
C_BG_CARD   = "#161b22"   # card fill
C_BG_ROW    = "#1a2233"   # scroll-row container
C_BG_HEADER = "#1e3a5f"   # day / week label pill
C_BG_TITLE  = "#0d1f3c"   # title bar

# Borders & dividers
C_BORDER    = "#2a3f5a"
C_DIVIDER   = "#1e3a5f"

# Text
C_TEXT_PRI  = "#e6edf3"   # primary (time, temp)
C_TEXT_SEC  = "#8b949e"   # secondary (description, sub-values)
C_TEXT_MIN  = "#6e7681"   # tertiary (min temp)

# Accent colours
C_ACCENT    = "#58a6ff"   # wind direction label
C_GREEN     = "#3fb950"   # wind speed
C_PILL_TXT  = "#79c0ff"   # header pill text

# ── Card builders ───────────────────────────────────────────────────────────────
_TD_STYLE = (
    f"padding:7px 5px;text-align:center;vertical-align:top;"
    f"background:{C_BG_CARD};border-radius:8px;width:105px;"
    f"font-family:Arial,Helvetica,sans-serif;font-size:12px;"
    f"border:1px solid {C_BORDER};white-space:normal;"
)

def _arrow_svg_dark(deg, size=20):
    """Wind arrow with dark-mode colours."""
    rad = math.radians(deg)
    cx = cy = size / 2
    r  = size / 2 - 2
    tx = cx + r * math.sin(rad)
    ty = cy - r * math.cos(rad)
    bx = cx - r * 0.55 * math.sin(rad)
    by = cy + r * 0.55 * math.cos(rad)
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
        f'style="vertical-align:middle;display:inline-block;">'
        f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="#1e3a5f" stroke="#2a3f5a" stroke-width="1"/>'
        f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" '
        f'stroke="{C_ACCENT}" stroke-width="2" stroke-linecap="round"/>'
        f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="2.5" fill="{C_ACCENT}"/>'
        f'</svg>'
    )

def hourly_td(time_str, temp, code, wspeed, wgust, wdir):
    desc, icon = wmo_label(code)
    hour = time_str[11:16] if len(time_str) > 10 else time_str
    return (
        f'<td style="{_TD_STYLE}">'
        f'<b style="color:{C_TEXT_PRI};font-size:13px;">{hour}</b>'
        f'<div style="font-size:24px;margin:3px 0;">{icon}</div>'
        f'<div style="font-size:10px;color:{C_TEXT_SEC};line-height:1.2;">{desc}</div>'
        f'<div style="font-size:17px;font-weight:bold;color:{C_TEXT_PRI};margin-top:3px;">{temp:.0f}°C</div>'
        f'<div style="margin-top:5px;">{_arrow_svg_dark(wdir)}</div>'
        f'<div style="font-size:10px;color:{C_ACCENT};font-weight:bold;">{deg_to_compass(wdir)} ±15°</div>'
        f'<div style="font-size:10px;color:{C_GREEN};">{round(wspeed)}–{round(wgust)}&nbsp;km/h</div>'
        f'</td>'
    )

def daily_td(date_str, tmax, tmin, code, wspeed, wgust, wdir):
    desc, icon = wmo_label(code)
    label = format_date_de(date_str)
    return (
        f'<td style="{_TD_STYLE}">'
        f'<b style="color:{C_TEXT_PRI};font-size:11px;">{label}</b>'
        f'<div style="font-size:24px;margin:3px 0;">{icon}</div>'
        f'<div style="font-size:10px;color:{C_TEXT_SEC};line-height:1.2;">{desc}</div>'
        f'<div style="font-size:15px;font-weight:bold;color:{C_TEXT_PRI};margin-top:3px;">{tmax:.0f}°C</div>'
        f'<div style="font-size:11px;color:{C_TEXT_MIN};">↓{tmin:.0f}°C</div>'
        f'<div style="margin-top:5px;">{_arrow_svg_dark(wdir)}</div>'
        f'<div style="font-size:10px;color:{C_ACCENT};font-weight:bold;">{deg_to_compass(wdir)} ±15°</div>'
        f'<div style="font-size:10px;color:{C_GREEN};">{round(wspeed)}–{round(wgust)}&nbsp;km/h</div>'
        f'</td>'
    )

# ── Multi-row card section ──────────────────────────────────────────────────────
def day_header(date_str):
    label = format_date_de(date_str)
    return (
        f'<div style="font-size:12px;font-weight:bold;color:{C_PILL_TXT};'
        f'background:{C_BG_HEADER};border-radius:5px;padding:3px 10px;'
        f'margin-top:8px;margin-bottom:4px;display:inline-block;">'
        f'📅 {label}</div>'
    )

def card_row_html(tds):
    return (
        f'<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;'
        f'border-radius:6px;border:1px solid {C_BORDER};padding:5px;background:{C_BG_ROW};">'
        '<table cellpadding="0" cellspacing="4" '
        'style="border-collapse:separate;border-spacing:4px;width:max-content;">'
        '<tr>' + "".join(tds) + '</tr>'
        '</table></div>'
    )

def week_header(label):
    return (
        f'<div style="font-size:12px;font-weight:bold;color:{C_PILL_TXT};'
        f'background:{C_BG_HEADER};border-radius:5px;padding:3px 10px;'
        f'margin-top:8px;margin-bottom:4px;display:inline-block;">'
        f'🗓 {label}</div>'
    )

# ── Full HTML ───────────────────────────────────────────────────────────────────
def build_html(location_name, lat, lon, weather, tile_grid, generated_at):
    hourly = weather.get("hourly", {})
    daily  = weather.get("daily",  {})
    tz     = weather.get("timezone", "UTC")

    times    = hourly.get("time", [])
    temps    = hourly.get("temperature_2m", [])
    codes_h  = hourly.get("weathercode", [])
    wspeed_h = hourly.get("windspeed_10m", [])
    wgust_h  = hourly.get("windgusts_10m", [])
    wdir_h   = hourly.get("winddirection_10m", [])

    # ── 72h: group cards by calendar day (1 row per day) ────────────────────────
    days_72h = {}  # date_str → list of td html
    for i in range(0, min(73, len(times)), 3):
        ts = times[i]
        date_key = ts[:10]
        td = hourly_td(
            ts,
            temps[i]        if i < len(temps)    else 0,
            int(codes_h[i]) if i < len(codes_h)  else 0,
            wspeed_h[i]     if i < len(wspeed_h) else 0,
            wgust_h[i]      if i < len(wgust_h)  else 0,
            wdir_h[i]       if i < len(wdir_h)   else 0,
        )
        days_72h.setdefault(date_key, []).append(td)

    hourly_section = ""
    for date_key, tds in list(days_72h.items())[:3]:
        hourly_section += day_header(date_key)
        hourly_section += card_row_html(tds)

    # ── 14-day: 2 rows of 7 days ─────────────────────────────────────────────────
    ddates  = daily.get("time", [])
    dcodes  = daily.get("weathercode", [])
    dtmax   = daily.get("temperature_2m_max", [])
    dtmin   = daily.get("temperature_2m_min", [])
    dwspeed = daily.get("windspeed_10m_max", [])
    dwgust  = daily.get("windgusts_10m_max", [])
    dwdir   = daily.get("winddirection_10m_dominant", [])

    all_daily_tds = []
    for i in range(min(14, len(ddates))):
        all_daily_tds.append(daily_td(
            ddates[i],
            dtmax[i]        if i < len(dtmax)   else 0,
            dtmin[i]        if i < len(dtmin)   else 0,
            int(dcodes[i])  if i < len(dcodes)  else 0,
            dwspeed[i]      if i < len(dwspeed) else 0,
            dwgust[i]       if i < len(dwgust)  else 0,
            dwdir[i]        if i < len(dwdir)   else 0,
        ))

    daily_section = ""
    for chunk_i, start in enumerate(range(0, 14, 7)):
        chunk = all_daily_tds[start:start+7]
        if not chunk:
            break
        w1 = format_date_de(ddates[start]) if start < len(ddates) else ""
        w2 = format_date_de(ddates[min(start+6, len(ddates)-1)]) if ddates else ""
        daily_section += week_header(f"Woche {chunk_i+1}: {w1} – {w2}")
        daily_section += card_row_html(chunk)

    banner_html = tiles_to_html(tile_grid) if tile_grid else (
        f'<div style="background:{C_BG_TITLE};width:100%;height:256px;text-align:center;'
        f'line-height:256px;font-family:Arial;color:{C_TEXT_PRI};font-size:18px;">'
        f'📍 {location_name}</div>'
    )

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wetterbericht – {location_name}</title>
</head>
<body style="margin:0;padding:0;background:{C_BG_PAGE};font-family:Arial,Helvetica,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0"
       style="max-width:900px;margin:0 auto;background:{C_BG_PAGE};">

  <!-- Kartenbanner (7×1 OSM-Kacheln = 1792×256 px, abgedunkelt) -->
  <tr>
    <td style="padding:0;overflow:hidden;line-height:0;font-size:0;height:256px;">
      {banner_html}
    </td>
  </tr>

  <!-- Titelzeile -->
  <tr>
    <td style="background:{C_BG_TITLE};padding:14px 20px;border-bottom:1px solid {C_DIVIDER};">
      <div style="color:{C_TEXT_PRI};font-size:20px;font-weight:bold;">
        📍 Wetterbericht: {location_name}
      </div>
      <div style="color:{C_TEXT_SEC};font-size:11px;margin-top:3px;">
        {lat:.4f}°N, {lon:.4f}°O &nbsp;·&nbsp; Zeitzone: {tz}
        &nbsp;·&nbsp; Stand: {generated_at}
      </div>
    </td>
  </tr>

  <!-- 72-Stunden-Vorhersage -->
  <tr>
    <td style="padding:18px 16px 10px;background:{C_BG_PAGE};">
      <div style="font-size:15px;font-weight:bold;color:{C_TEXT_PRI};
                  border-bottom:2px solid {C_DIVIDER};padding-bottom:6px;margin-bottom:6px;">
        ⏱ 72-Stunden-Vorhersage
        <span style="font-size:11px;font-weight:normal;color:{C_TEXT_SEC};">(3-Stunden-Intervalle, ein Tag pro Zeile)</span>
      </div>
      <div style="font-size:10px;color:{C_TEXT_MIN};margin-bottom:6px;">
        Windrichtung ±15° Modellstreuung &nbsp;·&nbsp; Windstärke: mittlere – Böen (km/h)
      </div>
      {hourly_section}
    </td>
  </tr>

  <!-- 14-Tage-Vorhersage -->
  <tr>
    <td style="padding:10px 16px 20px;background:{C_BG_PAGE};">
      <div style="font-size:15px;font-weight:bold;color:{C_TEXT_PRI};
                  border-bottom:2px solid {C_DIVIDER};padding-bottom:6px;margin-bottom:6px;">
        📅 14-Tage-Vorhersage
        <span style="font-size:11px;font-weight:normal;color:{C_TEXT_SEC};">(täglich, eine Woche pro Zeile)</span>
      </div>
      <div style="font-size:10px;color:{C_TEXT_MIN};margin-bottom:6px;">
        Windrichtung ±15° Modellstreuung &nbsp;·&nbsp; Max. Windstärke: mittlere – Böen (km/h)
      </div>
      {daily_section}
    </td>
  </tr>

  <!-- Fußzeile -->
  <tr>
    <td style="background:{C_BG_TITLE};padding:8px 16px;border-top:1px solid {C_DIVIDER};">
      <div style="font-size:10px;color:{C_TEXT_MIN};text-align:center;">
        Wetterdaten: <a href="https://open-meteo.com/" style="color:{C_ACCENT};">Open-Meteo</a>
        &nbsp;·&nbsp; Karte: © OpenStreetMap-Mitwirkende
        &nbsp;·&nbsp; Windrichtungsungenauigkeit: ±15° Modellstreuung
      </div>
    </td>
  </tr>

</table>
</body>
</html>"""

# ── MIME .eml ───────────────────────────────────────────────────────────────────
def build_eml(subject, html_content):
    import email.mime.multipart, email.mime.text
    outer = email.mime.multipart.MIMEMultipart("mixed")
    outer["Subject"] = subject
    outer["To"] = ""
    outer["From"] = ""
    outer.attach(email.mime.text.MIMEText(html_content, "html", "utf-8"))
    return outer.as_string()

# ── Main ────────────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Nutzung: weather_report.py 'Stadt, Land'"}))
        sys.exit(1)

    location_query = " ".join(sys.argv[1:])

    try:
        lat, lon, location_name = geocode(location_query)
    except Exception as e:
        print(json.dumps({"error": f"Geocodierung fehlgeschlagen: {e}"}))
        sys.exit(1)

    try:
        weather = fetch_weather(lat, lon)
    except Exception as e:
        print(json.dumps({"error": f"Wetterdaten konnten nicht abgerufen werden: {e}"}))
        sys.exit(1)

    tile_grid    = fetch_map_tiles(lat, lon, zoom=10, cols=7, rows=1)
    generated_at = datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M UTC")

    # Full HTML (map tiles embedded) – written to disk for local preview / .eml
    html_full = build_html(location_name, lat, lon, weather, tile_grid, generated_at)

    # Compact HTML (gradient banner, no tiles) – small enough to pass to Gmail MCP
    html_draft = build_html(location_name, lat, lon, weather, None, generated_at)

    html_fd, html_path = tempfile.mkstemp(suffix=".html", prefix="wetterbericht_")
    with os.fdopen(html_fd, "w", encoding="utf-8") as f:
        f.write(html_full)

    subject = f"Wetterbericht: {location_name}"
    eml_fd, eml_path = tempfile.mkstemp(suffix=".eml", prefix="wetterbericht_")
    with os.fdopen(eml_fd, "w", encoding="utf-8") as f:
        f.write(build_eml(subject, html_full))

    # stdout JSON intentionally omits html_full (too large for MCP calls).
    # html_path points to the full version on disk.
    print(json.dumps({
        "location_name": location_name,
        "lat": lat,
        "lon": lon,
        "subject": subject,
        "html_draft": html_draft,   # ~45 KB – use this for gmail_create_draft
        "html_path": html_path,     # full version with map tiles
        "eml_path": eml_path,
    }))

if __name__ == "__main__":
    main()
