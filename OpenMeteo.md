# Open-Meteo API — Complete Variable Reference

## Overview

Open-Meteo provides multiple distinct APIs, each with their own variable sets. This document covers all endpoints comprehensively.

**APIs covered:**
1. Weather Forecast API (standard)
2. Historical Weather API
3. Historical Forecast API
4. Marine Weather API
5. Air Quality API
6. Flood API
7. Ensemble Forecast API
8. Seasonal Forecast API
9. Climate API
10. Geocoding API
11. Elevation API

---

## 1. Weather Forecast API

**Base URL:** `https://api.open-meteo.com/v1/forecast`

### 1.1 Hourly Variables (`hourly=`)

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m` | Air temperature at 2 meters above ground | °C (°F) |
| `relative_humidity_2m` | Relative humidity at 2 meters above ground | % |
| `dew_point_2m` | Dew point temperature at 2 meters above ground | °C (°F) |
| `apparent_temperature` | Perceived feels-like temperature combining wind chill factor, relative humidity, and solar radiation | °C (°F) |
| `pressure_msl` | Atmospheric air pressure reduced to mean sea level | hPa |
| `surface_pressure` | Pressure at surface | hPa |
| `cloud_cover` | Total cloud cover as an area fraction | % |
| `cloud_cover_low` | Low level clouds and fog up to 3 km altitude | % |
| `cloud_cover_mid` | Mid level clouds from 3 to 8 km altitude | % |
| `cloud_cover_high` | High level clouds from 8 km altitude | % |
| `wind_speed_10m` | Wind speed at 10 meters above ground | km/h (mph, m/s, knots) |
| `wind_speed_80m` | Wind speed at 80 meters above ground | km/h (mph, m/s, knots) |
| `wind_speed_120m` | Wind speed at 120 meters above ground | km/h (mph, m/s, knots) |
| `wind_speed_180m` | Wind speed at 180 meters above ground | km/h (mph, m/s, knots) |
| `wind_direction_10m` | Wind direction at 10 meters above ground | ° |
| `wind_direction_80m` | Wind direction at 80 meters above ground | ° |
| `wind_direction_120m` | Wind direction at 120 meters above ground | ° |
| `wind_direction_180m` | Wind direction at 180 meters above ground | ° |
| `wind_gusts_10m` | Gusts at 10 meters above ground as a maximum of the preceding hour | km/h (mph, m/s, knots) |
| `shortwave_radiation` | Shortwave solar radiation as average of the preceding hour | W/m² |
| `direct_radiation` | Direct solar radiation as average of the preceding hour on the horizontal plane | W/m² |
| `direct_normal_irradiance` | Direct solar radiation on the normal plane (perpendicular to the sun) | W/m² |
| `diffuse_radiation` | Diffuse solar radiation as average of the preceding hour | W/m² |
| `global_tilted_irradiance` | Total radiation received on a tilted pane as average of the preceding hour | W/m² |
| `shortwave_radiation_instant` | Shortwave radiation at the indicated time (instantaneous) | W/m² |
| `direct_radiation_instant` | Direct radiation at the indicated time (instantaneous) | W/m² |
| `diffuse_radiation_instant` | Diffuse radiation at the indicated time (instantaneous) | W/m² |
| `direct_normal_irradiance_instant` | Direct normal irradiance at the indicated time (instantaneous) | W/m² |
| `global_tilted_irradiance_instant` | Global tilted irradiance at the indicated time (instantaneous) | W/m² |
| `terrestrial_solar_radiation` | Terrestrial solar radiation (averaged over hour) | W/m² |
| `terrestrial_solar_radiation_instant` | Terrestrial solar radiation at the indicated time (instantaneous) | W/m² |
| `vapour_pressure_deficit` | Vapor pressure deficit | kPa |
| `cape` | Convective available potential energy | J/kg |
| `lifted_index` | Lifted Index — atmospheric instability measure | dimensionless |
| `convective_inhibition` | Convective inhibition energy needed to trigger convection | J/kg |
| `evapotranspiration` | Evapotranspiration from land surface and plants | mm (inch) |
| `et0_fao_evapotranspiration` | ET₀ Reference Evapotranspiration of a well watered grass field | mm (inch) |
| `precipitation` | Total precipitation (rain, showers, snow) sum of the preceding hour | mm (inch) |
| `snowfall` | Snowfall amount of the preceding hour | cm (inch) |
| `precipitation_probability` | Probability of precipitation with more than 0.1 mm in the preceding hour | % |
| `rain` | Rain from large scale weather systems of the preceding hour | mm (inch) |
| `showers` | Showers from convective precipitation in the preceding hour | mm (inch) |
| `weather_code` | Weather condition as a numeric code following WMO standards | WMO code |
| `snow_depth` | Snow depth on the ground | meters |
| `freezing_level_height` | Altitude above sea level of the 0°C level | meters |
| `visibility` | Viewing distance | meters |
| `soil_temperature_0cm` | Temperature in the soil at 0 cm depth (surface) | °C (°F) |
| `soil_temperature_6cm` | Temperature in the soil at 6 cm depth | °C (°F) |
| `soil_temperature_18cm` | Temperature in the soil at 18 cm depth | °C (°F) |
| `soil_temperature_54cm` | Temperature in the soil at 54 cm depth | °C (°F) |
| `soil_moisture_0_to_1cm` | Average soil water content at 0–1 cm depth | m³/m³ |
| `soil_moisture_1_to_3cm` | Average soil water content at 1–3 cm depth | m³/m³ |
| `soil_moisture_3_to_9cm` | Average soil water content at 3–9 cm depth | m³/m³ |
| `soil_moisture_9_to_27cm` | Average soil water content at 9–27 cm depth | m³/m³ |
| `soil_moisture_27_to_81cm` | Average soil water content at 27–81 cm depth | m³/m³ |
| `temperature_80m` | Air temperature at 80 meters above ground | °C (°F) |
| `temperature_120m` | Air temperature at 120 meters above ground | °C (°F) |
| `temperature_180m` | Air temperature at 180 meters above ground | °C (°F) |
| `uv_index` | UV Index | Index (0–11+) |
| `uv_index_clear_sky` | UV Index assuming cloud-free conditions | Index (0–11+) |
| `is_day` | 1 if the current time step has daylight, 0 at night | Dimensionless |
| `sunshine_duration` | Number of seconds of sunshine in the preceding hour (direct radiation > 120 W/m²) | seconds |
| `wet_bulb_temperature_2m` | Wet bulb temperature at 2 meters above ground | °C (°F) |
| `total_column_integrated_water_vapour` | Total column integrated water vapour in the atmosphere | kg/m² |
| `boundary_layer_height` | Height of the atmospheric planetary boundary layer | meters |

### 1.2 15-Minutely Variables (`minutely_15=`)

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m` | Air temperature at 2 meters above ground | °C (°F) |
| `relative_humidity_2m` | Relative humidity at 2 meters above ground | % |
| `dew_point_2m` | Dew point temperature at 2 meters above ground | °C (°F) |
| `apparent_temperature` | Apparent temperature combining multiple factors | °C (°F) |
| `precipitation` | Total precipitation sum of the preceding 15 minutes | mm (inch) |
| `rain` | Rain from the preceding 15 minutes | mm (inch) |
| `showers` | Showers from the preceding 15 minutes | mm (inch) |
| `snowfall` | Snowfall amount of the preceding 15 minutes | cm (inch) |
| `snowfall_height` | Altitude above sea level where snowfall occurs | meters |
| `freezing_level_height` | Altitude above sea level of the 0°C level | meters |
| `sunshine_duration` | Duration of sunshine in the preceding 15-minute period | seconds |
| `weather_code` | Weather condition as a numeric code (WMO) | WMO code |
| `wind_speed_10m` | Wind speed at 10 meters above ground | km/h (mph, m/s, knots) |
| `wind_speed_80m` | Wind speed at 80 meters above ground | km/h (mph, m/s, knots) |
| `wind_direction_10m` | Wind direction at 10 meters above ground | ° |
| `wind_direction_80m` | Wind direction at 80 meters above ground | ° |
| `wind_gusts_10m` | Gusts at 10 meters as a maximum of the preceding 15 minutes | km/h (mph, m/s, knots) |
| `visibility` | Viewing distance | meters |
| `cape` | Convective available potential energy | J/kg |
| `lightning_potential` | Lightning Potential Index | J/kg |
| `is_day` | 1 if daylight, 0 at night | Dimensionless |
| `shortwave_radiation` | Solar radiation averaged over preceding 15 minutes | W/m² |
| `direct_radiation` | Direct solar radiation averaged over preceding 15 minutes | W/m² |
| `diffuse_radiation` | Diffuse solar radiation averaged over preceding 15 minutes | W/m² |
| `direct_normal_irradiance` | Direct normal irradiance averaged over preceding 15 minutes | W/m² |
| `global_tilted_irradiance` | Total radiation on tilted pane averaged over preceding 15 minutes | W/m² |
| `terrestrial_solar_radiation` | Terrestrial solar radiation averaged over preceding 15 minutes | W/m² |
| `shortwave_radiation_instant` | Shortwave radiation at indicated time (instantaneous) | W/m² |
| `direct_radiation_instant` | Direct radiation at indicated time (instantaneous) | W/m² |
| `diffuse_radiation_instant` | Diffuse radiation at indicated time (instantaneous) | W/m² |
| `direct_normal_irradiance_instant` | Direct normal irradiance at indicated time (instantaneous) | W/m² |
| `global_tilted_irradiance_instant` | Global tilted irradiance at indicated time (instantaneous) | W/m² |
| `terrestrial_solar_radiation_instant` | Terrestrial solar radiation at indicated time (instantaneous) | W/m² |

