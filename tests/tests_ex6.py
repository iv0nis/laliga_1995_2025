"""Tests de las funciones fun_total_goals, fun_total_goals_by_team
y fun_summary_1996_2025 del ejercicio 6."""
import sys
import os
import unittest
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from exercises.ex6 import (fun_total_goals, # pylint: disable=wrong-import-position
                           fun_total_goals_by_team,
                           fun_summary_1996_2025)


class TestFunTotalGoals(unittest.TestCase):
    """Comprueba las funciones de goles y resumen del ejercicio 6 con dataframes de ejemplo."""

    def test_fun_total_goals(self):
        """Los goles en casa, fuera y el total tienen que cuadrar con el dataframe."""
        data = pd.DataFrame({'FTHG': [2, 0, 1], 'FTAG': [1, 1, 3]})
        self.assertEqual(fun_total_goals(data), (3, 5, 8))

    def test_fun_total_goals_by_team(self):
        """Los goles por equipo en casa, fuera y total tienen que cuadrar con el dataframe."""
        data = pd.DataFrame({
            'HomeTeam': ['Barcelona', 'Real Madrid', 'Villarreal'],
            'AwayTeam': ['Real Madrid', 'Villarreal', 'Barcelona'],
            'FTHG': [2, 0, 1],
            'FTAG': [1, 1, 3]
        })
        home_goals, away_goals, total_goals = fun_total_goals_by_team(data)
        self.assertEqual(home_goals.loc['Barcelona', 'home_goals'], 2)
        self.assertEqual(away_goals.loc['Barcelona', 'away_goals'], 3)
        self.assertEqual(total_goals.loc['Barcelona', 'total_goals'], 5)

    def test_fun_summary_1996_2025(self):
        """Las columnas del resumen tienen que cuadrar con los dataframes de entrada."""
        equipos = ['Barcelona', 'Real Madrid']
        total_points = pd.DataFrame({'total_points': [6, 3]}, index=equipos)
        home_goals = pd.DataFrame({'home_goals': [2, 0]}, index=equipos)
        away_goals = pd.DataFrame({'away_goals': [3, 1]}, index=equipos)
        total_goals = pd.DataFrame({'total_goals': [5, 1]}, index=equipos)
        summary = fun_summary_1996_2025(total_points, home_goals, away_goals, total_goals)
        self.assertEqual(summary.loc['Barcelona', 'total_points'], 6)
        self.assertEqual(summary.loc['Barcelona', 'away_goals'], 3)
        self.assertEqual(summary.loc['Real Madrid', 'total_goals'], 1)


if __name__ == '__main__':
    unittest.main()
