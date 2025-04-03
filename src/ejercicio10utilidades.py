# Determina el MVP de la ronda y actualiza el contador de MVPs.
def determinar_mvp(round_scores, mvp_count):
    """Determina el MVP de la ronda y actualiza el contador de MVPs."""
    mvp_player = max(round_scores, key=round_scores.get)
    mvp_count[mvp_player] += 1

    return mvp_player


def obtener_puntos(jugador):
    
    return jugador[1]['points']

# Ordena por puntos totales y muestra el ranking de la ronda junto con el MVP
def mostrar_ranking(round_count, stats, mvp_player):
    """Ordena por puntos totales y muestra el ranking de la ronda junto con el MVP."""
    ranking = sorted(stats.items(), key=obtener_puntos, reverse=True)

    print(f"Ranking Ronda {round_count}:")
    for player, data in ranking:
        print(f"{player}: {data['kills']} Kills, {data['assists']} Assists, {data['deaths']} Muertes, {data['points']} Puntos")
    
    print("--------------------------------")
    print(f"MVP: {mvp_player}")
    print("--------------------------------")


# Función para generar el ranking final
def generar_ranking_final(stats, mvp_count):
    """Función para generar el ranking final"""
    final_ranking = sorted(stats.items(), key=obtener_puntos, reverse=True)
    print("Ranking Final:")
    for player, data in final_ranking:
        print(f"Jugador: {player} , Kills:{data['kills']} , Assists:{data['assists']} , Deaths:{data['deaths']} , MVP: {mvp_count[player]} , Puntos:{data['points']}")