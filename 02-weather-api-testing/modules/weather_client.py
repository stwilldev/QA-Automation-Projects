import requests

class WeatherClient:
    def __init__(self):
        self.base_url = "https://wttr.in"

    def get_city_weather(self, city_name: str) -> requests.Response:
        endpoint = f"{self.base_url}/{city_name}?format=j1"
        headers = {
        "Accept": "application/json",
        "User-Agent": "SDET-Automation-Framework"
    }
        return requests.get(endpoint, headers=headers)