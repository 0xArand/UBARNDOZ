#!/usr/bin/env python3

import unittest
import sys
from unittest.mock import patch, MagicMock

# Add the directory containing main.py to the Python path
# This is often not needed if your project is structured as a package
# or if you run tests using a test runner that handles paths.
# For a simple script, this might be necessary if test_main.py is in the same directory.
sys.path.append('.')

from main import get_coordinates, get_weather, get_weather_emoji

class TestWeatherEmoji(unittest.TestCase):
    def test_known_weather_codes(self):
        self.assertEqual(get_weather_emoji(0), "☀️")  # Clear sky
        self.assertEqual(get_weather_emoji(1), "🌤️")  # Mainly clear
        self.assertEqual(get_weather_emoji(2), "🌥️")  # Partly cloudy
        self.assertEqual(get_weather_emoji(3), "☁️")  # Overcast
        self.assertEqual(get_weather_emoji(45), "🌫️") # Fog
        self.assertEqual(get_weather_emoji(51), "💧") # Drizzle
        self.assertEqual(get_weather_emoji(56), "🥶") # Freezing Drizzle
        self.assertEqual(get_weather_emoji(61), "🌧️") # Rain
        self.assertEqual(get_weather_emoji(66), "🥶🌧️")# Freezing Rain
        self.assertEqual(get_weather_emoji(71), "❄️") # Snow fall
        self.assertEqual(get_weather_emoji(73), "❄️") # Snow fall (moderate)
        self.assertEqual(get_weather_emoji(75), "❄️") # Snow fall (heavy)
        self.assertEqual(get_weather_emoji(77), "❄️") # Snow grains
        self.assertEqual(get_weather_emoji(80), "🌦️") # Rain showers
        self.assertEqual(get_weather_emoji(85), "❄️🌨️")# Snow showers
        self.assertEqual(get_weather_emoji(95), "⛈️") # Thunderstorm
        self.assertEqual(get_weather_emoji(96), "⛈️") # Thunderstorm with hail
        self.assertEqual(get_weather_emoji(99), "⛈️") # Thunderstorm with heavy hail


    def test_unknown_weather_code(self):
        self.assertEqual(get_weather_emoji(999), "❓")

    def test_none_weather_code(self):
        self.assertEqual(get_weather_emoji(None), "❓")

class TestGetCoordinates(unittest.TestCase):
    @patch('main.requests.get')
    def test_successful_api_call(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'results': [{
                'latitude': 52.52,
                'longitude': 13.41,
                'country': 'Germany',
                'name': 'Berlin'
            }]
        }
        mock_get.return_value = mock_response

        lat, lon, country = get_coordinates('Berlin')
        self.assertEqual(lat, 52.52)
        self.assertEqual(lon, 13.41)
        self.assertEqual(country, 'Germany')
        mock_get.assert_called_once()

    @patch('main.requests.get')
    def test_city_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'results': []}
        mock_get.return_value = mock_response

        lat, lon, country = get_coordinates('UnknownCity')
        self.assertIsNone(lat)
        self.assertIsNone(lon)
        self.assertIsNone(country)

    @patch('main.requests.get')
    def test_api_no_results_key(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'some_other_key': 'value'}
        mock_get.return_value = mock_response

        lat, lon, country = get_coordinates('City')
        self.assertIsNone(lat)
        self.assertIsNone(lon)
        self.assertIsNone(country)

    @patch('main.requests.get')
    def test_api_request_exception(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Test API error")

        lat, lon, country = get_coordinates('AnyCity')
        self.assertIsNone(lat)
        self.assertIsNone(lon)
        self.assertIsNone(country)

    @patch('main.requests.get')
    def test_api_json_decode_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("JSON decode error") # Corresponds to requests.exceptions.JSONDecodeError
        mock_get.return_value = mock_response

        lat, lon, country = get_coordinates('CityWithBadJSON')
        self.assertIsNone(lat)
        self.assertIsNone(lon)
        self.assertIsNone(country)

class TestGetWeather(unittest.TestCase):
    @patch('main.requests.get')
    def test_successful_api_call(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'current': {
                'temperature_2m': 15.0,
                'relative_humidity_2m': 70,
                'weather_code': 0,
                'wind_speed_10m': 10.0
            }
        }
        mock_get.return_value = mock_response

        weather_data = get_weather(52.52, 13.41)
        expected_data = {
            'temperature_2m': 15.0,
            'relative_humidity_2m': 70,
            'weather_code': 0,
            'wind_speed_10m': 10.0
        }
        self.assertEqual(weather_data, expected_data)
        mock_get.assert_called_once()

    @patch('main.requests.get')
    def test_api_response_missing_current_data(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'other_data': 'value'}
        mock_get.return_value = mock_response

        weather_data = get_weather(52.52, 13.41)
        self.assertIsNone(weather_data)

    @patch('main.requests.get')
    def test_api_request_exception(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Test API error")

        weather_data = get_weather(52.52, 13.41)
        self.assertIsNone(weather_data)

    @patch('main.requests.get')
    def test_api_json_decode_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("JSON decode error") # Corresponds to requests.exceptions.JSONDecodeError
        mock_get.return_value = mock_response

        weather_data = get_weather(52.52, 13.41)
        self.assertIsNone(weather_data)

if __name__ == '__main__':
    # Need to import requests here for the side_effect in tests
    # This is a bit of a workaround for how the main script might be structured
    # and how tests are run in this environment.
    import requests
    unittest.main()
