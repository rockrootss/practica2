# Simulación de partidas y ranking en shooter online

# Simule varias partidas de un juego de disparos y genere un ranking basado en el puntaje
# total de cada jugador. Se utilizará el siguiente sistema de puntuación:

#    Acción    Puntos
#    Kill         3
#    Asistencia   1
#    Muerte      -1

# Dado el siguiente conjunto de rondas:

#    rounds = [
# {
# 'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
# 'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
# 'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
# 'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
# 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
# },
# {
# 'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
# 'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
# 'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
# 'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
# 'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
# },
# {
# 'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
# 'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
# 'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
# 'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
# 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
# },
# {
# 'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
# 'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
# 'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
# 'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
# 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
# },
# {
# 'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
# 'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
# 'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
# 'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
# 'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
# }
# ]

# Imprima las tablas de resultados luego de la inserción de cada una de las rondas pudiendo
# ver el progreso en el equipo.

# Además cada ronda debe tener un MVP (Mejor Jugador del Partido/ronda) basado en su
# puntuación. La cantidad de veces que el jugador ha sido MVP también se debe contabilizar
# Se debe imprimir el total de kills, asistencias, muertes, cantidad de MVP y puntos totales. La
# tabla tienen que estar en orden decreciente por los puntos totales.
# Salida esperada:

#Ranking ronda 1:
#...
#Ranking ronda 2:
#...
#Ranking final:
#Jugador Kills Asistencias Muertes MVPs Puntos
#Shadow    6        6        2      2     22
#Blaze     6        3        3      1     18
#Viper     5        6        3      1     18
#Reaper    4        5        1      0     16
#Frost     4        5        2      1     15
#-------------------------------------------------------

# Nota: No hace falta que la tabla se vea exactamente igual. Lo importante es que tengas los
# valores correctos y se entienda.

from ejercicio10utilidades import *

rounds = [
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}
]

# Diccionario para almacenar las estadísticas totales
stats = {} # kills, assists, deaths y puntos totales de cada jugador
mvp_count = {} # Cuenta cuantas veces un jugador fue MVP

round_count = 1                   #cuento las rondas

#Itero entre las rondas
for round in rounds:
    
    round_scores = {}    # Diccionario para almacenar los puntos de cada jugador en la ronda

    #Itero entre los jugadores de esa ronda
    for player, data in round.items(): 
        kills = data['kills']    
        assists = data['assists']
        deaths =  data['deaths']
        points = (kills * 3) + (assists * 1) - (1 if deaths else 0)  #sumo los puntos de cada jugador

        #Si el jugador no existe en stats, lo agrego con todo en 0
        if player not in stats:                                                    
            stats[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'points': 0}
            mvp_count[player] = 0
        
        #Actualizo estadisticas de jugador
        stats[player]['kills'] += kills
        stats[player]['assists'] += assists
        stats[player]['deaths'] += 1 if deaths else 0
        stats[player]['points'] += points

        # Guardar la puntuación de la ronda para determinar MVP
        round_scores[player] = points

    # Determinar el MVP de la ronda
    mvp_player = determinar_mvp(round_scores, mvp_count)

    # Ordenar por puntos totales. Mostrar ranking de la ronda y MVP
    mostrar_ranking(round_count,stats,mvp_player)
    
    round_count += 1  # Incrementar número de ronda

# Generar el ranking final
generar_ranking_final(stats, mvp_count)

