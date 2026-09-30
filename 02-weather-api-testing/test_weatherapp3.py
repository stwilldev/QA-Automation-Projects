import pytest
from modules.weather_client import WeatherClient

@pytest.fixture
def weather_client():
    return WeatherClient()

def test_weather_api_atlanta(weather_client):
    #1. Call the service client method
    response = weather_client.get_city_weather("Atlanta")

    #2. Assert HTTP[ status code is 200 OK
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    #3. Parse JSON payload and verify city location
    data = response.json()
    area_name = data["nearest_area"][0]["areaName"][0]["value"]
    assert "Atlanta" in area_name, f"Expected Atlanta in area name, got {area_name}"

    #4. Extract and verify live temperature
    temp_f = data["current_condition"][0]["temp_F"]
    assert temp_f is not None, "Temperature reading is missing!"

    print(f"\nsuccess] Atlanta Weather: {temp_f}°F")
    
def test_weather_api_tokyo(weather_client):
    # 1. Call the service client method for Tokyo
    response = weather_client.get_city_weather("Tokyo")

    # 2. Assert HTTP status code is 200 OK
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # 3. Parse JSON payload and verify city location
    data = response.json()
    area_name = data["nearest_area"][0]["areaName"][0]["value"]
    assert "Tokyo" in area_name or "Shikinejima" in area_name, f"Expected Tokyo into the area name, got {area_name}"

    # 4. Extract and verify live temperature
    temp_f = data["current_condition"][0]["temp_F"]
    assert temp_f is not None, "Temperature reading is missing!"

    print(f"\n[Success] Tokyo Weather: {temp_f}°F")                      
