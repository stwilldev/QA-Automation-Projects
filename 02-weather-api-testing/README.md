# Weather API Automation & Testing Framework

An automated API testing suite built with Python, PyTest, and Requests, implementing the Service Client Pattern and integrated with GitHub Actions for CI/CD.

## Features

* **HTTP Status Validation:** Automatically verifies successful REST API responses (200 OK).
* **JSON Payload Parsing:** Extracts and validates nested data fields (location data, area names, temperature, and humidity).
* **Data Assertion:** Checks live meteorological data against expected conditions.
* **PyTest Integration:** Structured for automated test execution and reporting.
* **Continuous Integration (CI/CD):** Automated cloud test execution via GitHub Actions on every push.

## Architecture & Design Pattern

This project implements the Service Client Pattern to cleanly separate API request plumbing from test assertions:
* **modules/weather_client.py:** Encapsulates base URLs, headers, user-agents, and HTTP methods into a reusable Python class.
* **test_weatherapp3.py:** Modular PyTest test files that consume the client and execute data validations.

## Tech Stack

* **Language:** Python 3
* **Testing Framework:** PyTest
* **HTTP Library:** Requests
* **CI/CD:** GitHub Actions

## Getting Started & Installation

Make sure you have Python installed, then clone the repository and install dependencies:

```bash
pip install requests pytest
