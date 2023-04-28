import json
from game import matchday
from richladder import createrichladder
from team import Team
from jogador import Jogador

# Tempo de duracao das partidas
TEMPO_GROUP_STAGE = 91
TEMPO_PLAYOFFS = 121

#Adicionar verificacoes
def substituir_jogador(equipe):
    print_escalacao(equipe)

    # Solicita o número do jogador titular que será substituído
    numero_titular = int(input("Digite o número do jogador titular que deseja substituir: "))

    # Localiza o jogador titular correspondente e obtém sua posição original
    for i, jogador in enumerate(equipe.players):
        if jogador.numero == numero_titular:
            jogador_titular = jogador
            posicao_original = i
            equipe.players.pop(i)
            break
        else: 
            print("Numero não existe!!")
    # Solicita o número do jogador reserva que irá substituir o titular
    numero_reserva = int(input("Digite o número do jogador reserva que irá substituir o titular: "))

    # Localiza o jogador reserva correspondente e insere na posição original do titular
    for i, jogador in enumerate(equipe.reservas):
        if jogador.numero == numero_reserva:
            equipe.reservas.pop(i)
            equipe.players.insert(posicao_original, jogador)
            equipe.reservas.insert(i, jogador_titular)
            break
    
    print_escalacao(equipe)  


def print_escalacao(equipe):
    print("--Titulares--")
    for jogador in equipe.players:
        print("{}   {} - {}".format(jogador.numero, jogador.nome, jogador.posicao))
    print("--Reservas--")
    for jogador in equipe.reservas:
        print("{}   {} - {}".format(jogador.numero, jogador.nome, jogador.posicao))


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
def partidas(userteam, season, database, tempo_partida, fase):
    partida_rapida = True
    partida_longa = False
    
    with open('data/teams_jogadores.txt', 'w') as json_file:
        json.dump(database, json_file, indent=4)

    teamcolor = "dark_olive_green3 bold italic"
    leaguecolor = "red1"
    gameweeknum = 0
    for week in season:
        #used to print gameweeks
        gameweeknum += 1

        # newweek é criado para garantir que o time do usuario esteja sempre a frente dos outros para melhor legibilidade
        # (o userteam é removido da posição que esteja e logo após isso é inserido na posição 0 novamente)
        newweek = []
        for matchbrackets in week:
            newweek.append(matchbrackets)
            for m in newweek:
                if userteam in m:
                    newweek.remove(m)
                    newweek.insert(0, m)
          
        if userteam == newweek[0][0]:
            print('Seu proximo adversário sera: {}'.format(newweek[0][1]))
        elif userteam == newweek[0][0]:
            print('Seu proximo adversário sera: {}'.format(newweek[0][0]))
        
            
        

        # Para cada match em uma week, configura o jogo usando versões temporarias da classe time
        for matchbrackets in newweek:
            match0 = []
            match1 = []
            for team in matchbrackets:
                match0.append(team)
            team1 = Team(0, str(match0[0]), 0, 0, 0, 0, 0, 0, 0, 0, database[match0[0]]['jogadores'])
            team2 = Team(0, str(match0[1]), 0, 0, 0, 0, 0, 0, 0, 0, database[match0[1]]['jogadores'])
            
            # Adiciona os jogadores do database às equipes
            
            # Adiciona titulares
            for i, team_name in enumerate([team1.name, team2.name]):
                for jogador in database[team_name]['jogadores'][:11]:
                    jogador = Jogador(jogador['nome'], jogador['numero'], jogador['gols'], jogador['posicao'], jogador['passe'], jogador['finalizacao'], jogador['defesa'], jogador['interceptacao'], jogador['penalty'],  jogador['stamina'], jogador['ball_control'], jogador['GK_skill'])
                    if i == 0:
                        team1.adicionar_jogador(jogador)
                    else:
                        team2.adicionar_jogador(jogador)
            
            # Adiciona reservas            
            for i, team_name in enumerate([team1.name, team2.name]):
                for jogador in database[team_name]['jogadores'][12:]:
                    jogador = Jogador(jogador['nome'], jogador['numero'], jogador['gols'], jogador['posicao'], jogador['passe'], jogador['finalizacao'], jogador['defesa'], jogador['interceptacao'], jogador['penalty'],  jogador['stamina'], jogador['ball_control'], jogador['GK_skill'])
                    if i == 0:
                        team1.adicionar_reservas(jogador)
                    else:
                        team2.adicionar_reservas(jogador)

            match1.append(team1)
            match1.append(team2) 

            # Se o time do usuario estiver no matchbracket
            if userteam in match0:
                # Pergunta se o usuario ira jogar ou skippar o proximo jogo
                print("1. Jogar")
                print("2. Skip")
                gamechoice = input("Gostaria de Jogar ou Pular o jogo? ")
                print(" ")
                # Pergunta se o usuario quer fazer alterações na escalação
                print('1. Editar Escalação')
                print('2. Usar Escalação Padrão')
                escalacao_choice = input("Gostaria de editar a escalação? ")
                if escalacao_choice == "1":
                    if userteam == match0[0]:
                        while True:
                            substituir_jogador(team1)
                            print(" ")
                            print("1. Sim")
                            print("2. Não")
                            mais_subistituicoes = input("Fazer mais mudanças? ")
                            if mais_subistituicoes != "1":
                                break
                    else:
                        while True:
                            substituir_jogador(team2)
                            print(" ")
                            print("1. Sim")
                            print("2. Não")
                            mais_subistituicoes = input("Fazer mais mudanças? ")
                            if mais_subistituicoes != "1":
                                break
                print(' ')
                # Se o usuario escolher o modo Play:
                if gamechoice == "1":
                    print(match0[0] + " vs " + match0[1])
                    print(' ')
                    matchday(match1, database, partida_rapida, tempo_partida, fase)
                    print(' ')
                    # print('Gameweek: ' + str(gameweeknum))
                    # print(' ')
                    input('Pressione algo para continuar..')
                # Se o usuario escolher Skip (Modo Rapido):
                else:
                    matchday(match1, database, partida_longa, tempo_partida, fase)
                    print(' ')
                    # print('Gameweek: ' + str(gameweeknum))
                    # print(' ')
                    input('Pressione algo para continuar..')
            else:
                matchday(match1, database, partida_longa, tempo_partida, fase)

            with open('data/teams_jogadores.txt', 'w') as json_file:
                json.dump(database, json_file, indent=4)
               
        if fase == 'grupos':
            input('Pressione algo para continuar..')
            print(' ')
            for grupos in grupos_dict:
                createrichladder(grupos, leaguecolor, teamcolor, userteam, gameweeknum)
            print(' ')


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
    lista_partidas = [(equipes_ordenadas[i][0], equipes_ordenadas[i + 1][0])for i in range(0, num_equipes_proxima_etapa, 2)]

    # Zerar a pontuação das equipes
    zerar_pontuacao(database)

    # Realizar as partidas da próxima etapa
    partidas(userteam, [lista_partidas], database, TEMPO_PLAYOFFS, 'playoffs')

    resultado_partidas = [[equipes_ordenadas[i][0], equipes_ordenadas[i + 1][0]]
                for i in range(0, num_equipes_proxima_etapa, 2)]

    return resultado_partidas


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

# Zera pontuacao dos times
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
            # print('Escalação')
            # for jogador in database[team]['jogadores']:
            #     print('-' + jogador['nome'])
            input('Precione enter para começar! ')
            partidas(userteam, season, database, TEMPO_GROUP_STAGE, 'grupos')
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
partidas(userteam, [oitavas_de_final], database, TEMPO_PLAYOFFS, 'playoffs')


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
