"""Ejercicio 7: Genera un grafo con los enfrentamientos entre los 5 equipos con más puntos."""
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from . import config


def graf(data: pd.DataFrame, selected_teams: list[str]) -> None:
    """Genera un gráfico de enfrentamientos entre los equipos seleccionados."""
    cond_home = data['HomeTeam'].isin(selected_teams)
    cond_away = data['AwayTeam'].isin(selected_teams)
    filtered_data = data[cond_home & cond_away]
    matches = filtered_data.groupby(['HomeTeam', 'AwayTeam']).size()

    graph = nx.Graph()
    for (home, away), n in matches.items():
        if graph.has_edge(home, away):
            graph[home][away]['weight'] += n
        else:
            graph.add_edge(home, away, weight=n)

    pos = nx.circular_layout(graph)
    fig, ax = plt.subplots(figsize=(10, 8))
    nx.draw(graph, pos, ax=ax, with_labels=True, node_color='lightblue',
            edge_color='gray', node_size=2000)

    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, ax=ax)
    fig.savefig(f"img/grafica_ex7_{config.nom_alumne}_{config.date_time}.png")
