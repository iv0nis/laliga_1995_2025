"""Configuración de setup para el proyecto de análisis de partidos de LaLiga entre las temporadas
1995-96 y 2024-25 mediante setuptools."""
from setuptools import setup, find_packages

setup(
    name='laliga_1995_2025',
    version='1.0.0',
    author='Ivonis Florindo Lopez',
    description='Analiza los partidos de LaLiga entre las temporadas 1995-96 y 2024-25',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas~=2.3.1',
        'matplotlib~=3.10.8',
        'networkx~=3.5'
    ],
    python_requires='>=3.10',
)
