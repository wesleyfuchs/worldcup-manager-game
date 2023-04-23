import json
from game import matchday
from game_fase_final import matchday_fase_final
from richladder import createrichladder
from team import Team
from jogador import Jogador

GROUP_STAGE = 91
PLAYOFFS = 121


def zerar_pontuacao(database):
    '''Zera a pontuação de cada time'''
    for team in database:
        database[team]['score'] = 0


def mostrar_pontuacao_times(database):
    '''print da pontuação dos times'''
    print('----')
    for team in database:
        print(str(database[team]["name"]) +
              " - " + str(database[team]["score"]))
    print('----')

#Arrumar o quickgame(nomes invertidos)
def partidas(userteam, season, database):
    partida_rapida = True
    partida_longa = False
    
    with open('data/teams_jogadores.txt', 'w') as json_file:
        json.dump(database, json_file, indent=4)

    teamcolor = "dark_olive_green3 bold italic"
    leaguecolor = "chartreuse3"
    gameweeknum = 0
    for week in season:
        gameweeknum += 1
        # used to determine next opponent by skipping ahead by 1 in the index
        upcomingArray = []
        x = 0
        for i in season:
            upcomingArray.append(i)
            x += 1

        # Pergunta se o usuario ira jogar ou skippar o proximo jogo!
        print("1. Jogar")
        print("2. Skip")
        gamechoice = input("Gostaria de Jogar ou Pular o jogo? ")
        print(" ")
        # print('Gameweek: ' + str(gameweeknum))
        print(" ")

        # newweek is created to ensure that the user team is always at the front of the gameweek for readability
        newweek = []
        for matchbrackets in week:
            newweek.append(matchbrackets)
            for m in newweek:
                if userteam in m:
                    newweek.remove(m)
                    newweek.insert(0, m)

        # for each match in a week, set up the game using temporary versions of the team class
        for matchbrackets in newweek:
            match0 = []
            match1 = []
            for team in matchbrackets:
                match0.append(team)
            team1 = Team(0, str(match0[0]), 0, 0, 0, 0, 0, 0, 0, 0, database[match0[0]]['jogadores'])
            team2 = Team(0, str(match0[1]), 0, 0, 0, 0, 0, 0, 0, 0, database[match0[1]]['jogadores'])
            
            # Adiciona os jogadores do database às equipes
            for i, team_name in enumerate([team1.name, team2.name]):
                for jogador in database[team_name]['jogadores']:
                    jogador = Jogador(jogador['nome'], jogador['posicao'], jogador['finalizacao'], jogador['defesa'], jogador['passe'], jogador['ball_control'], jogador['gols'])
                    if i == 0:
                        team1.adicionar_jogador(jogador)
                    else:
                        team2.adicionar_jogador(jogador)
            
            match1.append(team1)
            match1.append(team2)

            # Se o time do usuario estiver no matchbracket
            if userteam in match0:
                # Se o usuario escolher o modo Play:
                if gamechoice == "1":
                    print(match0[0] + " vs " + match0[1])
                    print(' ')
                    matchday(match1, database, partida_rapida, GROUP_STAGE, '')
                    print(' ')
                    print('Gameweek: ' + str(gameweeknum))
                    print(' ')
                    input(' ')
                # Se o usuario escolher Skip (Modo Rapido):
                else:
                    matchday(match1, database, partida_longa, GROUP_STAGE, '')
                    print(' ')
                    print('Gameweek: ' + str(gameweeknum))
                    print(' ')
                    input(' ')
            else:
                matchday(match1, database, partida_longa, GROUP_STAGE, '')

            with open('data/teams_jogadores.txt', 'w') as json_file:
                json.dump(database, json_file, indent=4)
                
        input(' ')
        print(' ')
        for grupos in grupos_dict:
            createrichladder(grupos, leaguecolor, teamcolor, userteam, gameweeknum)
        print(' ')


