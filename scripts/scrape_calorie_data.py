import requests
from bs4 import BeautifulSoup
import csv

def scrape_calorie_data(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find food categories and calories (this depends on the website structure)
    food_items = []
    table = soup.find('table')  # Assuming data is in a table
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) >= 2:
            food_name = columns[0].get_text(strip=True)
            calories = columns[1].get_text(strip=True)
            food_items.append((food_name, calories))

    # Write scraped data to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Food Name', 'Calories'])
        writer.writerows(food_items)

    print(f"Calorie data scraped and saved to {output_file}")

if __name__ == "__main__":
    url = "https://www.nutritionix.com/foods"  
    output_file = "calorie_data.csv"
    scrape_calorie_data(url, output_file)
