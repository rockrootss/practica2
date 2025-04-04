

import sys
import os

#Obtener la ruta absoluta del directorio raiz del proyecto 
sys.path.append(os.path.abspath("../practica2/src"))

from funciones import *

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

