from Place_Classes import Habitat
# from bs4 import BeautifulSoup
# import requests

# zillow_aa_url = 'https://www.realtor.com/apartments/Ann-Arbor_MI'

# response = requests.get(zillow_aa_url)

# soup = BeautifulSoup(response.content, 'html.parser')

# possible_places = []

# for row in soup.select('tbody.lister-list tr'):
#     # title = row.find('td', class_='titleColumn').find('a').get_text()
#     # year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').get_text()[1:-1]
#     # rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()

#     # place = Habitat(rooms, rent, kind, location, kind)
#     # movies.append([title, year, rating])

#     for black in range(50):
#         print(row)

import requests
from bs4 import BeautifulSoup
import pandas as pd





# Function to get the HTML content of a page
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to parse the HTML and extract data
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    listings = []

    for item in soup.select('.list-card-info'):
        address = item.select_one('.list-card-addr').text if item.select_one('.list-card-addr') else None
        price = item.select_one('.list-card-price').text if item.select_one('.list-card-price') else None
        beds = item.select_one('.list-card-details li:nth-child(1)').text if item.select_one('.list-card-details li:nth-child(1)') else None
        baths = item.select_one('.list-card-details li:nth-child(2)').text if item.select_one('.list-card-details li:nth-child(2)') else None
        sqft = item.select_one('.list-card-details li:nth-child(3)').text if item.select_one('.list-card-details li:nth-child(3)') else None

        listings.append({
            'Address': address,
            'Price': price,
            'Beds': beds,
            'Baths': baths,
            'SqFt': sqft
        })
    
    return listings

# Main function to scrape Zillow
def scrape_zillow(url):
    html = get_html(url)
    if html:
        data = parse_html(html)
        return data
    else:
        print("Failed to retrieve the webpage.")
        return None

# URL of the Zillow page to scrape
zillow_url = 'https://www.realtor.com/apartments/Ann-Arbor_MI'

# Scrape the data
data = scrape_zillow(zillow_url)

# Save the data to a CSV file
if data:
    df = pd.DataFrame(data)
    df.to_csv('zillow_listings.csv', index=False)
    print("Data saved to zillow_listings.csv")
else:
    print("No data to save.")
