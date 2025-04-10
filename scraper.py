import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36"
}

def get_offer_rank(url, brand_name):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Cerca tutte le offerte
        offers = soup.find_all('div', class_='offerta-energy-box')

        for i, offer in enumerate(offers):
            if brand_name.lower() in offer.text.lower():
                return i + 1  # Il ranking parte da 1
        return -1  # Offerta non trovata
    except Exception as e:
        print(f"Errore nel recupero della pagina {url}: {e}")
        return -1

