import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = '817d87bb1899925cd19bedf645ba0550'
city = 'Lagos'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()

# Print the entire response for debugging
print("API Response:", data)

# Check if the response contains the 'list' key
if 'list' in data:
    # Extract relevant data
    dates = [datetime.utcfromtimestamp(item['dt']) for item in data['list']]
    temperatures = [item['main']['temp'] for item in data['list']]

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o')
    plt.title(f'5-Day Weather Forecast for {city}')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('weather_forecast.png')
    plt.show()
else:
    print("Error: The API response does not contain the expected 'list' key.")
