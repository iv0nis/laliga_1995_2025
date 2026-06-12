"""Ejercicio 2: Devuelve el número total de partidos de cada equipo en un dataframe."""
import pandas as pd
import matplotlib.pyplot as plt
from . import config


def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """Calcula el número total de partidos por equipo."""
    matches_team_total = (data['HomeTeam'].value_counts() + data['AwayTeam'].value_counts()
                         ).to_frame('total_matches')

    return matches_team_total


def plot_matches_team_total(matches_team_total: pd.DataFrame) -> None:
    """Genera un gráfico de barras con el número total de partidos por equipo."""

    df_sorted = matches_team_total.sort_values('total_matches', ascending=False)

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.bar(df_sorted.index, df_sorted['total_matches'], color='tab:blue')
    ax.tick_params(axis='x', rotation=90)
    ax.set_title('Número total de partidos por equipo')
    fig.tight_layout()
    fig.savefig(f"img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png")
