import requests
from bs4 import BeautifulSoup
import csv

def scrape_weather(city_url, city_name, csv_writer):
    try:
        # Send GET request to the URL
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(city_url, headers=headers)
        
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract temperature
            temperature_elem = soup.find('div', class_='temp')
            if temperature_elem:
                temperature = temperature_elem.text.strip()
            else:
                temperature = 'Not available'
            
            # Print the extracted temperature
            print(f"Temperature in {city_name}: {temperature}")
            
            # Write temperature to CSV
            csv_writer.writerow([city_name, temperature])
            
            print(f"Weather data for {city_name} saved.")
            
        else:
            print(f"Failed to retrieve data for {city_name}. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    
    except Exception as e:
        print(f"Error: {e}")

# URL and city names for weather
urls = {
    'Multan': 'https://www.accuweather.com/en/pk/multan/260376/weather-forecast/260376',
    'Faisalabad': 'https://www.accuweather.com/en/pk/faisalabad/259286/weather-forecast/259286'
}

# Open CSV file for writing
csv_file = 'weather_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['City', 'Temperature'])
    
    # Scrape weather data for each city
    for city, url in urls.items():
        scrape_weather(url, city, writer)

print(f"Weather data saved to {csv_file}")