> Note: 15-minutely data is only available in Central Europe and North America; hourly data is interpolated elsewhere.

### 1.3 Daily Variables (`daily=`)

| Parameter | Description | Unit |
|-----------|-------------|------|
| `weather_code` | The most severe weather condition on a given day | WMO code |
| `temperature_2m_max` | Maximum daily air temperature at 2 meters above ground | °C (°F) |
| `temperature_2m_min` | Minimum daily air temperature at 2 meters above ground | °C (°F) |
| `temperature_2m_mean` | Mean daily air temperature at 2 meters above ground | °C (°F) |
| `apparent_temperature_max` | Maximum daily apparent temperature | °C (°F) |
| `apparent_temperature_min` | Minimum daily apparent temperature | °C (°F) |
| `apparent_temperature_mean` | Mean daily apparent temperature | °C (°F) |
| `sunrise` | Time of sunrise | ISO 8601 |
| `sunset` | Time of sunset | ISO 8601 |
| `daylight_duration` | Number of seconds of daylight per day | seconds |
| `sunshine_duration` | Number of seconds of sunshine per day (direct radiation > 120 W/m²) | seconds |
| `uv_index_max` | Daily maximum UV Index | Index |
| `uv_index_clear_sky_max` | Daily maximum UV Index assuming cloud-free conditions | Index |
| `precipitation_sum` | Sum of daily precipitation (rain + showers + snowfall) | mm |
| `rain_sum` | Sum of daily rain | mm |
| `showers_sum` | Sum of daily showers | mm |
| `snowfall_sum` | Sum of daily snowfall | cm |
| `precipitation_hours` | Number of hours with rain | hours |
| `precipitation_probability_max` | Maximum probability of precipitation during the day | % |
| `precipitation_probability_mean` | Mean probability of precipitation during the day | % |
| `precipitation_probability_min` | Minimum probability of precipitation during the day | % |
| `wind_speed_10m_max` | Maximum wind speed at 10 meters on a day | km/h (mph, m/s, knots) |
| `wind_gusts_10m_max` | Maximum wind gusts at 10 meters on a day | km/h (mph, m/s, knots) |
| `wind_direction_10m_dominant` | Dominant wind direction during the day | ° |
| `wind_speed_10m_mean` | Mean wind speed at 10 meters | km/h (mph, m/s, knots) |
| `wind_speed_10m_min` | Minimum wind speed at 10 meters | km/h (mph, m/s, knots) |
| `wind_gusts_10m_mean` | Mean wind gusts at 10 meters | km/h (mph, m/s, knots) |
| `wind_gusts_10m_min` | Minimum wind gusts at 10 meters | km/h (mph, m/s, knots) |
| `shortwave_radiation_sum` | Sum of solar radiation on a given day | MJ/m² |
| `et0_fao_evapotranspiration` | Daily sum of ET₀ Reference Evapotranspiration | mm |
| `cloud_cover_mean` | Mean cloud cover | % |
| `cloud_cover_max` | Maximum cloud cover | % |
| `cloud_cover_min` | Minimum cloud cover | % |
| `relative_humidity_2m_mean` | Mean relative humidity at 2 meters | % |
| `relative_humidity_2m_max` | Maximum relative humidity at 2 meters | % |
| `relative_humidity_2m_min` | Minimum relative humidity at 2 meters | % |
| `dew_point_2m_mean` | Mean dew point at 2 meters | °C (°F) |
| `dew_point_2m_max` | Maximum dew point at 2 meters | °C (°F) |
| `dew_point_2m_min` | Minimum dew point at 2 meters | °C (°F) |
| `wet_bulb_temperature_2m_mean` | Mean wet bulb temperature at 2 meters | °C (°F) |
| `wet_bulb_temperature_2m_max` | Maximum wet bulb temperature at 2 meters | °C (°F) |
| `wet_bulb_temperature_2m_min` | Minimum wet bulb temperature at 2 meters | °C (°F) |
| `cape_mean` | Mean convective available potential energy | J/kg |
| `cape_max` | Maximum convective available potential energy | J/kg |
| `cape_min` | Minimum convective available potential energy | J/kg |
| `vapour_pressure_deficit_max` | Maximum vapor pressure deficit | kPa |
| `pressure_msl_mean` | Mean sea level pressure | hPa |
| `pressure_msl_max` | Maximum sea level pressure | hPa |
| `pressure_msl_min` | Minimum sea level pressure | hPa |
| `surface_pressure_mean` | Mean surface pressure | hPa |
| `surface_pressure_max` | Maximum surface pressure | hPa |
| `surface_pressure_min` | Minimum surface pressure | hPa |
| `visibility_mean` | Mean visibility | meters |
| `visibility_min` | Minimum visibility | meters |
| `visibility_max` | Maximum visibility | meters |
| `snowfall_water_equivalent_sum` | Water equivalent of daily snowfall | mm |
| `precipitation_probability_mean` | Mean precipitation probability | % |
| `precipitation_probability_min` | Minimum precipitation probability | % |
| `leaf_wetness_probability_mean` | Mean probability of leaf surface wetness | % |
| `growing_degree_days_base_0_limit_50` | Growing degree days (base 0°C, limit 50°C) | °C·day |
| `updraft_max` | Maximum updraft speed | m/s |

### 1.4 Current Variables (`current=`)

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m` | Air temperature at 2 meters above ground | °C (°F) |
| `relative_humidity_2m` | Relative humidity at 2 meters above ground | % |
| `apparent_temperature` | Apparent feels-like temperature | °C (°F) |
| `is_day` | 1 if daylight, 0 at night | Dimensionless |
| `precipitation` | Current precipitation | mm |
| `rain` | Current rain | mm |
| `showers` | Current showers | mm |
| `snowfall` | Current snowfall | cm |
| `weather_code` | Weather condition as numeric code (WMO) | WMO code |
| `cloud_cover` | Total cloud cover | % |
| `pressure_msl` | Atmospheric pressure reduced to mean sea level | hPa |
| `surface_pressure` | Atmospheric pressure at surface | hPa |
| `wind_speed_10m` | Wind speed at 10 meters above ground | km/h (mph, m/s, knots) |
| `wind_direction_10m` | Wind direction at 10 meters above ground | ° |
| `wind_gusts_10m` | Wind gusts at 10 meters above ground | km/h (mph, m/s, knots) |

> Note: All hourly variables can also be queried as `current` variables; the values above are the standard set.

### 1.5 Pressure Level Variables (`hourly=`)

Append pressure level in hPa to variable name, e.g. `temperature_850hPa`.

**Available pressure levels:** 1000, 975, 950, 925, 900, 850, 800, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30 hPa

| Parameter Pattern | Description | Unit |
|-------------------|-------------|------|
| `temperature_[hPa]` | Air temperature at the specified pressure level | °C (°F) |
| `relative_humidity_[hPa]` | Relative humidity at the specified pressure level | % |
| `dew_point_[hPa]` | Dew point temperature at the specified pressure level | °C (°F) |
| `cloud_cover_[hPa]` | Cloud cover fraction at the specified pressure level | % |
| `wind_speed_[hPa]` | Wind speed at the specified pressure level | km/h (mph, m/s, knots) |
| `wind_direction_[hPa]` | Wind direction at the specified pressure level | ° |
| `geopotential_height_[hPa]` | Geopotential height at the specified pressure level | meters |

---

## 2. Historical Weather API

**Base URL:** `https://archive-api.open-meteo.com/v1/archive`

