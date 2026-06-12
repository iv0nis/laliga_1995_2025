"""Fichero principal que ejecuta los diferentes módulos de ejercicios."""
import argparse
from exercises import ex1, ex2, ex3, ex4, ex5, ex6, ex7


# main concentra los prints de todos los ejercicios (lo pide el enunciado),
# así que supera el límite de variables locales de pylint
def main() -> None:  # pylint: disable=too-many-locals
    """Lee el argumento -ex y ejecuta los ejercicios."""
    parser = argparse.ArgumentParser(description="Ejecuta los ejercicios de La Liga 1995-2025")
    parser.add_argument("-ex", type=int, default=7, choices=range(1, 8),
                        help="ejecuta los ejercicios del 1 al EX de forma secuencial")
    args = parser.parse_args()

    print("\n--- Ejercicio 1 ---")
    data = ex1.load_and_eda("data/LaLiga_Matches.csv")
    ex1.plot_home_away_goals(data)

    if args.ex >= 2:
        print("\n--- Ejercicio 2 ---")
        matches_team_total = ex2.total_matches(data)
        print(matches_team_total.head(10))
        maximo = matches_team_total['total_matches'].max()
        print("Equipos que siempre han estado en primera división:")
        print(matches_team_total[matches_team_total['total_matches'] == maximo])
        ex2.plot_matches_team_total(matches_team_total)

    if args.ex >= 3:
        print("\n--- Ejercicio 3 ---")
        distr_goals_home, distr_goals_away = ex3.goals_distribution(data)
        print(distr_goals_home)
        print(distr_goals_away)
        ex3.plot_goals_ditribution(distr_goals_home, distr_goals_away)

    if args.ex >= 4:
        print("\n--- Ejercicio 4 ---")
        ftr = ex4.FTR(data)
        print(ftr)
        porcentaje_locales = ftr.loc['H', 'matches'] / ftr['matches'].sum() * 100
        print(f"Los locales ganan el {porcentaje_locales:.2f}% de los partidos")
        ex4.plot_FTR(ftr)

    if args.ex >= 5:
        print("\n--- Ejercicio 5 ---")
        data = ex5.add_points(data)
        print(data.head(10))
        serie_points, total_points = ex5.fun_total_points(data)
        print(total_points.head(10))
        print("Ganador histórico:", ex5.alltime_winner(total_points))

    if args.ex >= 6:
        print("\n--- Ejercicio 6 ---")
        home_goals, away_goals, total_goals = ex6.fun_total_goals(data)
        print(f"Goles en casa: {home_goals}, fuera: {away_goals}, total: {total_goals}")
        h_team, a_team, t_team = ex6.fun_total_goals_by_team(data)
        print(t_team.head(10))
        summary_1996_2025 = ex6.fun_summary_1996_2025(total_points, h_team, a_team, t_team)
        print(summary_1996_2025.head(10))
        ex6.podium(summary_1996_2025)

    if args.ex >= 7:
        print("\n--- Ejercicio 7 ---")
        # la ejecución es incremental: llegar al 7 implica que el 5 ya corrió
        # pylint: disable-next=possibly-used-before-assignment
        selected_teams = serie_points.nlargest(5).index.tolist()
        print("Equipos seleccionados:", selected_teams)
        ex7.graf(data, selected_teams)


if __name__ == "__main__":
    main()
