"""Ejercicio 1: Carga los datos de La Liga en un df, hace una exploración preliminar
y genera una gráfica de goles casa/fuera."""
import pandas as pd
import matplotlib.pyplot as plt
from . import config


def load_and_eda(file: str) -> pd.DataFrame:
    """Carga el CSV, quita las columnas descanso (HTHG, HTAG, HTR)
    y muestra info básica del dataframe."""
    df = pd.read_csv(file)

    # Elimina las columnas del descanso porque
    # solo nos interesa el resultado final
    df = df.drop(columns=['HTHG', 'HTAG', 'HTR'])

    # Unifica el nombre del equipo Villarreal, que aparece escrito de dos formas distintas
    df = df.replace('Villareal', 'Villarreal')

    print(df.head())
    print(df.tail())
    df.info()

    return df


def plot_home_away_goals(data: pd.DataFrame) -> None:
    """Pinta dos boxplots para ver cómo se reparten los
    goles en casa y fuera."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

    axes[0].boxplot(data['FTHG'], tick_labels=['FTHG'], patch_artist=True,
                    boxprops={'facecolor': 'tab:blue'}, medianprops={'color': 'black'})
    axes[0].set_title('Goles en casa')

    axes[1].boxplot(data['FTAG'], tick_labels=['FTAG'], patch_artist=True,
                    boxprops={'facecolor': 'tab:orange'}, medianprops={'color': 'black'})
    axes[1].set_title('Goles fuera de casa')

    fig.savefig(f"img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png")