Data from ERA5 and ERA5-Land reanalysis, available from 1940 onward.

### 2.1 Hourly Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m` | Air temperature at 2 meters above ground | °C (°F) |
| `relative_humidity_2m` | Relative humidity at 2 meters above ground | % |
| `dew_point_2m` | Dew point temperature at 2 meters above ground | °C (°F) |
| `apparent_temperature` | Perceived feels-like temperature | °C (°F) |
| `pressure_msl` | Atmospheric air pressure reduced to mean sea level | hPa |
| `surface_pressure` | Pressure at surface | hPa |
| `precipitation` | Total precipitation sum of the preceding hour | mm (inch) |
| `rain` | Liquid precipitation including local showers in the preceding hour | mm (inch) |
| `snowfall` | Snowfall amount of the preceding hour | cm (inch) |
| `cloud_cover` | Total cloud cover as an area fraction | % |
| `cloud_cover_low` | Low level clouds and fog up to 2 km altitude | % |
| `cloud_cover_mid` | Mid level clouds from 2 to 6 km altitude | % |
| `cloud_cover_high` | High level clouds from 6 km altitude | % |
| `shortwave_radiation` | Shortwave solar radiation as average of the preceding hour | W/m² |
| `direct_radiation` | Direct solar radiation as average of the preceding hour on horizontal plane | W/m² |
| `direct_normal_irradiance` | Direct solar radiation on the normal plane (perpendicular to the sun) | W/m² |
| `diffuse_radiation` | Diffuse solar radiation as average of the preceding hour | W/m² |
| `global_tilted_irradiance` | Total radiation received on a tilted pane as average of the preceding hour | W/m² |
| `sunshine_duration` | Number of seconds of sunshine in the preceding hour | seconds |
| `wind_speed_10m` | Wind speed at 10 meters above ground | km/h (mph, m/s, knots) |
| `wind_speed_100m` | Wind speed at 100 meters above ground | km/h (mph, m/s, knots) |
| `wind_direction_10m` | Wind direction at 10 meters above ground | ° |
| `wind_direction_100m` | Wind direction at 100 meters above ground | ° |
| `wind_gusts_10m` | Gusts at 10 meters above ground in the indicated hour | km/h (mph, m/s, knots) |
| `et0_fao_evapotranspiration` | ET₀ Reference Evapotranspiration of a well watered grass field | mm (inch) |
| `vapour_pressure_deficit` | Vapor pressure deficit | kPa |
| `weather_code` | Weather condition as a numeric code (WMO) | WMO code |
| `snow_depth` | Snow depth on the ground | meters |
| `soil_temperature_0_to_7cm` | Average soil temperature at 0–7 cm depth | °C (°F) |
| `soil_temperature_7_to_28cm` | Average soil temperature at 7–28 cm depth | °C (°F) |
| `soil_temperature_28_to_100cm` | Average soil temperature at 28–100 cm depth | °C (°F) |
| `soil_temperature_100_to_255cm` | Average soil temperature at 100–255 cm depth | °C (°F) |
| `soil_moisture_0_to_7cm` | Average soil water content as volumetric mixing ratio at 0–7 cm | m³/m³ |
| `soil_moisture_7_to_28cm` | Soil water content at 7–28 cm depth | m³/m³ |
| `soil_moisture_28_to_100cm` | Soil water content at 28–100 cm depth | m³/m³ |
| `soil_moisture_100_to_255cm` | Soil water content at 100–255 cm depth | m³/m³ |

### 2.2 Daily Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `weather_code` | The most severe weather condition on a given day | WMO code |
| `temperature_2m_max` | Maximum daily air temperature at 2 meters | °C (°F) |
| `temperature_2m_min` | Minimum daily air temperature at 2 meters | °C (°F) |
| `apparent_temperature_max` | Maximum daily apparent temperature | °C (°F) |
| `apparent_temperature_min` | Minimum daily apparent temperature | °C (°F) |
| `precipitation_sum` | Sum of daily precipitation | mm |
| `rain_sum` | Sum of daily rain | mm |
| `snowfall_sum` | Sum of daily snowfall | cm |
| `precipitation_hours` | Number of hours with rain | hours |
| `sunrise` | Time of sunrise | ISO 8601 |
| `sunset` | Time of sunset | ISO 8601 |
| `daylight_duration` | Number of seconds of daylight per day | seconds |
| `sunshine_duration` | Number of seconds of sunshine per day | seconds |
| `wind_speed_10m_max` | Maximum wind speed during the day | km/h (mph, m/s, knots) |
| `wind_gusts_10m_max` | Maximum wind gusts during the day | km/h (mph, m/s, knots) |
| `wind_direction_10m_dominant` | Dominant wind direction | ° |
| `shortwave_radiation_sum` | Sum of solar radiation on a given day | MJ/m² |
| `et0_fao_evapotranspiration` | Daily sum of ET₀ Reference Evapotranspiration | mm |

---

## 3. Historical Forecast API

**Base URL:** `https://historical-forecast-api.open-meteo.com/v1/forecast`

Archived numerical weather prediction model data (not reanalysis). Shares the same variable set as the standard Forecast API but for past dates.

### 3.1 Hourly Variables

All variables from Section 1.1 (Forecast API Hourly) apply, plus:

| Parameter | Description | Unit |
|-----------|-------------|------|
| `hail` | Hail probability (Met Office UK 2km model only) | % |
| `lightning_potential` | Lightning Potential Index | J/kg |

### 3.2 15-Minutely Variables

Same as Section 1.2 (Forecast API 15-minutely).

### 3.3 Daily Variables

Same as Section 1.3 (Forecast API daily), plus the extended soil variables:

| Parameter | Description | Unit |
|-----------|-------------|------|
| `soil_moisture_0_100cm_mean` | Mean soil moisture 0–100 cm | m³/m³ |
| `soil_moisture_0_10cm_mean` | Mean soil moisture 0–10 cm | m³/m³ |
| `soil_moisture_0_7cm_mean` | Mean soil moisture 0–7 cm | m³/m³ |
| `soil_moisture_28_100cm_mean` | Mean soil moisture 28–100 cm | m³/m³ |
| `soil_moisture_7_28cm_mean` | Mean soil moisture 7–28 cm | m³/m³ |
| `soil_temperature_0_100cm_mean` | Mean soil temperature 0–100 cm | °C |
| `soil_temperature_0_7cm_mean` | Mean soil temperature 0–7 cm | °C |
| `soil_temperature_28_100cm_mean` | Mean soil temperature 28–100 cm | °C |
| `soil_temperature_7_28cm_mean` | Mean soil temperature 7–28 cm | °C |

### 3.4 Pressure Level Variables

Same as Section 1.5 (same pressure levels and variable patterns).

---

## 4. Marine Weather API

**Base URL:** `https://marine-api.open-meteo.com/v1/marine`

### 4.1 Hourly Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `wave_height` | Significant mean wave height (combined wind and swell) | meters |
| `wind_wave_height` | Significant wind wave height | meters |
| `swell_wave_height` | Significant primary swell wave height | meters |
| `secondary_swell_wave_height` | Significant secondary swell wave height | meters |
| `tertiary_swell_wave_height` | Significant tertiary swell wave height | meters |
| `wave_direction` | Mean direction of combined waves | ° |
| `wind_wave_direction` | Wind wave direction | ° |
| `swell_wave_direction` | Primary swell wave direction | ° |
| `secondary_swell_wave_direction` | Secondary swell wave direction | ° |
| `tertiary_swell_wave_direction` | Tertiary swell wave direction | ° |
| `wave_period` | Mean period between combined waves | seconds |
| `wind_wave_period` | Wind wave period | seconds |
| `swell_wave_period` | Primary swell wave period | seconds |
| `secondary_swell_wave_period` | Secondary swell wave period | seconds |
| `tertiary_swell_wave_period` | Tertiary swell wave period | seconds |
| `wind_wave_peak_period` | Peak period for wind waves | seconds |
| `swell_wave_peak_period` | Peak period for swell waves | seconds |
| `ocean_current_velocity` | Velocity of ocean current (includes tidal effects) | km/h (mph, m/s, knots) |
| `ocean_current_direction` | Direction of ocean current flow | ° |
| `sea_surface_temperature` | Temperature near the water surface | °C |
| `sea_level_height_msl` | Sea level height accounting for tides and atmospheric pressure | meters |
| `invert_barometer_height` | Inverse barometer effect on sea level from pressure anomalies | meters |

