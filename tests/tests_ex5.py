"""Tests de las funciones add_points, fun_total_points y alltime_winner del ejercicio 5."""
import sys
import os
import unittest
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from exercises.ex5 import (add_points, # pylint: disable=wrong-import-position
                           fun_total_points, alltime_winner)


class TestFunTotalPoints(unittest.TestCase):
    """Comprueba add_points, fun_total_points y alltime_winner con un dataframe de ejemplo."""

    def test_add_points(self):
        """Los puntos de cada partido tienen que cuadrar con su FTR."""
        data = pd.DataFrame({
            'HomeTeam': ['Barcelona', 'Real Madrid', 'Villarreal'],
            'AwayTeam': ['Real Madrid', 'Villarreal', 'Barcelona'],
            'FTR': ['H', 'D', 'A']
        })
        data = add_points(data)
        self.assertEqual(data['points_home'].tolist(), [3, 1, 0])
        self.assertEqual(data['points_away'].tolist(), [0, 1, 3])

    def test_fun_total_points(self):
        """El acumulado por equipo tiene que cuadrar con los puntos de los 3 partidos."""
        data = pd.DataFrame({
            'HomeTeam': ['Barcelona', 'Real Madrid', 'Villarreal'],
            'AwayTeam': ['Real Madrid', 'Villarreal', 'Barcelona'],
            'FTR': ['H', 'D', 'A']
        })
        serie_points, total_points = fun_total_points(add_points(data))
        self.assertEqual(serie_points.loc['Barcelona'], 6)
        self.assertEqual(total_points.loc['Real Madrid', 'total_points'], 1)

    def test_alltime_winner(self):
        """El equipo con más puntos tiene que salir como ganador."""
        total_points = pd.DataFrame(
            {'total_points': [6, 1, 1]},
            index=['Barcelona', 'Real Madrid', 'Villarreal'])
        self.assertEqual(alltime_winner(total_points), 'Barcelona')


if __name__ == '__main__':
    unittest.main()
