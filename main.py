from Place_Classes import Habitat
from bs4 import BeautifulSoup
import requests

zillow_aa_url = 'https://tinyurl.com/zillow-annarbor-rentals'

response = requests.get(zillow_aa_url)

soup = BeautifulSoup(response.content, 'html.parser')

possible_places = []

for row in soup.select('tbody.lister-list tr'):
    # title = row.find('td', class_='titleColumn').find('a').get_text()
    # year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').get_text()[1:-1]
    # rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()

    # place = Habitat(rooms, rent, kind, location, kind)
    # movies.append([title, year, rating])

    for black in range(50):
        print(row)
