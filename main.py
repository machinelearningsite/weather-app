import requests

class CityWeather:
    def __init__(self, city) -> None:
        self.city = city
        self.api_key = API_KEY  # Replace with your OpenWeatherMap API key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(self.city, self.api_key)
        params = {
        "q": self.city,
        "appid": self.api_key,
        "units": "metric"  # You can change the units to "imperial" for Fahrenheit
    }
    
        response = requests.get(self.base_url, params=params)
        self.weather_data = response.json()
    

    def get_weather(self):
        if self.weather_data["cod"] == "404":
            print("City not found!")
        else:
            main_weather = self.weather_data["weather"][0]["main"]
            description = self.weather_data["weather"][0]["description"]
            temperature = self.weather_data["main"]["temp"]
            humidity = self.weather_data["main"]["humidity"]
            
            print(f"Weather in {self.city}:")
            print(f"Main weather: {main_weather}")
            print(f"Description: {description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")

def main():
    city = input("Enter a city name: ")
    berlin = CityWeather(city)
main()
