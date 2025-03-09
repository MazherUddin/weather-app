# Weather App MCP Tool

A tool for fetching weather alerts and forecasts using the National Weather Service API.

## Features

- Get weather alerts for any US state using a two-letter state code
- Get detailed weather forecasts for any location using latitude and longitude coordinates

## Usage

### Get Alerts

```python
# Get alerts for California
get_alerts("CA")
```

### Get Forecast

```python
# Get forecast for San Francisco
get_forecast(37.7749, -122.4194)
```

## Requirements

- httpx
- mcp-server

## How It Works

This tool uses the National Weather Service API to fetch real-time weather data and presents it in a readable format.