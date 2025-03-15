import requests     # Importing the requests library to make HTTP requests
import weather_api as wapi      # Importing weather_api module (a pyhton file containing the API key) to retrieve the API key. To use this program without any error, please substitute your own API key.

# Function to get the current weather data for the given city using the OpenWeatherMap API
def get_weather(city):
    # This function retrieves the current weather data for the given city using the OpenWeatherMap API.
    
    # Parameters:
    # city (str): The name of the city for which the weather information is needed.
    
    # It constructs the API URL, sends a request to the OpenWeatherMap API, parses the returned data, and then prints the weather details such as temperature, pressure, humidity, description, and wind speed for the city. If the city is not found, it will print an error message.


    api_key = wapi.openweather_apikey       # Retrieving the API key from the weather_api module
    # Constructing the URL for OpenWeatherMap API with the provided city name and API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # Sending a GET request to the OpenWeatherMap API and storing the response
        response = requests.get(url)
        # Parsing the response JSON into a Python dictionary
        data = response.json()

        # Checking if the city was not found in the API response
        if data["cod"] == "404":
            print("Error: City not found. Please enter the valid city name.")

        else:
            # Extracting main weather data (temperature, pressure, humidity) from the response
            main_data = data["main"]
            # Extracting weather condition description from the response
            weather_data = data["weather"][0]
            # Extracting wind data (speed) from the response
            wind_data = data["wind"]

            # Extracting temperature data value from main weather data
            temperature_data = main_data["temp"]
            # Extracting pressure data value from main weather data
            pressure_data = main_data["pressure"]
            # Extracting humidity data value from main weather data
            humidity_data = main_data["humidity"]

            # Extracting weather description
            weather_description = weather_data["description"]

            # Extracting wind speed value from wind data
            windspeed_data = wind_data["speed"]

            # Printing the weather information
            print(f"Weather in {city.capitalize()}:\n")
            print(f"Temperature: {temperature_data}°C")
            print(f"Pressure: {pressure_data} hPa")
            print(f"Humidity: {humidity_data}%")
            print(f"Weather Description: {weather_description.capitalize()}")
            print(f"Wind Speed: {windspeed_data} m/s")

    except Exception as e:
        # Handling any exceptions that occur during the process
        print(f"An error occured: {str(e)}")

# Main entry point function
def main():
    # This function is the main entry point of the program.
    # It prompts the user to input the name of a city, and then calls the `get_weather()` function to retrieve and display the current weather information for that city.

    # Prompting the user to enter a city name
    city = input("Enter the City name: ")

    # Calling the function to get current weather for the entered city
    get_weather(city)


# Ensuring that the program runs only if it's executed directly (not imported)
if __name__ == "__main__":
    # Calling the main function to start the program
    main()
