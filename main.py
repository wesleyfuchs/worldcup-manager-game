import json
from controllers.game import matchday
from views.richladder import criar_tabela
from models.team import Team
from models.jogador import Jogador
from controllers.database import load_data, save_data, zerar_pontuacao, reset_player_stats, reset_team_stats, ordenar_fase_final, listar_equipes
from logging_config import setup_logging
import logging

# Configurar logs
setup_logging()
logging.info("Programa iniciado.")

# Tempo de duracao das partidas
TEMPO_GROUP_STAGE = 91
TEMPO_PLAYOFFS = 121

# Carregar o banco de dados
database = load_data('data/teams_jogadores.txt')
logging.info(f"Banco de dados carregado com {len(database)} times.")

# Resetar estatísticas
reset_team_stats(database)
reset_player_stats(database)
zerar_pontuacao(database)

# Salva as alterações de volta no arquivo json
save_data('data/teams_jogadores.txt', database)


def substituir_jogador(team):
    """
    Permite ao usuário substituir um jogador suspenso ou titular.
    """
    while True:
        print(f"\n🔄 Substituições para {team.name}:")
        print("Titulares:")
        for jogador in team.players:
            print(f"{jogador.numero} - {jogador.nome}")

        print("\nReservas:")
        for jogador in team.reservas:
            print(f"{jogador.numero} - {jogador.nome}")

        numero_titular = input("\nDigite o número do jogador titular que deseja substituir (ou pressione Enter para cancelar): ").strip()
        
        # 📌 Se o usuário pressionar Enter sem digitar nada, cancelar a substituição
        if not numero_titular:
            print("❌ Substituição cancelada.")
            return

        # 📌 Verificar se a entrada é um número válido
        if not numero_titular.isdigit():
            print("⚠️ Entrada inválida! Digite um número correspondente a um jogador titular.")
            continue  # Perguntar novamente

        numero_titular = int(numero_titular)

        # 📌 Encontrar o jogador titular pelo número
        jogador_titular = next((j for j in team.players if j.numero == numero_titular), None)

        if not jogador_titular:
            print("⚠️ Número inválido! O jogador não está na lista de titulares.")
            continue

        # 📌 Se não houver reservas, não há substituições disponíveis
        if not team.reservas:
            print("⚠️ Nenhum reserva disponível para substituição.")
            return

        # 📌 Mostrar opções de substituição
        print("\nEscolha um reserva para substituir:")
        for i, jogador_reserva in enumerate(team.reservas, start=1):
            print(f"{i}. {jogador_reserva.nome}")

        numero_reserva = input("\nDigite o número do reserva escolhido: ").strip()

        if not numero_reserva.isdigit():
            print("⚠️ Entrada inválida! Digite um número correspondente a um reserva.")
            continue

        numero_reserva = int(numero_reserva) - 1

        if numero_reserva < 0 or numero_reserva >= len(team.reservas):
            print("⚠️ Número inválido! Escolha um reserva da lista.")
            continue

        # 📌 Substituir o jogador titular pelo reserva escolhido
        jogador_substituto = team.reservas.pop(numero_reserva)
        team.players.remove(jogador_titular)
        team.players.append(jogador_substituto)

        print(f"✅ {jogador_titular.nome} foi substituído por {jogador_substituto.nome}.")

        return  # Sai da função após uma substituição bem-sucedida


def print_escalacao(equipe):
    print("--Titulares--")
    for jogador in equipe.players:
        print("{}   {} - {}".format(jogador.numero, jogador.nome, jogador.posicao))
    print("--Reservas--")
    for jogador in equipe.reservas:
        print("{}   {} - {}".format(jogador.numero, jogador.nome, jogador.posicao))


def mostrar_pontuacao_times(database):
    '''print da pontuação dos times'''
    print('----')
    for team in database:
        print(str(database[team]["name"]) +
              " - " + str(database[team]["score"]))
    print('----')