### 4.2 Daily Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `wave_height_max` | Maximum wave height during the day | meters |
| `wind_wave_height_max` | Maximum wind wave height during the day | meters |
| `swell_wave_height_max` | Maximum swell wave height during the day | meters |
| `wave_direction_dominant` | Dominant wave direction during the day | ° |
| `wind_wave_direction_dominant` | Dominant wind wave direction during the day | ° |
| `swell_wave_direction_dominant` | Dominant swell wave direction during the day | ° |
| `wave_period_max` | Maximum wave period during the day | seconds |
| `wind_wave_period_max` | Maximum wind wave period during the day | seconds |
| `swell_wave_period_max` | Maximum swell wave period during the day | seconds |
| `wind_wave_peak_period_max` | Maximum wind wave peak period during the day | seconds |
| `swell_wave_peak_period_max` | Maximum swell wave peak period during the day | seconds |

> Note: All hourly variables are also available as current conditions using `current=`.

---

## 5. Air Quality API

**Base URL:** `https://air-quality-api.open-meteo.com/v1/air-quality`

Data sourced from the Copernicus Atmosphere Monitoring Service (CAMS).

### 5.1 Hourly Variables

#### Pollutants

| Parameter | Description | Unit |
|-----------|-------------|------|
| `pm10` | Particulate matter with diameter smaller than 10 µm near surface | µg/m³ |
| `pm2_5` | Particulate matter with diameter smaller than 2.5 µm near surface | µg/m³ |
| `carbon_monoxide` | Carbon monoxide (CO) concentration near surface | µg/m³ |
| `nitrogen_dioxide` | Nitrogen dioxide (NO₂) concentration near surface | µg/m³ |
| `nitrogen_monoxide` | Nitrogen monoxide (NO) concentration near surface | µg/m³ |
| `sulphur_dioxide` | Sulphur dioxide (SO₂) concentration near surface | µg/m³ |
| `ozone` | Ozone (O₃) concentration near surface | µg/m³ |
| `carbon_dioxide` | Carbon dioxide (CO₂) concentration near surface | ppm |
| `methane` | Methane (CH₄) concentration near surface | µg/m³ |
| `ammonia` | Ammonia (NH₃) concentration near surface (Europe only) | µg/m³ |
| `dust` | Saharan dust particle concentration near surface | µg/m³ |
| `formaldehyde` | Formaldehyde (CH₂O) concentration | µg/m³ |
| `glyoxal` | Glyoxal (C₂H₂O₂) concentration | µg/m³ |
| `non_methane_volatile_organic_compounds` | Non-methane volatile organic compounds (NMVOC) — Europe only | µg/m³ |
| `peroxyacyl_nitrates` | Peroxyacyl nitrates (PAN) concentration | µg/m³ |
| `sea_salt_aerosol` | Sea salt aerosol particle concentration near surface | µg/m³ |
| `aerosol_optical_depth` | Aerosol optical depth (haze indicator at 550 nm) for entire atmosphere | dimensionless |

#### Radiation

| Parameter | Description | Unit |
|-----------|-------------|------|
| `uv_index` | UV Index considering cloud coverage | Index (0–11+) |
| `uv_index_clear_sky` | UV Index in clear sky conditions | Index (0–11+) |

#### Pollen (Europe only, seasonal availability)

| Parameter | Description | Unit |
|-----------|-------------|------|
| `alder_pollen` | Alder pollen concentration | Grains/m³ |
| `birch_pollen` | Birch pollen concentration | Grains/m³ |
| `grass_pollen` | Grass pollen concentration | Grains/m³ |
| `mugwort_pollen` | Mugwort pollen concentration | Grains/m³ |
| `olive_pollen` | Olive pollen concentration | Grains/m³ |
| `ragweed_pollen` | Ragweed pollen concentration | Grains/m³ |

#### Air Quality Index (AQI)

| Parameter | Description | Scale |
|-----------|-------------|-------|
| `european_aqi` | Overall European AQI (worst pollutant) | 0–100+ |
| `european_aqi_pm2_5` | European AQI for PM2.5 | 0–100+ |
| `european_aqi_pm10` | European AQI for PM10 | 0–100+ |
| `european_aqi_nitrogen_dioxide` | European AQI for NO₂ | 0–100+ |
| `european_aqi_ozone` | European AQI for O₃ | 0–100+ |
| `european_aqi_sulphur_dioxide` | European AQI for SO₂ | 0–100+ |
| `us_aqi` | Overall U.S. AQI (worst pollutant) | 0–500 |
| `us_aqi_pm2_5` | U.S. AQI for PM2.5 | 0–500 |
| `us_aqi_pm10` | U.S. AQI for PM10 | 0–500 |
| `us_aqi_nitrogen_dioxide` | U.S. AQI for NO₂ | 0–500 |
| `us_aqi_ozone` | U.S. AQI for O₃ | 0–500 |
| `us_aqi_sulphur_dioxide` | U.S. AQI for SO₂ | 0–500 |
| `us_aqi_carbon_monoxide` | U.S. AQI for CO | 0–500 |

---

## 6. Flood API

**Base URL:** `https://flood-api.open-meteo.com/v1/flood`

Data sourced from the Global Flood Awareness System (GloFAS). River discharge at ~5 km resolution.

### 6.1 Daily Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `river_discharge` | Daily river discharge rate | m³/s |
| `river_discharge_mean` | Statistical mean from ensemble members for discharge rate | m³/s |
| `river_discharge_median` | Statistical median from ensemble members for discharge rate | m³/s |
| `river_discharge_max` | Maximum value across ensemble members | m³/s |
| `river_discharge_min` | Minimum value across ensemble members | m³/s |
| `river_discharge_p25` | 25th percentile across ensemble members | m³/s |
| `river_discharge_p75` | 75th percentile across ensemble members | m³/s |

> Note: Statistical ensemble variables (mean, median, max, min, p25, p75) are available for forecasts only, not for historical data.

---

## 7. Ensemble Forecast API

**Base URL:** `https://ensemble-api.open-meteo.com/v1/ensemble`

Provides probabilistic forecasts from multiple ensemble members. Supports models including ICON-EPS, GFS-Ensemble, ECMWF-IFS-Ensemble, and others.

