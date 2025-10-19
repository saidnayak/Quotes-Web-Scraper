import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the page")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    with open("quotes.txt", "w", encoding="utf-8") as file:
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            print(f"{text} — {author}")
            file.write(f"{text} — {author}\n")

if __name__ == "__main__":
    scrape_quotes()
