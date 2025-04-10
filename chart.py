import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_trend(df, output_path):
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["luce_rank"], label="Luce", marker="o")
    plt.plot(df["date"], df["gas_rank"], label="Gas", marker="o")
    plt.xlabel("Data")
    plt.ylabel("Posizione Ranking")
    plt.title("Trend posizione A2A Click - Gas e Luce")
    plt.gca().invert_yaxis()  # Rank 1 is better
    plt.legend()
    plt.grid(True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
