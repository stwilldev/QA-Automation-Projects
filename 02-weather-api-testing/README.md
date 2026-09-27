# Weather API Automation Testing Suite

An automated API testing suite built with Python and PyTest. Designed to validate live HTTP responses, JSON data payloads, and weather data metrics from external REST endpoints.

## Features
* **HTTP Status Validation:** Automatically verifies successful REST API responses (`200 OK`).
* **JSON Payload Parsing:** Extracts and validates nested data fields (location data, area names).
* **Data Assertion:** Checks live meteorological data such as temperature and humidity against expected conditions.
* **PyTest Integration:** Structured for automated test execution and reporting.

## Tech Stack
* **Language:** Python 3
* **Testing Framework:** PyTest
* **HTTP Library:** Requests

## Getting Started

### Prerequisites
Make sure you have Python and the required dependencies installed:
```bash
pip install pytest requests