### 7.1 Hourly Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m` | Air temperature at 2 meters above ground | °C (°F) |
| `relative_humidity_2m` | Relative humidity at 2 meters above ground | % |
| `dew_point_2m` | Dew point temperature at 2 meters above ground | °C (°F) |
| `apparent_temperature` | Apparent temperature combining wind chill, humidity, and solar effects | °C (°F) |
| `pressure_msl` | Atmospheric air pressure reduced to mean sea level | hPa |
| `surface_pressure` | Pressure measured at ground surface | hPa |
| `cloud_cover` | Total cloud cover as an area fraction | % |
| `wind_speed_10m` | Wind speed at 10 meters above ground | km/h (mph, m/s, knots) |
| `wind_speed_80m` | Wind speed at 80 meters above ground | km/h (mph, m/s, knots) |
| `wind_speed_100m` | Wind speed at 100 meters above ground | km/h (mph, m/s, knots) |
| `wind_speed_120m` | Wind speed at 120 meters above ground | km/h (mph, m/s, knots) |
| `wind_direction_10m` | Wind direction at 10 meters above ground | ° |
| `wind_direction_80m` | Wind direction at 80 meters above ground | ° |
| `wind_direction_100m` | Wind direction at 100 meters above ground | ° |
| `wind_direction_120m` | Wind direction at 120 meters above ground | ° |
| `wind_gusts_10m` | Gusts at 10 meters as maximum of the preceding hour | km/h (mph, m/s, knots) |
| `shortwave_radiation` | Solar radiation averaged over preceding hour | W/m² |
| `direct_radiation` | Direct solar radiation on horizontal plane | W/m² |
| `direct_normal_irradiance` | Direct solar radiation perpendicular to the sun | W/m² |
| `diffuse_radiation` | Diffuse solar radiation from sky | W/m² |
| `global_tilted_irradiance` | Total radiation on a tilted panel surface | W/m² |
| `sunshine_duration` | Seconds of sunshine exceeding 120 W/m² following WMO definition | seconds |
| `vapour_pressure_deficit` | Vapor pressure deficit (water stress indicator) | kPa |
| `evapotranspiration` | Water loss from soil and plants | mm (inch) |
| `et0_fao_evapotranspiration` | ET₀ Reference Evapotranspiration of a well watered grass field | mm (inch) |
| `weather_code` | Weather condition as numeric code (WMO) | WMO code |
| `precipitation` | Total precipitation sum of preceding hour | mm (inch) |
| `rain` | Liquid precipitation of preceding hour | mm (inch) |
| `snowfall` | Frozen precipitation depth in preceding hour | cm (inch) |
| `snow_depth` | Snow depth on the ground | meters |
| `freezing_level_height` | Altitude above sea level of the 0°C level | meters |
| `visibility` | Viewing distance | meters |
| `cape` | Convective available potential energy | J/kg |
| `surface_temperature` | Temperature at the topmost soil layer | °C (°F) |
| `soil_temperature_0_to_10cm` | Soil temperature at 0–10 cm depth | °C (°F) |
| `soil_temperature_10_to_40cm` | Soil temperature at 10–40 cm depth | °C (°F) |
| `soil_temperature_40_to_100cm` | Soil temperature at 40–100 cm depth | °C (°F) |
| `soil_temperature_100_to_200cm` | Soil temperature at 100–200 cm depth | °C (°F) |
| `soil_moisture_0_to_10cm` | Soil water content at 0–10 cm depth | m³/m³ |
| `soil_moisture_10_to_40cm` | Soil water content at 10–40 cm depth | m³/m³ |
| `soil_moisture_40_to_100cm` | Soil water content at 40–100 cm depth | m³/m³ |
| `soil_moisture_100_to_200cm` | Soil water content at 100–200 cm depth | m³/m³ |

### 7.2 Daily Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m_max` | Maximum daily air temperature at 2 meters | °C (°F) |
| `temperature_2m_mean` | Mean daily air temperature at 2 meters | °C (°F) |
| `temperature_2m_min` | Minimum daily air temperature at 2 meters | °C (°F) |
| `apparent_temperature_max` | Maximum daily apparent temperature | °C (°F) |
| `apparent_temperature_mean` | Mean daily apparent temperature | °C (°F) |
| `apparent_temperature_min` | Minimum daily apparent temperature | °C (°F) |
| `cloud_cover_max` | Maximum daily cloud cover | % |
| `cloud_cover_mean` | Mean daily cloud cover | % |
| `cloud_cover_min` | Minimum daily cloud cover | % |
| `relative_humidity_2m_max` | Maximum daily relative humidity | % |
| `relative_humidity_2m_mean` | Mean daily relative humidity | % |
| `relative_humidity_2m_min` | Minimum daily relative humidity | % |
| `dew_point_2m_max` | Maximum daily dew point | °C (°F) |
| `dew_point_2m_mean` | Mean daily dew point | °C (°F) |
| `dew_point_2m_min` | Minimum daily dew point | °C (°F) |
| `rain_sum` | Daily rainfall total | mm |
| `showers_sum` | Daily shower total | mm |
| `snowfall_sum` | Daily snowfall total | cm |
| `precipitation_sum` | Daily total precipitation | mm |
| `precipitation_hours` | Hours with measurable rain | hours |
| `pressure_msl_max` | Maximum daily sea-level pressure | hPa |
| `pressure_msl_mean` | Mean daily sea-level pressure | hPa |
| `pressure_msl_min` | Minimum daily sea-level pressure | hPa |
| `surface_pressure_max` | Maximum daily surface pressure | hPa |
| `surface_pressure_mean` | Mean daily surface pressure | hPa |
| `surface_pressure_min` | Minimum daily surface pressure | hPa |
| `wind_speed_10m_max` | Maximum daily wind speed at 10 meters | km/h (mph, m/s, knots) |
| `wind_speed_10m_mean` | Mean daily wind speed at 10 meters | km/h (mph, m/s, knots) |
| `wind_speed_10m_min` | Minimum daily wind speed at 10 meters | km/h (mph, m/s, knots) |
| `wind_gusts_10m_max` | Maximum daily wind gusts | km/h (mph, m/s, knots) |
| `wind_gusts_10m_mean` | Mean daily wind gusts | km/h (mph, m/s, knots) |
| `wind_gusts_10m_min` | Minimum daily wind gusts | km/h (mph, m/s, knots) |
| `wind_direction_10m_dominant` | Prevailing wind direction | ° |
| `wind_direction_100m_dominant` | Prevailing wind direction at 100 meters | ° |
| `shortwave_radiation_sum` | Daily solar radiation total | MJ/m² |
| `cape_max` | Maximum daily convective energy | J/kg |
| `cape_mean` | Mean daily convective energy | J/kg |
| `cape_min` | Minimum daily convective energy | J/kg |
| `et0_fao_evapotranspiration` | Daily reference evapotranspiration sum | mm |

---

## 8. Seasonal Forecast API

**Base URL:** `https://seasonal-api.open-meteo.com/v1/seasonal`

Long-range probabilistic forecasts up to 7 months ahead. Models: ECMWF SEAS5 (EC46), NCEP CFSv2, and others.

### 8.1 6-Hourly Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m` | Temperature at 2 meters | °C |
| `temperature_2m_max_6h` | Maximum temperature over 6-hour interval at 2 meters | °C |
| `temperature_2m_min_6h` | Minimum temperature over 6-hour interval at 2 meters | °C |
| `dew_point_2m` | Dew point at 2 meters | °C |
| `relative_humidity_2m` | Relative humidity at 2 meters | % |
| `apparent_temperature_2m` | Perceived temperature at 2 meters | °C |
| `reference_evapotranspiration` | ET₀ reference evapotranspiration | mm |
| `vapour_pressure_deficit` | Vapor pressure deficit | hPa |
| `sea_level_pressure` | Atmospheric pressure at sea level | hPa |
| `weather_code` | WMO weather condition code | code |
| `precipitation` | Total precipitation amount | mm |
| `showers` | Shower precipitation (EC46 only) | mm |
| `snowfall` | Snow accumulation | cm |
| `rain` | Liquid precipitation | mm |
| `wave_height` | Ocean wave height (EC46 only) | meters |
| `wave_direction` | Ocean wave direction (EC46 only) | ° |
| `wave_period` | Ocean wave period (EC46 only) | seconds |
| `wave_peak_period` | Peak wave period (EC46 only) | seconds |
| `cloud_cover` | Total cloud coverage | % |
| `sunshine_duration` | Hours of sunshine (EC46 only) | hours |
| `wind_speed_10m` | Wind speed at 10 meters | km/h |
| `wind_speed_100m` | Wind speed at 100 meters | km/h |
| `wind_speed_200m` | Wind speed at 200 meters | km/h |
| `wind_direction_10m` | Wind direction at 10 meters | ° |
| `wind_direction_100m` | Wind direction at 100 meters | ° |
| `wind_direction_200m` | Wind direction at 200 meters | ° |
| `wind_gusts_10m` | Wind gust speed at 10 meters (EC46 only) | km/h |
| `sea_surface_temperature` | Ocean water surface temperature | °C |
| `soil_temperature_0_to_7cm` | Soil temperature at 0–7 cm depth | °C |
| `soil_temperature_7_to_28cm` | Soil temperature at 7–28 cm depth (EC46 only) | °C |
| `soil_temperature_28_to_100cm` | Soil temperature at 28–100 cm depth (EC46 only) | °C |
| `soil_temperature_100_to_255cm` | Soil temperature at 100–255 cm depth (EC46 only) | °C |
| `soil_moisture_0_to_7cm` | Soil water content at 0–7 cm (EC46 only) | m³/m³ |
| `soil_moisture_7_to_28cm` | Soil water content at 7–28 cm (EC46 only) | m³/m³ |
| `soil_moisture_28_to_100cm` | Soil water content at 28–100 cm (EC46 only) | m³/m³ |
| `soil_moisture_100_to_255cm` | Soil water content at 100–255 cm (EC46 only) | m³/m³ |

#### Solar Radiation (6-Hourly)

