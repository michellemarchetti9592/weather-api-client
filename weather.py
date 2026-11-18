import json
import urllib.request

def get_forecast(lat: float = 52.52, lon: float = 13.41) -> dict:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    with urllib.request.urlopen(url, timeout=10) as resp:
        return json.loads(resp.read().decode())

if __name__ == "__main__":
    print("Weather client ready")
