import pandas as pd
import datetime
from scraper import get_offer_rank
from chart import plot_trend

# URL dei comparatori con i filtri richiesti
URL_LUCE = "https://tariffe.segugio.it/costo-energia-elettrica/ricerca-offerte-energia-elettrica.aspx"
URL_GAS = "https://tariffe.segugio.it/costo-gas-metano/ricerca-offerte-gas-metano.aspx"
BRAND_NAME = "A2A"

DATA_PATH = "data/offers_history.csv"

def update_history(luce_rank, gas_rank):
    today = datetime.date.today().isoformat()
    new_entry = {
        "date": today,
        "luce_rank": luce_rank,
        "gas_rank": gas_rank
    }

    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["date", "luce_rank", "gas_rank"])

    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)

    return df

def main():
    print("Inizio raccolta dati...")

    luce_rank = get_offer_rank(URL_LUCE, BRAND_NAME)
    gas_rank = get_offer_rank(URL_GAS, BRAND_NAME)

    print(f"Ranking Luce: {luce_rank}, Ranking Gas: {gas_rank}")

    df = update_history(luce_rank, gas_rank)

    plot_trend(df)

if __name__ == "__main__":
    main()
