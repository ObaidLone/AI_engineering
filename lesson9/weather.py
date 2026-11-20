
import requests
import json
import os

url = "https://geocoding-api.open-meteo.com/v1/search"
weather_url = "https://api.open-meteo.com/v1/forecast"


# Step 1: Get city coordinates
def get_coordinates(city):

    response = requests.get(
        url,
        params={"name": city, "count": 1},
        timeout=10
    )

    response.raise_for_status()
    data = response.json()

    if not data.get("results"):
        return None

    city_data = data["results"][0]

    latitude = city_data["latitude"]
    longitude = city_data["longitude"]

    return latitude, longitude


# Step 2: Get current weather
def get_weather(lat, lon):

    response = requests.get(
        weather_url,
        params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": "true"
        },
        timeout=10
    )

    response.raise_for_status()
    data = response.json()

    current = data["current_weather"]

    temperature = current["temperature"]
    wind_speed = current["windspeed"]

    return temperature, wind_speed

def save_weather(city,temperature,wind_speed):
    weather_data={
        "city": city,
        "temperature": temperature,
        "wind_speed": wind_speed
    }
    with open("last_weather.json",'w',encoding="utf-8") as file:
        json.dump(weather_data,file,indent=4)
    print("weather save successfully")

def load_weather():

    if os.path.exists("last_weather.json"):

        with open("last_weather.json", "r", encoding="utf-8") as file:
            weather_data = json.load(file)

        print("\nLast saved weather")
        print("----------------------")
        print("City:", weather_data["city"])
        print("Temperature:", weather_data["temperature"], "°C")
        print("Wind speed:", weather_data["wind_speed"], "km/h")

    else:
        print("No previous weather data found.")
# Step 3: Main function
def main():
    load_weather()
    

    city = input("Enter a city name: ")

    try:
        coordinates = get_coordinates(city)

        if coordinates is None:
            print("Sorry, city not found!")
            return

        lat, lon = coordinates

        temperature, wind_speed = get_weather(lat, lon)

        print("\nWeather in", city)
        print("----------------------")
        print("Temperature:", temperature, "°C")
        print("Wind speed:", wind_speed, "km/h")
        
        save_weather(city, temperature, wind_speed)

    except requests.exceptions.Timeout:
        print("The request took too long. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")

    except requests.exceptions.HTTPError as error:
        print("The server returned an error:", error)

    except requests.exceptions.RequestException as error:
        print("Something went wrong:", error)

    

if __name__ == "__main__":
    main()