| Parameter | Description | Unit |
|-----------|-------------|------|
| `shortwave_radiation_ghi` | Global horizontal irradiance | W/m² |
| `direct_solar_radiation` | Direct beam solar radiation | W/m² |
| `diffuse_radiation_dhi` | Diffuse horizontal irradiance | W/m² |
| `direct_normal_irradiance_dni` | Direct normal irradiance | W/m² |
| `global_tilted_radiation_gti` | Irradiance on a tilted panel | W/m² |
| `terrestrial_solar_radiation` | Surface solar radiation | W/m² |
| `shortwave_radiation_ghi_instant` | Instantaneous global horizontal irradiance | W/m² |
| `direct_solar_radiation_instant` | Instantaneous direct radiation | W/m² |
| `diffuse_radiation_dhi_instant` | Instantaneous diffuse irradiance | W/m² |
| `direct_normal_irradiance_dni_instant` | Instantaneous direct normal irradiance | W/m² |
| `global_tilted_radiation_gti_instant` | Instantaneous tilted panel irradiance | W/m² |
| `terrestrial_solar_radiation_instant` | Instantaneous terrestrial radiation | W/m² |

### 8.2 Daily Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m_max` | Daily maximum temperature | °C |
| `temperature_2m_mean` | Daily mean temperature | °C |
| `temperature_2m_min` | Daily minimum temperature | °C |
| `apparent_temperature_max` | Maximum perceived temperature | °C |
| `apparent_temperature_mean` | Mean perceived temperature | °C |
| `apparent_temperature_min` | Minimum perceived temperature | °C |
| `relative_humidity_2m_max` | Maximum daily humidity | % |
| `relative_humidity_2m_mean` | Mean daily humidity | % |
| `relative_humidity_2m_min` | Minimum daily humidity | % |
| `dew_point_2m_max` | Maximum daily dew point | °C |
| `dew_point_2m_mean` | Mean daily dew point | °C |
| `dew_point_2m_min` | Minimum daily dew point | °C |
| `wet_bulb_temperature_2m_max` | Maximum daily wet bulb temperature | °C |
| `wet_bulb_temperature_2m_mean` | Mean daily wet bulb temperature | °C |
| `wet_bulb_temperature_2m_min` | Minimum daily wet bulb temperature | °C |
| `precipitation_sum` | Daily total precipitation | mm |
| `rain_sum` | Daily rainfall total | mm |
| `showers_sum` | Daily showers total | mm |
| `snowfall_sum` | Daily snowfall total | cm |
| `snowfall_water_equivalent_sum` | Daily snowfall water equivalent | mm |
| `cloud_cover_max` | Maximum daily cloud coverage | % |
| `cloud_cover_mean` | Mean daily cloud coverage | % |
| `cloud_cover_min` | Minimum daily cloud coverage | % |
| `sealevel_pressure_max` | Maximum sea level pressure | hPa |
| `sealevel_pressure_mean` | Mean sea level pressure | hPa |
| `sealevel_pressure_min` | Minimum sea level pressure | hPa |
| `surface_pressure_max` | Maximum surface pressure | hPa |
| `surface_pressure_mean` | Mean surface pressure | hPa |
| `surface_pressure_min` | Minimum surface pressure | hPa |
| `vapour_pressure_deficit_max` | Maximum vapor pressure deficit | hPa |
| `vapour_pressure_deficit_mean` | Mean vapor pressure deficit | hPa |
| `vapour_pressure_deficit_min` | Minimum vapor pressure deficit | hPa |
| `wind_speed_10m_max` | Maximum wind speed at 10 meters | km/h |
| `wind_speed_10m_mean` | Mean wind speed at 10 meters | km/h |
| `wind_speed_10m_min` | Minimum wind speed at 10 meters | km/h |
| `wind_speed_100m_max` | Maximum wind speed at 100 meters (EC46 only) | km/h |
| `wind_speed_100m_mean` | Mean wind speed at 100 meters (EC46 only) | km/h |
| `wind_speed_100m_min` | Minimum wind speed at 100 meters (EC46 only) | km/h |
| `wind_speed_200m_max` | Maximum wind speed at 200 meters (EC46 only) | km/h |
| `wind_speed_200m_mean` | Mean wind speed at 200 meters (EC46 only) | km/h |
| `wind_speed_200m_min` | Minimum wind speed at 200 meters (EC46 only) | km/h |
| `wind_gusts_10m_max` | Maximum wind gusts at 10 meters (EC46 only) | km/h |
| `wind_gusts_10m_mean` | Mean wind gusts at 10 meters (EC46 only) | km/h |
| `wind_gusts_10m_min` | Minimum wind gusts at 10 meters (EC46 only) | km/h |
| `wind_direction_10m_dominant` | Dominant wind direction at 10 meters | ° |
| `wind_direction_100m_dominant` | Dominant wind direction at 100 meters (EC46 only) | ° |
| `wind_direction_200m_dominant` | Dominant wind direction at 200 meters (EC46 only) | ° |
| `sea_surface_temperature_max` | Maximum daily ocean surface temperature | °C |
| `sea_surface_temperature_mean` | Mean daily ocean surface temperature | °C |
| `sea_surface_temperature_min` | Minimum daily ocean surface temperature | °C |
| `reference_evapotranspiration_sum` | Daily ET₀ total | mm |
| `shortwave_radiation_sum` | Daily shortwave radiation total | MJ/m² |
| `sunrise` | Time of sunrise | ISO 8601 |
| `sunset` | Time of sunset | ISO 8601 |
| `weather_code` | Daily weather condition code | WMO code |
| `soil_temperature_0_to_7cm_mean` | Mean soil temperature 0–7 cm | °C |
| `soil_temperature_7_to_28cm_mean` | Mean soil temperature 7–28 cm | °C |
| `soil_temperature_28_to_100cm_mean` | Mean soil temperature 28–100 cm | °C |
| `soil_temperature_100_to_255cm_mean` | Mean soil temperature 100–255 cm | °C |
| `soil_moisture_0_to_7cm_mean` | Mean soil moisture 0–7 cm | m³/m³ |
| `soil_moisture_7_to_28cm_mean` | Mean soil moisture 7–28 cm | m³/m³ |
| `soil_moisture_28_to_100cm_mean` | Mean soil moisture 28–100 cm | m³/m³ |
| `soil_moisture_100_to_255cm_mean` | Mean soil moisture 100–255 cm | m³/m³ |

### 8.3 Weekly Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m_mean` | Weekly mean temperature | °C |
| `temperature_2m_anomaly` | Temperature departure from climatology | °C |
| `temperature_2m_max_6h_mean` | Weekly mean of 6-hour max temperatures | °C |
| `temperature_2m_max_6h_anomaly` | Anomaly for 6-hour max temperatures | °C |
| `temperature_2m_min_6h_mean` | Weekly mean of 6-hour min temperatures | °C |
| `temperature_2m_min_6h_anomaly` | Anomaly for 6-hour min temperatures | °C |
| `dew_point_2m_mean` | Weekly mean dew point | °C |
| `dew_point_2m_anomaly` | Dew point anomaly vs climatology | °C |
| `soil_temperature_0_to_7cm_mean` | Weekly mean soil temperature 0–7 cm | °C |
| `soil_temperature_0_to_7cm_anomaly` | Soil temperature anomaly 0–7 cm | °C |
| `precipitation_mean` | Weekly mean precipitation | mm |
| `precipitation_anomaly` | Precipitation anomaly vs climatology | mm |
| `snowfall_mean` | Weekly mean snowfall | cm |
| `snowfall_anomaly` | Snowfall anomaly vs climatology | cm |
| `snow_depth_mean` | Weekly mean snow depth | cm |
| `snow_depth_anomaly` | Snow depth anomaly vs climatology | cm |
| `pressure_msl_mean` | Weekly mean sea level pressure | hPa |
| `pressure_msl_anomaly` | Sea level pressure anomaly | hPa |
| `sea_surface_temperature_mean` | Weekly mean ocean surface temperature | °C |
| `sea_surface_temperature_anomaly` | Ocean temperature anomaly | °C |
| `sunshine_duration_mean` | Weekly mean sunshine hours | hours |
| `sunshine_duration_anomaly` | Sunshine duration anomaly | hours |
| `cloud_cover_mean` | Weekly mean cloud coverage | % |
| `cloud_cover_anomaly` | Cloud coverage anomaly | % |
| `wind_speed_10m_mean` | Weekly mean wind speed at 10 meters | km/h |
| `wind_speed_10m_anomaly` | Wind speed anomaly at 10 meters | km/h |
| `wind_speed_100m_mean` | Weekly mean wind speed at 100 meters | km/h |
| `wind_speed_100m_anomaly` | Wind speed anomaly at 100 meters | km/h |
| `wind_direction_10m_mean` | Weekly mean wind direction at 10 meters | ° |
| `wind_direction_10m_anomaly` | Wind direction anomaly | ° |
| `wind_direction_100m_mean` | Weekly mean wind direction at 100 meters | ° |
| `wind_direction_100m_anomaly` | Wind direction anomaly at 100 meters | ° |
| `snow_density_mean` | Weekly mean snow density | kg/m³ |
| `snow_density_anomaly` | Snow density anomaly | kg/m³ |
| `snow_depth_water_equivalent_mean` | Weekly mean snow water equivalent | mm |
| `snow_depth_water_equivalent_anomaly` | Snow water equivalent anomaly | mm |
| `snowfall_water_equivalent_mean` | Weekly mean snowfall water equivalent | mm |
| `snowfall_water_equivalent_anomaly` | Snowfall water equivalent anomaly | mm |
| `total_column_integrated_water_vapour_mean` | Weekly mean atmospheric water vapor column | kg/m² |
| `total_column_integrated_water_vapour_anomaly` | Atmospheric water vapor anomaly | kg/m² |

