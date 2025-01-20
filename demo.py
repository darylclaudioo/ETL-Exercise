import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

base_url = "https://api.openweathermap.org/data/2.5/weather"

# Extract
def extract(city):
    url = f"{base_url}?q={city}&appid={api_key}"
    response = requests.get(url)
    
    return response.json()

# Transform    
def transform(data):
    transformed = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }

    return transformed

# Load
def load(data, filename):
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)

# Run
def run(city):
    data = extract(city)
    transformed = transform(data)
    load(transformed, "weather.csv")

city="Bandung"
run(city)