"""Guarda el nombre del alumno y la hora a la que se ejecuta el programa.

Sirve para ponerle nombre a las gráficas que se generan en img/, así
cada imagen lleva el nombre y el momento en que se creó.
"""
from datetime import datetime

# en minúsculas porque el enunciado lo usa así (config.nom_alumne)
nom_alumne: str = "Ivonis Florindo"  # pylint: disable=invalid-name
date_time: str = datetime.now().strftime('%Y%m%d_%H%M%S')
