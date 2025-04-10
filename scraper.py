import requests
from bs4 import BeautifulSoup

# URL delle pagine
URL_LUCE = "https://tariffe.segugio.it/costo-energia-elettrica/ricerca-offerte-energia-elettrica.aspx"
URL_GAS = "https://tariffe.segugio.it/costo-gas-metano/ricerca-offerte-gas-metano.aspx"

# Parametri di filtro (questi vanno eventualmente passati al form o con querystring se supportato dal sito)
CONSUMO_LUCE = 2000  # in kWh
CONSUMO_GAS = 1000   # in smc

def fetch_page(url):
    """Recupera il contenuto HTML della pagina data."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Errore nel recupero della pagina {url}: {e}")
        return None

def parse_ranking(html: str, offer_keyword: str = "A2A Click") -> int:
    """
    Parsea l'HTML per trovare il ranking dell'offerta che contiene offer_keyword.
    Si assume che la pagina contenga una lista ordinata di offerte.
    
    Ritorna la posizione (1-based) oppure -1 se non trovato.
    """
    soup = BeautifulSoup(html, "html.parser")
    
    # Supponiamo che ogni offerta sia in un div con classe 'offer' o simile.
    # Potrebbe essere necessario adattare il selettore in base alla struttura effettiva.
    offerte = soup.select("div.offer, li.offer, div.box-offerta")
    
    # Selezioniamo gli elementi che contengono il testo di interesse
    rank = 1
    for offerta in offerte:
        # Puliamo il testo eliminando spazi e passiamo in minuscolo
        testo_offerta = offerta.get_text(strip=True).lower()
        if offer_keyword.lower() in testo_offerta:
            return rank
        rank += 1
    
    return -1  # non trovato

def get_offer_ranking():
    """
    Recupera il ranking dell'offerta A2A Click per gas e luce.
    Attualmente viene fatto uno scraping diretto delle pagine.
    Se sono necessari parametri di filtro, occorrerà simulare una richiesta POST o passare querystring.
    """
    # Recupero della pagina della luce
    html_luce = fetch_page(URL_LUCE)
    luce_rank = -1
    if html_luce:
        luce_rank = parse_ranking(html_luce, offer_keyword="A2A Click")
    
    # Recupero della pagina del gas
    html_gas = fetch_page(URL_GAS)
    gas_rank = -1
    if html_gas:
        gas_rank = parse_ranking(html_gas, offer_keyword="A2A Click")
    
    return luce_rank, gas_rank

# Se questo modulo viene eseguito direttamente (utile per testare in locale)
if __name__ == "__main__":
    luce, gas = get_offer_ranking()
    print(f"Ranking Luce: {luce}")
    print(f"Ranking Gas: {gas}")
