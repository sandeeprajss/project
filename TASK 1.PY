import requests
import matplotlib.pyplot as plt
import datetime
import seaborn as sns

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key"
CITY = "London"

# Fetch weather data from OpenWeatherMap API
url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)

# Validate API response
if response.status_code == 200:
    data = response.json()
    
    if "list" in data and isinstance(data["list"], list):
        # Extract relevant data
        timestamps = []
        temperatures = []
        
        for entry in data["list"]:
            if "dt" in entry and "main" in entry and "temp" in entry["main"]:
                timestamps.append(datetime.datetime.fromtimestamp(entry["dt"]))
                temperatures.append(entry["main"]["temp"])
        
        if timestamps and temperatures:
            # Set Seaborn style
            sns.set_theme(style="darkgrid")
            
            # Plot temperature trend
            plt.figure(figsize=(12, 6))
            plt.plot(timestamps, temperatures, marker="o", linestyle="-", color="b", label="Temperature (°C)")
            plt.xlabel("Date and Time")
            plt.ylabel("Temperature (°C)")
            plt.title(f"Temperature Forecast for {CITY}")
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            plt.show()
        else:
            print("Error: No valid temperature data available.")
    else:
        print("Error: Unexpected response structure. Check the API response format.")
else:
    print(f"Error: Failed to fetch data. HTTP Status Code: {response.status_code}")