def verificar_suspensoes(team, database, userteam):
    """
    Remove jogadores suspensos da escalação antes da partida.
    Substitui automaticamente jogadores suspensos para times da CPU.
    
    Parâmetros:
        team (Team): O time a ser verificado.
        database (dict): O banco de dados contendo informações dos times e jogadores.
    """

    # if not hasattr(team, "suspensos"):
    #     team.suspensos = []

    jogadores_disponiveis = []
    jogadores_suspensos = []

    # Separar jogadores suspensos e disponíveis
    for jogador in team.players:
        if jogador.nome in team.suspensos:
            jogadores_suspensos.append(jogador)
        else:
            jogadores_disponiveis.append(jogador)

    # 🔍 Debug: Exibir jogadores suspensos e disponíveis
    print(f"\n🔎 {team.name} - Jogadores suspensos: {[j.nome for j in jogadores_suspensos]}")
    print(f"🔎 {team.name} - Jogadores disponíveis antes da substituição: {[j.nome for j in jogadores_disponiveis]}")

    # Para times da CPU, substituir automaticamente os suspensos
    if team.name != userteam:
        for jogador_suspenso in jogadores_suspensos:
            logging.info(f"{jogador_suspenso.nome} está suspenso e será substituído automaticamente no {team.name}.")
            
            if team.reservas:
                substituto = team.reservas.pop(0)
                jogadores_disponiveis.append(substituto)
                print(f"✅ {team.name} - {jogador_suspenso.nome} foi substituído por {substituto.nome}.")

    # 📌 Se for o time do usuário, obrigá-lo a substituir manualmente
    else:
        if jogadores_suspensos:
            print(f"\n⚠️ Os seguintes jogadores estão suspensos e não podem jogar: {', '.join([j.nome for j in jogadores_suspensos])}")
            print("Você deve substituí-los antes de iniciar a partida.")

            while jogadores_suspensos:
                substituir_jogador(team)  # Chama a função de substituição
                jogadores_suspensos = [j for j in jogadores_suspensos if j.nome in [p.nome for p in team.players]]
    
    # Atualiza a lista de titulares
    team.players = jogadores_disponiveis

    # 🔍 Debug: Exibir a nova lista de titulares após substituição
    print(f"🔎 {team.name} - Titulares após substituições: {[j.nome for j in team.players]}\n")


#Arrumar o quickgame(nomes invertidos)
def partidas(userteam, season, database, tempo_partida, fase):
    partida_rapida = True
    partida_longa = False

    teamcolor = "dark_olive_green3 bold italic"
    leaguecolor = "red1"
    gameweeknum = 0
    for week in season:
        
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

            team1 = Team(0, str(match0[0]), 0, 0, 0, 0, 0, 0, 0, 0, database[match0[0]]['jogadores'], database[match0[0]]['suspensos'])
            team2 = Team(0, str(match0[1]), 0, 0, 0, 0, 0, 0, 0, 0, database[match0[1]]['jogadores'], database[match0[1]]['suspensos'])
            
            # Adiciona os jogadores do database às equipes
            # Adiciona titulares
            for i, team_name in enumerate([team1.name, team2.name]):
                for jogador in database[team_name]['jogadores'][:11]:
                    jogador = Jogador(jogador['nome'], jogador['numero'], jogador['gols'], jogador['posicao'], jogador['passe'], jogador['finalizacao'], jogador['defesa'],
                                       jogador['interceptacao'], jogador['penalty'],  jogador['stamina'], jogador['ball_control'], 
                                       jogador['GK_skill'], jogador['assistencias'], jogador['cartoes_amarelos'], jogador['cartoes_vermelhos'])
                    if i == 0:
                        team1.adicionar_jogador(jogador)
                    else:
                        team2.adicionar_jogador(jogador)
            
            # Adiciona reservas            
            for i, team_name in enumerate([team1.name, team2.name]):
                for jogador in database[team_name]['jogadores'][12:]:
                    jogador = Jogador(jogador['nome'], jogador['numero'], jogador['gols'], jogador['posicao'], jogador['passe'], jogador['finalizacao'], jogador['defesa'], 
                                      jogador['interceptacao'], jogador['penalty'],  jogador['stamina'], jogador['ball_control'], 
                                      jogador['GK_skill'], jogador['assistencias'], jogador['cartoes_amarelos'], jogador['cartoes_vermelhos'])
                    if i == 0:
                        team1.adicionar_reservas(jogador)
                    else:
                        team2.adicionar_reservas(jogador)

             # ✅ Impede jogadores suspensos de jogar
            verificar_suspensoes(team1, database, userteam)
            verificar_suspensoes(team2, database, userteam)

            match1.append(team1)
            match1.append(team2)  

            # Se o time do usuario estiver no matchbracket
            if userteam in match0:
                logging.info(f"Partida iniciada: {team1.name} vs {team2.name}.")
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


        save_data('data/teams_jogadores.txt', database)

        if fase == 'grupos':
            input('Pressione algo para continuar..')
            print(' ')
            for grupos in grupos_dict:
                criar_tabela(grupos, leaguecolor, teamcolor, userteam, gameweeknum)
            print(' ')


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


# with open('data/teams_jogadores.txt', encoding='utf-8') as f:
#     database = json.load(f)

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
quartas_de_final = realizar_etapa_final(listar_equipes(lista_round_16, database), 8, database)

# Semi Finais
print(" ")
print('###############################')
print('######### Semi Finais #########')
print('###############################')
semi_finais = realizar_etapa_final(listar_equipes(quartas_de_final, database), 4, database)

# Final
print(" ")
print('###############################')
print("############ Final ###########")
print('###############################')

final = realizar_etapa_final(listar_equipes(semi_finais, database), 2, database)
