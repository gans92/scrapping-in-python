import requests
import csv
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.content, 'html.parser')

# Create a CSV file and write the header row
with open('books.csv', 'w', newline='',encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Price', 'Rating', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Find all book titles
    titles = soup.find_all('h3')
    for title in titles:
        title_text = title.text
        link = title.find('a')['href']
        # Find the price and rating of the book
        price = title.find_next(class_='price_color').text
        rating = title.find_next(class_='star-rating')['class'][1]
        # Write the data to the CSV file
        writer.writerow({'Title': title_text, 'Price': price, 'Rating': rating, 'Link': link})
