"""Ejercicio 6: Calcula goles totales, el resumen de 1995-2025 por equipo y la gráfica de podium."""
import pandas as pd
import matplotlib.pyplot as plt
from . import config


def fun_total_goals(data: pd.DataFrame) -> tuple[int, int, int]:
    """Devuelve una tupla con goles marcados en casa, fuera y el total."""
    home_goals = int(data['FTHG'].sum())
    away_goals = int(data['FTAG'].sum())
    total_goals = home_goals + away_goals

    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Devuelve una tupla de tres dataframes con los goles por equipo en casa, fuera y el total."""
    home_goals_by_team = data.groupby('HomeTeam')['FTHG'].sum()
    away_goals_by_team = data.groupby('AwayTeam')['FTAG'].sum()
    total_goals_by_team = home_goals_by_team + away_goals_by_team
    total_goals_by_team = total_goals_by_team.rename_axis('Team').to_frame('total_goals')
    home_goals_by_team = home_goals_by_team.to_frame('home_goals').rename_axis('Team')
    away_goals_by_team = away_goals_by_team.to_frame('away_goals').rename_axis('Team')

    return home_goals_by_team, away_goals_by_team, total_goals_by_team


def fun_summary_1996_2025(total_points_by_team: pd.DataFrame,
                          home_goals_by_team: pd.DataFrame,
                          away_goals_by_team: pd.DataFrame,
                          total_goals_by_team: pd.DataFrame) -> pd.DataFrame:
    """Devuelve un dataframe con la concatenación de los 4 dataframes anteriores:
    total_points_by_team, home_goals_by_team, away_goals_by_team y total_goals_by_team."""
    summary_1996_2025 = pd.concat([total_points_by_team, home_goals_by_team, away_goals_by_team,
                                   total_goals_by_team], axis=1)

    return summary_1996_2025


def podium(summary_1996_2025: pd.DataFrame) -> None:
    """Genera una gráfica de podium con los 3 equipos con más puntos históricos."""
    top_3 = (summary_1996_2025.sort_values('total_points', ascending=False)
             .head(3).iloc[[1, 0, 2]])
    fig, ax = plt.subplots(figsize=(8, 6))
    barras = ax.bar(top_3.index, top_3['total_points'], color=['silver', 'gold', 'peru'])
    ax.bar_label(barras, labels=top_3.index)
    ax.axis('off')
    fig.savefig(f"img/grafica_ex6_{config.nom_alumne}_{config.date_time}.png")