def partidas_fase_final(userteam, season, database):
    partida_rapida = True
    partida_longa = False
    
    with open('data/teams_jogadores.txt', 'w') as json_file:
        json.dump(database, json_file, indent=4)
    
    gameweeknum = 0
    for week in season:
        gameweeknum += 1
        # used to determine next opponent by skipping ahead by 1 in the index
        upcomingArray = []
        x = 0
        for i in season:
            upcomingArray.append(i)
            x += 1
        
        print("1. Jogar")
        print("2. Skip")
        gamechoice = input("Gostaria de Jogar ou Pular o jogo? ")
        # newweek is created to ensure that the user team is always at the front of the gameweek for readability
        newweek = []
        for matchbrackets in week:
            newweek.append(matchbrackets)
            for m in newweek:
                if userteam in m:
                    newweek.remove(m)
                    newweek.insert(0, m)

        # for each match in a week, set up the game using temporary versions of the team class
        for matchbrackets in newweek:
            match0 = []
            match1 = []
            for team in matchbrackets:
                match0.append(team)
            team1 = Team(0, str(match0[0]), 0, 0, 0, 0, 0, 0, 0, 0, database[match0[0]]['jogadores'])
            team2 = Team(0, str(match0[1]), 0, 0, 0, 0, 0, 0, 0, 0, database[match0[1]]['jogadores'])
            
            # Adiciona os jogadores do database às equipes
            for i, team_name in enumerate([team1.name, team2.name]):
                for jogador in database[team_name]['jogadores']:
                    jogador = Jogador(jogador['nome'], jogador['posicao'], jogador['finalizacao'], jogador['defesa'], jogador['passe'], jogador['ball_control'], jogador['gols'])
                    if i == 0:
                        team1.adicionar_jogador(jogador)
                    else:
                        team2.adicionar_jogador(jogador)
                        
            match1.append(team1)
            match1.append(team2)

            # Se o time do usuario estiver no matchbracket
            if userteam in match0:
                
                # if user wants to play a game use long game mode matchday
                if gamechoice == "1":
                    print(match0[0] + " vs " + match0[1])
                    print(' ')
                    matchday(match1, database, partida_rapida, PLAYOFFS, 'playoffs')
                    print(' ')
                else:
                    matchday(match1, database, partida_longa, PLAYOFFS, 'playoffs')
            else:
                matchday(match1, database, partida_longa, PLAYOFFS, 'playoffs')

            with open('data/teams_jogadores.txt', 'w') as json_file:
                json.dump(database, json_file, indent=4)


def ordenar_fase_final(confrontos):
    '''Ordena os times por pontuação e depois por saldo de gols'''
    selecoes_ordenado = []
    for grupos in confrontos:
        dicc = {}
        for team in grupos:
            dicc[grupos[team]['name']] = (
                grupos[team]["score"], grupos[team]["goaldif"])

        sorteddicc = sorted(dicc, key=lambda x: (-dicc[x][0], -dicc[x][1]))
        selecoes_ordenado.append(sorteddicc)
    return selecoes_ordenado


def listar_equipes(lista_de_partidas):
    equipes_database = []
    for confronto in lista_de_partidas:
        quartas = {k: database[k] for k in confronto}
        equipes_database.append(quartas)
    return equipes_database


def realizar_etapa_final(equipes, num_equipes_proxima_etapa, database):
    '''Cria os matchbrackets e realiza as partidas'''
    
    # Ordenar as equipes pelo número de pontos
    equipes_ordenadas = ordenar_fase_final(equipes)


    # Criar a lista de partidas da próxima etapa
    partidas = [(equipes_ordenadas[i][0], equipes_ordenadas[i + 1][0])for i in range(0, num_equipes_proxima_etapa, 2)]

    # Zerar a pontuação das equipes
    zerar_pontuacao(database)

    # Realizar as partidas da próxima etapa
    partidas_fase_final(userteam, [partidas], database)

    partidas = [[equipes_ordenadas[i][0], equipes_ordenadas[i + 1][0]]
                for i in range(0, num_equipes_proxima_etapa, 2)]

    return partidas


with open('data/teams_jogadores.txt') as f:
    database = json.load(f)

# Lista dos grupos
grupos = [('Catar', 'Equador', 'Senegal', 'Holanda'), 
          ('Inglaterra', 'Ira', 'Estados Unidos', 'Pais de Gales'), 
          ('Argentina', 'Arabia Saudita', 'Mexico', 'Polonia'), 
          ('Franca', 'Australia', 'Dinamarca', 'Tunisia'), 
          ('Espanha', 'Costa Rica', 'Alemanha', 'Japao'), 
          ('Belgica', 'Canada', 'Marrocos', 'Croacia'), 
          ('Brasil', 'Servia', 'Suica', 'Camaroes'), 
          ('Portugal', 'Gana', 'Uruguai', 'Coreia do Sul')]

# Cria os grupos a partir do database
grupos_dict = [{k: database[k] for k in grupo} for grupo in grupos]

