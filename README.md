# Análisis de LaLiga 1995-2025

Ivonis Florindo. PEC4 de Programación para la ciencia de datos (UOC).

## Descripción

Proyecto en Python que analiza los partidos de LaLiga entre las temporadas 1995-96 y 2024-25: goles por equipo, porcentaje de victorias locales, clasificación histórica por puntos y un grafo de enfrentamientos entre equipos. Cada ejercicio tiene su módulo en `src/exercises/` y el proyecto se ejecuta desde `src/main.py`. Las gráficas generadas se guardan en `src/img/`.

## Estructura de carpetas

```
laliga_1995_2025/
├── doc/                   documentación generada con pydoc
├── screenshots/           capturas de autoría
├── src/
│   ├── data/              dataset LaLiga_Matches.csv
│   ├── exercises/         un módulo por ejercicio (ex1.py ... ex7.py) + config.py
│   ├── img/               gráficas generadas
│   └── main.py            punto de entrada, ejecuta los ejercicios
├── tests/
│   ├── tests_ex5.py       tests de puntos y ganador histórico (ejercicio 5)
│   └── tests_ex6.py       tests de goles totales, por equipo y resumen (ejercicio 6)
├── .pylintrc              configuración de pylint
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py               empaquetado con setuptools
```

## Instalación

Desde la raíz del proyecto, crear un entorno virtual limpio, activarlo e instalar las dependencias:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Para salir del entorno virtual, `deactivate`.

El proyecto también incluye `setup.py`, así que como alternativa se puede instalar como paquete con `pip install -e .` desde la raíz.

## Ejecución

El proyecto se ejecuta desde la carpeta `src/`, ojo con esto: las rutas al dataset y a las imágenes son relativas a ella.

```bash
cd src
python3 main.py
```

Sin argumentos se ejecutan los 7 ejercicios. El argumento `-ex` ejecuta los ejercicios del 1 al número indicado:

```bash
python3 main.py -ex 3     # ejecuta los ejercicios 1, 2 y 3
python3 main.py -h        # ayuda
```

Los resultados se muestran por pantalla y las gráficas se guardan en `src/img/` con el nombre del alumno y la fecha y hora de generación.

## Linting

El código se revisa con [pylint](https://pylint.readthedocs.io/), usando la configuración del archivo `.pylintrc`. Desde la raíz del proyecto:

```bash
python3 -m pylint src tests
```

Pylint no forma parte de las dependencias del proyecto; si no se tiene, se instala con `pip install pylint`.

## Documentación

Todas las funciones llevan docstring. La documentación en HTML de la carpeta `doc/` se ha generado con [pydoc](https://docs.python.org/3/library/pydoc.html), desde `src/`:

```bash
cd src
python3 -m pydoc -w main exercises exercises.config exercises.ex1 exercises.ex2 exercises.ex3 exercises.ex4 exercises.ex5 exercises.ex6 exercises.ex7
mv *.html ../doc/
```

## Tests

El test que pide el enunciado comprueba `fun_total_goals` (ejercicio 6); además hay tests de los goles por equipo, del resumen y del cálculo de puntos del ejercicio 5. Se ejecutan desde la raíz del proyecto:

```bash
python3 -m tests.tests_ex6
python3 -m tests.tests_ex5
```

También se pueden lanzar todos de una vez con `python3 -m unittest discover tests -p "tests_*.py"`.

El informe de cobertura se saca con coverage (hay que instalarlo con `pip install coverage`; no va en requirements.txt porque es herramienta de desarrollo, igual que pylint):

```bash
coverage run -m unittest discover tests -p "tests_*.py"
coverage report
```

De los módulos que tocan los tests, lo único que queda sin cubrir es la gráfica del podium.

## Subir el proyecto a GitHub

El proyecto está subido en [github.com/iv0nis/laliga_1995_2025](https://github.com/iv0nis/laliga_1995_2025). Para subirlo se creó un repositorio vacío en GitHub y se ejecutó, desde la raíz del proyecto:

```bash
git init
git add .
git commit -m "PEC4: análisis de LaLiga 1995-2025"
git branch -M main
git remote add origin https://github.com/iv0nis/laliga_1995_2025.git
git push -u origin main
```

## Notas sobre los datos

El dataset trae el equipo Villarreal con dos grafías distintas (`Villareal` y `Villarreal`), lo que duplicaba el equipo en los resultados. Se detectó en la gráfica del ejercicio 2 y la función de carga (`load_and_eda`, en `ex1.py`) lo unifica a `Villarreal`.

## Licencia

El proyecto se distribuye bajo licencia MIT (ver archivo `LICENSE`).

## Referencias

- [U6] Material UOC, unidad 6: *Testing, mantenimiento y despliegue de aplicaciones Python* (estructura de proyecto, módulos y paquetes, requirements.txt, entornos virtuales, unittest, git).
- Vídeos de la PEC4 (UOC): linting con pylint y ejecución de tests.
- Documentación oficial de Python: [unittest](https://docs.python.org/3/library/unittest.html), [pydoc](https://docs.python.org/3/library/pydoc.html) y [argparse](https://docs.python.org/3/library/argparse.html).
- Documentación oficial de [pylint](https://pylint.readthedocs.io/).
- Documentación oficial de las librerías del proyecto: [pandas](https://pandas.pydata.org/docs/), [matplotlib](https://matplotlib.org/stable/) y [networkx](https://networkx.org/documentation/stable/).
- Métodos consultados en la documentación oficial: [`rename_axis`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename_axis.html), [`to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html) y [`nlargest`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html) de pandas, y [`bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html) de matplotlib.
