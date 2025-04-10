import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def load_data(csv_path: str):
    """Carica lo storico dei dati da CSV."""
    try:
        df = pd.read_csv(csv_path, parse_dates=["data"])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["data", "luce_rank", "gas_rank"])
    return df

def save_data(df: pd.DataFrame, csv_path: str):
    """Salva lo storico dei dati nel CSV."""
    df.to_csv(csv_path, index=False)

def plot_trend(csv_path: str, output_path: str):
    """Genera un grafico del ranking e lo salva come immagine."""
    df = load_data(csv_path)
    if df.empty:
        print("Nessun dato da visualizzare.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(df["data"], df["luce_rank"], marker="o", label="Luce - A2A Click")
    plt.plot(df["data"], df["gas_rank"], marker="o", label="Gas - A2A Click")
    plt.title("Trend ranking offerte A2A Click")
    plt.xlabel("Data")
    plt.ylabel("Ranking")
    plt.legend()
    plt.gca().invert_yaxis()  # Se il ranking 1 è il migliore, si inverte l’asse Y
    plt.grid(True)
    plt.tight_layout()

    # Crea la cartella di output se non esiste
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    print(f"Grafico salvato in {output_path}")

if __name__ == "__main__":
    # Test rapido (modifica i percorsi se necessario)
    csv_file = "data/offers_history.csv"
    output_file = "charts/trend_ranking.png"
    plot_trend(csv_file, output_file)
