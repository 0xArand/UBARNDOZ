# Python Weather CLI Tool

A command-line interface tool that fetches and displays the current weather for a specified city. It utilizes the Open-Meteo API for geocoding city names to coordinates and for retrieving weather forecasts. Weather conditions are displayed with corresponding emojis for a quick visual understanding.

## Features

*   Fetches current temperature (in Celsius).
*   Displays current relative humidity.
*   Shows current wind speed (in km/h).
*   Represents weather conditions with emojis (e.g., ☀️, 🌧️, ☁️).
*   Automatically looks up city coordinates.
*   User-friendly command-line input.

## Requirements

*   Python 3.x
*   `requests` library

## Installation

1.  Ensure you have Python 3 installed on your system.
2.  Clone this repository or download the `main.py` and `require.txt` files.
3.  Navigate to the directory containing the files in your terminal.
4.  Install the necessary dependencies:
    ```bash
    pip install -r require.txt
    ```

## Usage

To get the weather for a city, run the script with the city name as an argument:

```bash
python main.py <city_name>
```

If the city name contains spaces, enclose it in quotes:

```bash
python main.py "New York"
```

### Example

```bash
python main.py "London"
```

## Example Output

```
Weather in London, United Kingdom:
🌥️ 12°C
Humidity: 85%
Wind: 15 km/h
```
*(Note: The actual output will vary based on the current weather conditions.)*

## Data Source

Weather data provided by [Open-Meteo](https://open-meteo.com/).

## License

This project is open-source. Feel free to use, modify, and distribute.
