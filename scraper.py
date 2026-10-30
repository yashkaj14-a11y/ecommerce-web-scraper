import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes():
    """
    Scrapes quote text and author names from a public website
    and exports the result to a clean CSV file.
    """
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch webpage!")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    
    data = []
    for q in quotes:
        text = q.find('span', class_='text').text
        author = q.find('small', class_='author').text
        data.append({"Quote": text, "Author": author})
        
    df = pd.DataFrame(data)
    df.to_csv("scraped_data.csv", index=False)
    print("Scraping completed! Data saved to scraped_data.csv")

if __name__ == "__main__":
    scrape_quotes()
