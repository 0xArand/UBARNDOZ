#!/usr/bin/env python3

import argparse
import sys
import requests

def get_coordinates(city_name: str):
    """
    Retrieves latitude, longitude, and country for a given city name using the Open-Meteo Geocoding API.
    """
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if not data.get("results"):
            return None, None, None
        result = data["results"][0]
        return result.get("latitude"), result.get("longitude"), result.get("country")
    except requests.exceptions.RequestException as e:
        print(f"Error during geocoding API request: {e}", file=sys.stderr)
        return None, None, None
    except (KeyError, IndexError, TypeError, ValueError) as e: # Added ValueError
        print(f"Error parsing geocoding API response: {e}", file=sys.stderr)
        return None, None, None

def get_weather(latitude: float, longitude: float):
    """
    Retrieves current weather data for given latitude and longitude using the Open-Meteo Forecast API.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "timezone": "auto"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if not data.get("current"):
            return None

        current_weather = data["current"]
        return {
            "temperature_2m": current_weather.get("temperature_2m"),
            "relative_humidity_2m": current_weather.get("relative_humidity_2m"),
            "weather_code": current_weather.get("weather_code"),
            "wind_speed_10m": current_weather.get("wind_speed_10m"),
        }
    except requests.exceptions.RequestException as e:
        print(f"Error during weather API request: {e}", file=sys.stderr)
        return None
    except (KeyError, TypeError, ValueError) as e: # Added ValueError
        print(f"Error parsing weather API response: {e}", file=sys.stderr)
        return None

def get_weather_emoji(weather_code: int) -> str:
    """
    Returns an emoji corresponding to the WMO weather interpretation code.
    """
    if weather_code is None:
        return "❓"
    # WMO Weather interpretation codes
    if weather_code == 0:
        return "☀️"  # Clear sky
    elif weather_code == 1:
        return "🌤️"  # Mainly clear
    elif weather_code == 2:
        return "🌥️"  # Partly cloudy
    elif weather_code == 3:
        return "☁️"  # Overcast
    elif weather_code in [45, 48]:
        return "🌫️"  # Fog and depositing rime fog
    elif weather_code in [51, 53, 55]:
        return "💧"  # Drizzle: Light, moderate, and dense intensity
    elif weather_code in [56, 57]:
        return "🥶"  # Freezing Drizzle: Light and dense intensity
    elif weather_code in [61, 63, 65]:
        return "🌧️"  # Rain: Slight, moderate and heavy intensity
    elif weather_code in [66, 67]:
        return "🥶🌧️" # Freezing Rain: Light and heavy intensity
    elif weather_code in [71, 73, 75]:
        return "❄️"  # Snow fall: Slight, moderate, and heavy intensity
    elif weather_code == 77:
        return "❄️"  # Snow grains
    elif weather_code in [80, 81, 82]:
        return "🌦️"  # Rain showers: Slight, moderate, and violent
    elif weather_code in [85, 86]:
        return "❄️🌨️" # Snow showers slight and heavy
    elif weather_code == 95: # Corresponds to WMO codes 95
        return "⛈️"  # Thunderstorm: Slight or moderate
    elif weather_code in [96, 99]: # Corresponds to WMO codes 96, 99
        return "⛈️"  # Thunderstorm with slight and heavy hail
    else:
        return "❓"  # Default for unknown codes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the current weather for a city.")
    parser.add_argument("city_name", help="The name of the city")

    args = parser.parse_args()

    latitude, longitude, country = get_coordinates(args.city_name)

    if latitude is None or longitude is None:
        print(f"Error: City '{args.city_name}' not found or geocoding failed.", file=sys.stderr)
        sys.exit(1)

    weather_data = get_weather(latitude, longitude)

    if weather_data is None:
        print("Error: Could not retrieve weather data for the location.", file=sys.stderr)
        sys.exit(1)

    weather_emoji = get_weather_emoji(weather_data.get("weather_code"))
    
    country_display = f", {country}" if country else ""

    print(f"Weather in {args.city_name}{country_display}:")
    if weather_data.get("temperature_2m") is not None:
        print(f"{weather_emoji} {weather_data['temperature_2m']}°C")
    else:
        print(f"{weather_emoji} Temperature data not available")

    if weather_data.get("relative_humidity_2m") is not None:
        print(f"Humidity: {weather_data['relative_humidity_2m']}%")
    else:
        print("Humidity data not available")

    if weather_data.get("wind_speed_10m") is not None:
        print(f"Wind: {weather_data['wind_speed_10m']} km/h")
    else:
        print("Wind speed data not available")
