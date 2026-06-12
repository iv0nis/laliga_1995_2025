"""Ejercicio 4: Calcula el número de partidos ganados por los equipos locales, por los
visitantes o empatados, en un dataframe, y lo representa en un gráfico de barras."""
import pandas as pd
import matplotlib.pyplot as plt
from . import config


def FTR(data: pd.DataFrame) -> pd.DataFrame:  # pylint: disable=invalid-name
    """Calcula el número de partidos ganados por los equipos locales,
    los visitantes o que han empatado."""
    ftr = data['FTR'].value_counts().to_frame('matches')

    return ftr


def plot_FTR(ftr: pd.DataFrame) -> None:  # pylint: disable=invalid-name
    """Genera un gráfico de barras con los partidos ganados por equipos locales, visitantes
    o empatados."""
    ftr_sorted = ftr.reindex(['H', 'A', 'D'])

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(ftr_sorted.index, ftr_sorted['matches'], color=['tab:blue', 'tab:orange', 'tab:gray'])
    ax.set_title('Partidos ganados en casa, fuera y empatados')
    ax.set_xlabel('Resultado final (FTR)')
    ax.set_ylabel('Número de partidos')
    fig.savefig(f"img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png")