#### Weekly Extreme Forecast Indices (EFI) and Shift of Tails (SOT)

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m_extreme_forecast_index` | EFI for temperature extremes | –1 to +1 |
| `temperature_2m_shift_of_tails_10` | SOT for 10th percentile temperature | std. dev. |
| `temperature_2m_shift_of_tails_90` | SOT for 90th percentile temperature | std. dev. |
| `temperature_2m_anomaly_gt_0k` | Probability temperature anomaly > 0 K | % |
| `temperature_2m_anomaly_gt_1k` | Probability temperature anomaly > +1 K | % |
| `temperature_2m_anomaly_gt_2k` | Probability temperature anomaly > +2 K | % |
| `temperature_2m_anomaly_lt_minus_1k` | Probability temperature anomaly < –1 K | % |
| `temperature_2m_anomaly_lt_minus_2k` | Probability temperature anomaly < –2 K | % |
| `precipitation_extreme_forecast_index` | EFI for precipitation extremes | –1 to +1 |
| `precipitation_shift_of_tails_90` | SOT for 90th percentile precipitation | std. dev. |
| `precipitation_anomaly_gt_0mm` | Probability precipitation > climatology | % |
| `precipitation_anomaly_gt_10mm` | Probability precipitation anomaly > 10 mm | % |
| `precipitation_anomaly_gt_20mm` | Probability precipitation anomaly > 20 mm | % |
| `pressure_msl_anomaly_gt_0pa` | Probability sea level pressure > climatology | % |
| `surface_temperature_anomaly_gt_0k` | Probability surface temperature > climatology | % |

### 8.4 Monthly Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m_mean` | Monthly mean temperature | °C |
| `temperature_2m_anomaly` | Temperature anomaly vs climatology | °C |
| `temperature_2m_max_24h_mean` | Monthly mean daily maximum temperature | °C |
| `temperature_2m_max_24h_anomaly` | Daily max temperature anomaly | °C |
| `temperature_2m_min_24h_mean` | Monthly mean daily minimum temperature | °C |
| `temperature_2m_min_24h_anomaly` | Daily min temperature anomaly | °C |
| `dew_point_2m_mean` | Monthly mean dew point | °C |
| `dew_point_2m_anomaly` | Dew point anomaly | °C |
| `precipitation_mean` | Monthly mean precipitation | mm |
| `precipitation_anomaly` | Precipitation anomaly | mm |
| `showers_mean` | Monthly mean showers | mm |
| `showers_anomaly` | Shower precipitation anomaly | mm |
| `snowfall_mean` | Monthly mean snowfall | cm |
| `snowfall_anomaly` | Snowfall anomaly | cm |
| `snow_depth_mean` | Monthly mean snow depth | cm |
| `snow_depth_anomaly` | Snow depth anomaly | cm |
| `cloud_cover_mean` | Monthly mean cloud coverage | % |
| `cloud_cover_anomaly` | Cloud coverage anomaly | % |
| `cloud_cover_low_mean` | Monthly mean low cloud cover | % |
| `cloud_cover_low_anomaly` | Low cloud cover anomaly | % |
| `sunshine_duration_mean` | Monthly mean sunshine hours | hours |
| `sunshine_duration_anomaly` | Sunshine duration anomaly | hours |
| `shortwave_radiation_mean` | Monthly mean shortwave radiation | MJ/m² |
| `shortwave_radiation_anomaly` | Shortwave radiation anomaly | MJ/m² |
| `sealevel_pressure_mean` | Monthly mean sea level pressure | hPa |
| `sealevel_pressure_anomaly` | Sea level pressure anomaly | hPa |
| `sea_surface_temperature_mean` | Monthly mean ocean surface temperature | °C |
| `sea_surface_temperature_anomaly` | Ocean surface temperature anomaly | °C |
| `sea_ice_cover_mean` | Monthly mean sea ice extent | % |
| `sea_ice_cover_anomaly` | Sea ice coverage anomaly | % |
| `wind_speed_10m_mean` | Monthly mean wind speed at 10 meters | km/h |
| `wind_speed_10m_anomaly` | Wind speed anomaly at 10 meters | km/h |
| `wind_gusts_10m_anomaly` | Wind gust anomaly at 10 meters | km/h |
| `longwave_radiation_mean` | Monthly mean longwave (outgoing) radiation | MJ/m² |
| `longwave_radiation_anomaly` | Longwave radiation anomaly | MJ/m² |
| `albedo_mean` | Monthly mean surface reflectivity | 0–1 |
| `albedo_anomaly` | Surface reflectivity anomaly | 0–1 |
| `latent_heat_flux_mean` | Monthly mean latent heat flux | W/m² |
| `latent_heat_flux_anomaly` | Latent heat flux anomaly | W/m² |
| `sensible_heat_flux_mean` | Monthly mean sensible heat flux | W/m² |
| `sensible_heat_flux_anomaly` | Sensible heat flux anomaly | W/m² |
| `runoff_mean` | Monthly mean surface and subsurface runoff | mm |
| `runoff_anomaly` | Runoff anomaly | mm |
| `evapotranspiration_mean` | Monthly mean evapotranspiration | mm |
| `evapotranspiration_anomaly` | Evapotranspiration anomaly | mm |
| `snow_density_mean` | Monthly mean snow density | kg/m³ |
| `snow_density_anomaly` | Snow density anomaly | kg/m³ |
| `snow_depth_water_equivalent_mean` | Monthly mean snow water equivalent | mm |
| `snow_depth_water_equivalent_anomaly` | Snow water equivalent anomaly | mm |
| `snowfall_water_equivalent_mean` | Monthly mean snowfall water equivalent | mm |
| `snowfall_water_equivalent_anomaly` | Snowfall water equivalent anomaly | mm |
| `total_column_integrated_water_vapour_mean` | Monthly mean atmospheric water vapor column | kg/m² |
| `total_column_integrated_water_vapour_anomaly` | Atmospheric water vapor anomaly | kg/m² |
| `soil_temperature_0_to_7cm_mean` | Monthly mean soil temperature 0–7 cm | °C |
| `soil_temperature_0_to_7cm_anomaly` | Soil temperature anomaly 0–7 cm | °C |
| `soil_temperature_7_to_28cm_mean` | Monthly mean soil temperature 7–28 cm | °C |
| `soil_temperature_7_to_28cm_anomaly` | Soil temperature anomaly 7–28 cm | °C |
| `soil_temperature_28_to_100cm_mean` | Monthly mean soil temperature 28–100 cm | °C |
| `soil_temperature_28_to_100cm_anomaly` | Soil temperature anomaly 28–100 cm | °C |
| `soil_temperature_100_to_255cm_mean` | Monthly mean soil temperature 100–255 cm | °C |
| `soil_temperature_100_to_255cm_anomaly` | Soil temperature anomaly 100–255 cm | °C |
| `soil_moisture_0_to_7cm_mean` | Monthly mean soil moisture 0–7 cm | m³/m³ |
| `soil_moisture_0_to_7cm_anomaly` | Soil moisture anomaly 0–7 cm | m³/m³ |
| `soil_moisture_7_to_28cm_mean` | Monthly mean soil moisture 7–28 cm | m³/m³ |
| `soil_moisture_7_to_28cm_anomaly` | Soil moisture anomaly 7–28 cm | m³/m³ |
| `soil_moisture_28_to_100cm_mean` | Monthly mean soil moisture 28–100 cm | m³/m³ |
| `soil_moisture_28_to_100cm_anomaly` | Soil moisture anomaly 28–100 cm | m³/m³ |
| `soil_moisture_100_to_255cm_mean` | Monthly mean soil moisture 100–255 cm | m³/m³ |
| `soil_moisture_100_to_255cm_anomaly` | Soil moisture anomaly 100–255 cm | m³/m³ |