# Lista os matchbrackets da fase de grupos
season = [[('Catar', 'Equador'), ('Senegal', 'Holanda'), ('Inglaterra', 'Ira'), ('Estados Unidos', 'Pais de Gales'), ('Argentina', 'Arabia Saudita'), ('Mexico', 'Polonia'), ('Franca', 'Australia'), ('Dinamarca', 'Tunisia'), ('Espanha', 'Costa Rica'), ('Alemanha', 'Japao'), ('Belgica', 'Canada'), ('Marrocos', 'Croacia'), ('Brasil', 'Servia'), ('Suica', 'Camaroes'), ('Portugal', 'Gana'), ('Uruguai', 'Coreia do Sul')],
          [('Catar', 'Senegal'), ('Holanda', 'Equador'), ('Inglaterra', 'Estados Unidos'), ('Pais de Gales', 'Ira'), ('Argentina', 'Mexico'), ('Polonia', 'Arabia Saudita'), ('Franca', 'Dinamarca'), ('Tunisia', 'Australia'), ('Espanha', 'Alemanha'), ('Japao', 'Costa Rica'), ('Belgica', 'Marrocos'), ('Croacia', 'Canada'), ('Brasil', 'Suica'), ('Camaroes', 'Servia'), ('Portugal', 'Uruguai'), ('Coreia do Sul', 'Gana')], 
          [('Catar', 'Holanda'), ('Equador', 'Senegal'), ('Inglaterra', 'Pais de Gales'), ('Ira', 'Estados Unidos'), ('Argentina', 'Polonia'), ('Arabia Saudita', 'Mexico'), ('Franca', 'Tunisia'), ('Australia', 'Dinamarca'), ('Espanha', 'Japao'), ('Costa Rica', 'Alemanha'), ('Belgica', 'Croacia'), ('Canada', 'Marrocos'), ('Brasil', 'Camaroes'), ('Servia', 'Suica'), ('Portugal', 'Coreia do Sul'), ('Gana', 'Uruguai')]]


# Zera todos dados dos times
for team in database:
    database[team]['goaldif'] = 0
    database[team]['goals'] = 0
    database[team]['goals_sofridos'] = 0
    database[team]['won'] = 0
    database[team]['drawn'] = 0
    database[team]['lost'] = 0

for team in database:
    for jogador in database[team]['jogadores']:
        jogador['gols'] = 0

# Salva as alterações de volta no arquivo json
with open('data/teams_jogadores.txt', 'w') as f:
    json.dump(database, f)

# Zera pontuacao e gols dos times
zerar_pontuacao(database)


# Menu com numero de cada time
menu_n = 1
for grupo in grupos:
    for team in grupo:
        print('{} - {}'.format(menu_n, team))
        menu_n += 1

numinputchoices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                   "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]
numinputcorrect = False
while numinputcorrect == False:
    numinput = input('Escolha um time: ')
    # Checar se o input é valido
    if numinput in numinputchoices:
        numinputcorrect = True
        userteamkey = int(numinput)
    else:
        print("Por favor escolha um numero entre 1 - 32!!")
if userteamkey > 0 and userteamkey < 33:
    for team in database:
        if userteamkey == database[team]['key']:
            userteam = database[team]['name']
            print('Voce escolheu: ' + database[team]['name'])
            input('Precione enter para começar! ')
            partidas(userteam, season, database)
else:
    print('Numero invalido!')

print('-------')
print('###############################')
print('###### Oitavas de Finais ######')
print('###############################')
# Oitavas de Finais
grupos_ordenados = ordenar_fase_final(grupos_dict)

oitavas_de_final = []
lista_round_16 = []

for i in range(0, 8, 2):
    round_i = []
    round_i.append(grupos_ordenados[i][0])
    round_i.append(grupos_ordenados[i+1][1])
    oitavas_de_final.append(tuple(round_i))
    lista_round_16.append(round_i)
for i in range(1, 8, 2):
    round_i = []
    round_i.append(grupos_ordenados[i][0])
    round_i.append(grupos_ordenados[i-1][1])
    oitavas_de_final.append(tuple(round_i))
    lista_round_16.append(round_i)

zerar_pontuacao(database)
partidas_fase_final(userteam, [oitavas_de_final], database)


# Quartas de Finais
print(" ")
print('###############################')
print('###### Quartas de Finais ######')
print('###############################')
quartas_de_final = realizar_etapa_final(listar_equipes(lista_round_16), 8, database)

# Semi Finais
print(" ")
print('###############################')
print('######### Semi Finais #########')
print('###############################')
semi_finais = realizar_etapa_final(listar_equipes(quartas_de_final), 4, database)

# Final
print(" ")
print('###############################')
print("############ Final ###########")
print('###############################')

final = realizar_etapa_final(listar_equipes(semi_finais), 2, database)
