import os
import pandas as pd
from datetime import datetime
from scraper import get_offer_ranking
from chart import load_data, save_data, plot_trend

# Percorsi dei file
DATA_DIR = "data"
CSV_PATH = os.path.join(DATA_DIR, "offers_history.csv")
CHART_PATH = os.path.join("charts", "trend_ranking.png")

def update_history(luce_rank: int, gas_rank: int):
    """Aggiorna il file CSV con i nuovi dati."""
    # Carica i dati esistenti, o creane uno nuovo se il file non esiste
    df = load_data(CSV_PATH)
    
    # Nuova riga da aggiungere
    new_entry = {
        "data": datetime.now().strftime("%Y-%m-%d"),
        "luce_rank": luce_rank,
        "gas_rank": gas_rank
    }
    df = df.append(new_entry, ignore_index=True)
    
    # Ordina per data
    df["data"] = pd.to_datetime(df["data"])
    df = df.sort_values("data")
    
    # Salva i dati aggiornati
    os.makedirs(DATA_DIR, exist_ok=True)
    save_data(df, CSV_PATH)
    print("Dati aggiornati nel CSV.")

def main():
    print("Inizio raccolta dati...")
    luce_rank, gas_rank = get_offer_ranking()
    print(f"Ranking Luce: {luce_rank}, Ranking Gas: {gas_rank}")
    
    update_history(luce_rank, gas_rank)
    plot_trend(CSV_PATH, CHART_PATH)

if __name__ == "__main__":
    main()
