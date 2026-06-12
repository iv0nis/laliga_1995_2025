"""Ejercicio 3: Calcula la distribución de goles marcados en casa y fuera
y genera un gráfico de barras."""
import pandas as pd
import matplotlib.pyplot as plt
from . import config


def goals_distribution(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Calcula la distribución de goles en casa y fuera."""
    distr_goals_home = data['FTHG'].value_counts().sort_index().to_frame('matches')
    distr_goals_away = data['FTAG'].value_counts().sort_index().to_frame('matches')

    return distr_goals_home, distr_goals_away


# ditribution con typo porque el enunciado lo escribe así
def plot_goals_ditribution(distr_goals_home: pd.DataFrame,
                           distr_goals_away: pd.DataFrame) -> None:
    """Genera un gráfico de barras con la distribución de goles en casa y fuera."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

    axes[0].bar(distr_goals_home.index, distr_goals_home['matches'], color='tab:blue')
    axes[0].set_title('Distribución de goles en casa')
    axes[0].set_xlabel('Número de goles')
    axes[0].set_ylabel('Número de partidos')

    axes[1].bar(distr_goals_away.index, distr_goals_away['matches'], color='tab:orange')
    axes[1].set_title('Distribución de goles fuera de casa')
    axes[1].set_xlabel('Número de goles')

    fig.tight_layout()
    fig.savefig(f"img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png")
