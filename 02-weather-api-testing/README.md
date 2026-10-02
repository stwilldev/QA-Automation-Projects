# 🌤️ Weather API Automation & Testing Framework

An automated API testing suite built with Python, PyTest, and Requests, implementing the **Service Client Pattern** and integrated with **GitHub Actions** for CI/CD[span_1](start_span)[span_1](end_span).

---

## 🚀 Features

* **HTTP Status Validation:** Automatically verifies successful REST API responses (`200 OK`)[span_2](start_span)[span_2](end_span).
* **JSON Payload Parsing:** Extracts and validates nested data fields (location data, area names, temperature, and humidity)[span_3](start_span)[span_3](end_span).
* **Data Assertion:** Checks live meteorological data against expected conditions[span_4](start_span)[span_4](end_span).
* **PyTest Integration:** Structured for automated test execution and reporting[span_5](start_span)[span_5](end_span).
* **Continuous Integration (CI/CD):** Automated cloud test execution via GitHub Actions on every push[span_6](start_span)[span_6](end_span).

---

## 🏗️ Architecture & Design Pattern

This project implements the **Service Client Pattern** to cleanly separate API request plumbing from test assertions:
* **`modules/weather_client.py`**: Encapsulates base URLs, headers, user-agents, and HTTP methods into a reusable Python class[span_7](start_span)[span_7](end_span).
* **`test_weatherapp3.py`**: Modular PyTest test files that consume the client and execute data validations[span_8](start_span)[span_8](end_span).

---

## 🛠️ Tech Stack

* **Language:** Python 3[span_9](start_span)[span_9](end_span)
* **Testing Framework:** PyTest[span_10](start_span)[span_10](end_span)
* **HTTP Library:** Requests[span_11](start_span)[span_11](end_span)
* **CI/CD:** GitHub Actions[span_12](start_span)[span_12](end_span)

---

## ⚙️ Getting Started & Installation

Make sure you have Python installed, then clone the repository and install dependencies:

```bash
pip install requests pytest
