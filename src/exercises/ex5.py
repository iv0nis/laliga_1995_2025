"""Ejercicio 5: Añade los puntos de cada partido al dataset, acumula el total por equipo y saca
el ganador histórico de la liga (1995-2025)."""
import pandas as pd


def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """Añade una columna con los puntos obtenidos como local y otra con los puntos obtenidos
    como visitante por cada partido."""
    data = data.copy()
    data['points_home'] = data['FTR'].map({'H': 3, 'D': 1, 'A': 0})
    data['points_away'] = data['FTR'].map({'H': 0, 'D': 1, 'A': 3})

    return data


def fun_total_points(data: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    """Calcula el total de puntos obtenidos y acumulados por cada equipo desde 1995."""
    serie_points = (data.groupby('HomeTeam')['points_home'].sum()
                    + data.groupby('AwayTeam')['points_away'].sum()).rename_axis('Team')

    total_points = serie_points.to_frame('total_points')

    return serie_points, total_points


def alltime_winner(total_points: pd.DataFrame) -> str:
    """Devuelve el equipo con más puntos acumulados en la historia de la liga."""
    maximo = total_points['total_points'].max()
    winner = total_points[total_points['total_points'] == maximo].index[0]

    return winner