> Note: For all weekly and monthly variables, an ensemble spread (standard deviation across 51 ensemble members) can be retrieved by appending `_ensemble_spread` to any parameter name.

---

## 9. Climate API

**Base URL:** `https://climate-api.open-meteo.com/v1/climate`

Daily downscaled climate data from CMIP6 models covering 1950–2050 (historical + projections). Available models include MRI-AGCM3-2-S, NICAM16-8S, EC-Earth3P-HR, and others.

### 9.1 Daily Variables

| Parameter | Description | Unit |
|-----------|-------------|------|
| `temperature_2m_max` | Maximum daily air temperature at 2 meters | °C (°F) |
| `temperature_2m_min` | Minimum daily air temperature at 2 meters | °C (°F) |
| `temperature_2m_mean` | Mean daily air temperature at 2 meters | °C (°F) |
| `cloud_cover_mean` | Mean cloud cover on a given day | % |
| `relative_humidity_2m_max` | Maximum daily relative humidity at 2 meters | % |
| `relative_humidity_2m_min` | Minimum daily relative humidity at 2 meters | % |
| `relative_humidity_2m_mean` | Mean daily relative humidity at 2 meters | % |
| `soil_moisture_0_to_10cm_mean` | Daily mean soil moisture fraction within 0–10 cm | m³/m³ |
| `precipitation_sum` | Sum of daily precipitation (rain + showers + snowfall) | mm |
| `rain_sum` | Sum of daily liquid rain excluding snow | mm |
| `snowfall_sum` | Sum of daily snowfall | cm |
| `wind_speed_10m_mean` | Mean wind speed at 10 meters | km/h (mph, m/s, knots) |
| `wind_speed_10m_max` | Maximum wind speed at 10 meters | km/h (mph, m/s, knots) |
| `pressure_msl_mean` | Daily mean air pressure reduced to mean sea level | hPa |
| `shortwave_radiation_sum` | Sum of solar radiation on a given day | MJ/m² |

---

## 10. Geocoding API

**Base URL:** `https://geocoding-api.open-meteo.com/v1/search`

### 10.1 Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | String | Yes | Location name to search for (minimum 2 characters) |
| `count` | Integer | No | Number of results to return (default: 10, max: 100) |
| `language` | String | No | Return localized results if available (default: `en`) |
| `format` | String | No | Response format: `json` or protobuf (default: `json`) |
| `countryCode` | String | No | ISO 3166-1 alpha-2 country code to filter results |
| `apikey` | String | No | Required for commercial use |

### 10.2 Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Unique location identifier |
| `name` | String | Location name (localized) |
| `latitude` | Float | WGS84 latitude |
| `longitude` | Float | WGS84 longitude |
| `elevation` | Float | Elevation above mean sea level in meters |
| `timezone` | String | IANA time zone name |
| `feature_code` | String | GeoNames feature code (location type) |
| `country_code` | String | ISO 3166-1 2-character country code |
| `country` | String | Country name (localized) |
| `country_id` | Integer | Unique GeoNames country identifier |
| `population` | Integer | Number of inhabitants |
| `postcodes` | String[] | List of postal codes |
| `admin1` | String | Primary administrative division (state/province) |
| `admin2` | String | Secondary administrative division (county) |
| `admin3` | String | Third-level administrative division |
| `admin4` | String | Fourth-level administrative division |
| `admin1_id` | Integer | Identifier for admin1 |
| `admin2_id` | Integer | Identifier for admin2 |
| `admin3_id` | Integer | Identifier for admin3 |
| `admin4_id` | Integer | Identifier for admin4 |

---

## 11. Elevation API

**Base URL:** `https://api.open-meteo.com/v1/elevation`

### 11.1 Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `latitude` | Float or Float[] | Yes | WGS84 latitude; up to 100 comma-separated values |
| `longitude` | Float or Float[] | Yes | WGS84 longitude; up to 100 comma-separated values |
| `apikey` | String | No | Required for commercial use |

### 11.2 Response Fields

| Field | Type | Description | Unit |
|-------|------|-------------|------|
| `elevation` | Float[] | Terrain elevation based on Copernicus DEM 2021 GLO-90 (90m resolution) | meters |

---

## Appendix A: WMO Weather Interpretation Codes

The `weather_code` variable uses WMO code table 4677:

| Code | Description |
|------|-------------|
| 0 | Clear sky |
| 1, 2, 3 | Mainly clear, partly cloudy, overcast |
| 45, 48 | Fog, depositing rime fog |
| 51, 53, 55 | Drizzle: light, moderate, dense intensity |
| 56, 57 | Freezing drizzle: light, dense |
| 61, 63, 65 | Rain: slight, moderate, heavy |
| 66, 67 | Freezing rain: light, heavy |
| 71, 73, 75 | Snow fall: slight, moderate, heavy |
| 77 | Snow grains |
| 80, 81, 82 | Rain showers: slight, moderate, violent |
| 85, 86 | Snow showers: slight, heavy |
| 95 | Thunderstorm: slight or moderate |
| 96, 99 | Thunderstorm with slight or heavy hail |

---

## Appendix B: Common API Request Parameters (All Endpoints)

These parameters apply across most Open-Meteo APIs:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `latitude` | WGS84 latitude of location | Required |
| `longitude` | WGS84 longitude of location | Required |
| `elevation` | Override elevation in meters (default: auto from DEM) | auto |
| `hourly` | Comma-separated list of hourly variables | — |
| `daily` | Comma-separated list of daily variables | — |
| `current` | Comma-separated list of current variables | — |
| `temperature_unit` | `celsius` or `fahrenheit` | celsius |
| `wind_speed_unit` | `kmh`, `mph`, `ms`, or `kn` | kmh |
| `precipitation_unit` | `mm` or `inch` | mm |
| `timeformat` | `iso8601` or `unixtime` | iso8601 |
| `timezone` | IANA timezone (e.g. `America/New_York`) or `auto` | GMT |
| `past_days` | Number of past days to include (0–92) | 0 |
| `forecast_days` | Number of forecast days (0–16) | 7 |
| `start_date` | Start date in `YYYY-MM-DD` format | — |
| `end_date` | End date in `YYYY-MM-DD` format | — |
| `models` | Specific weather model(s) to use | auto |
| `cell_selection` | Grid cell selection: `land`, `sea`, or `nearest` | land |
| `apikey` | API key for commercial use | — |

---

*Sources: Open-Meteo official documentation at https://open-meteo.com/en/docs and its sub-pages for Marine, Air Quality, Historical, Historical Forecast, Flood, Ensemble, Seasonal, and Climate APIs.*

---

**Summary of what was compiled:**

- **Section 1** — Standard Forecast API: ~55 hourly, ~35 15-minutely, ~70+ daily, 15 current, and 7 pressure-level variables
- **Section 2** — Historical Weather API: 35 hourly + 18 daily ERA5-based variables
- **Section 3** — Historical Forecast API: same variable set as Forecast + soil mean daily aggregations
- **Section 4** — Marine API: 22 hourly + 11 daily ocean/wave variables
- **Section 5** — Air Quality API: 17 pollutant/aerosol variables, 2 UV variables, 6 pollen types, 13 AQI index variables
- **Section 6** — Flood API: 7 daily river discharge variables
- **Section 7** — Ensemble API: ~40 hourly + ~40 daily probabilistic variables
- **Section 8** — Seasonal Forecast API: 35 6-hourly, ~55 daily, ~40 weekly (with anomalies + EFI/SOT), ~60 monthly (with anomalies) variables
- **Section 9** — Climate API: 15 daily CMIP6-based variables
- **Sections 10–11** — Geocoding and Elevation utility APIs
- **Appendices** — WMO weather codes and universal request parameters