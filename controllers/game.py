import random
import time
from logging_config import setup_logging
import logging

from models.jogador import Jogador
from rich.console import Console
from rich.table import Table

# Configurar logs
setup_logging()

def aplicar_suspensao(jogador, team):
    """
    Adiciona o jogador à lista de suspensos e controla suspensão por acúmulo de amarelos.
    
    Parâmetros:
        jogador (Jogador): O jogador que recebeu o cartão vermelho ou acumulou amarelos.
        team (Team): O time ao qual o jogador pertence.
    """

    if not hasattr(team, "suspensos"):  # Garante que a lista de suspensos existe
        team.suspensos = []

    # 🔥 Se o jogador recebeu um cartão vermelho, ele é suspenso automaticamente
    if jogador.cartao_vermelho and jogador.nome not in team.suspensos:
        team.suspensos.append(jogador.nome)  # Armazena apenas o nome do jogador
        logging.info(f"🚫 {jogador.nome} está suspenso para a próxima partida do {team.name} por expulsão.")

    # 🔥 Se acumulou 3 amarelos ao longo das partidas, é suspenso na próxima
    elif jogador.cartoes_amarelos >= 3 and jogador.nome not in team.suspensos:
        team.suspensos.append(jogador.nome)
        logging.info(f"🚫 {jogador.nome} está suspenso para a próxima partida do {team.name} por acúmulo de 3 amarelos.")
        jogador.cartoes_amarelos = 0  # Reseta os amarelos APÓS a suspensão ser aplicada


def registrar_cartao(jogador, tipo, team, exibir_eventos=True):
    """
    Registra um cartão para um jogador e aplica suspensão conforme necessário.
    
    Parâmetros:
        jogador (Jogador): O jogador que recebeu o cartão.
        tipo (str): Tipo do cartão ('amarelo' ou 'vermelho').
        team (Team): O time ao qual o jogador pertence.
        exibir_eventos (bool): Se True, imprime o evento no console.
    """

    if jogador.cartao_vermelho:
        logging.warning(f"Tentativa de dar um cartão para {jogador.nome}, mas ele já foi expulso!")
        return  

    if tipo == "amarelo":
        jogador.recebeu_cartao_amarelo()

        if jogador.cartoes_amarelos_na_partida == 2:
            # 🔥 Se for o segundo amarelo NA MESMA PARTIDA, vira vermelho
            jogador.cartao_vermelho = True
            jogador.cartoes_vermelhos += 1  
            
            logging.info(f"🟡🟡 {jogador.nome} recebeu o segundo amarelo na mesma partida e foi expulso! 🔴")

            if exibir_eventos:
                print(f"🟡🟡 {jogador.nome} recebeu o segundo amarelo e foi expulso! 🔴")

            aplicar_suspensao(jogador, team)  # Suspensão automática

        elif jogador.cartoes_amarelos >= 3:
            # 🔥 Se acumulou 3 amarelos ao longo das partidas, será suspenso na próxima
            aplicar_suspensao(jogador, team)

        else:
            logging.info(f"🟡 Cartão Amarelo: {jogador.nome}")
            if exibir_eventos:
                print(f"🟡 Cartão Amarelo para {jogador.nome}!")

    elif tipo == "vermelho":
        jogador.recebeu_cartao_vermelho()
        jogador.cartao_vermelho = True
        
        logging.info(f"🔴 Cartão Vermelho direto! {jogador.nome} foi expulso do time {team.name}.")

        if exibir_eventos:
            print(f"🔴 Cartão Vermelho para {jogador.nome}! Expulso da partida!")

        aplicar_suspensao(jogador, team)  # Suspensão automática


def registrar_gol(team, jogador, exibir_eventos=True):
    """Registra um gol e exibe o evento apenas se necessário."""
    team.goals += 1
    jogador.gol()
    logging.info(f"GOL! {jogador.nome} marcou para {team.name}")

    if exibir_eventos:
        print(f"Gooool! {team.name} marcou! ⚽")


def quickgoal_sofrido(team):
    team.goals_sofridos += 1
    
#Preciso ver como refatorar isso aqui
def cobrança_penalty(match):
    for i in match:
        nVar_penalti = random.randint(0,4)
        if nVar_penalti > 1:
            i.penalti_goals += 1
            # print(str(i.name) + ' ' + "Penalty Convertido! ✅")
            logging.info(f"Pênalti convertido por {i.name}")
        else:
            # print(str(i.name) + ' ' + "Penalty Perdido!    ❌")
            logging.info(f"Pênalti perdido por {i.name}")
        time.sleep(0.5)


def quickcobrança_penalty(match):
    for i in match:
        nVar_penalti = random.randint(0,4)
        if nVar_penalti > 1:
            i.penalti_goals += 1
            logging.debug(f"Pênalti convertido por {i.name}")
        else:
            logging.debug(f"Pênalti perdido por {i.name}")


def definir_posse_de_bola(team, meia_central_preferido=True):
    """
    Define a posse de bola para um time e escolhe um jogador para iniciar a jogada.

    Parâmetros:
        team (Team): O time que terá a posse de bola.
        meia_central_preferido (bool): Se True, tenta escolher o meia central (jogador 10). Se False, escolhe qualquer jogador.

    Retorna:
        jogador_com_bola (Jogador): O jogador que inicia a posse de bola.
    """
    # Remove posse de bola de todos os jogadores do time
    for jogador in team.players:
        jogador.posse_de_bola = False

    # Escolher meia central (jogador 10) se ele ainda estiver disponível
    if meia_central_preferido:
        jogador_central = next((j for j in team.players if j.numero == 10), None)
        if jogador_central:  # Se o jogador 10 estiver disponível, ele recebe a posse
            jogador_central.posse_de_bola = True
            team.ball_possession = True
            logging.info(f"{team.name} começa com a posse de bola ({jogador_central.nome}).")
            return jogador_central

    # Se não for o início ou o jogador 10 estiver expulso, escolhe um jogador aleatório
    jogador_com_bola = random.choice(team.players)
    jogador_com_bola.posse_de_bola = True
    team.ball_possession = True

    logging.info(f"{team.name} inicia a posse de bola com {jogador_com_bola.nome}.")
    
    return jogador_com_bola


def inicializar_contadores(match):
    """
    Inicializa os contadores de estatísticas da partida.

    Parâmetros:
        match (list): Lista contendo os dois times.

    Retorna:
        dict: Dicionário com os contadores da partida.
    """
    contadores = {
        "team_0_ball_possession": 0,
        "team_1_ball_possession": 0,
        "gols_evento": [],
    }

    # Inicializa estatísticas de chutes
    for team in match:
        team.chutes = 0
        team.chutes_gol = 0

    return contadores


def matchday(match, json, quick_game, duracao_partida, fase):
    """
    Simula uma partida entre dois times.

    Parâmetros:
        match (list): Lista com os times que irão jogar.
        json (dict): Banco de dados dos times.
        quick_game (bool): Define se o jogo será rápido (sem exibição) ou detalhado.
        duracao_partida (int): Duração total da partida.
        fase (str): Define se a partida é de fase de grupos ou mata-mata.
    """
    logging.info(f"Iniciando partida: {match[0].name} vs {match[1].name}")
    
    # Define quem começa com a bola (meia central preferido no início do jogo)
    time_inicial = random.choice(match)
    jogador_com_bola = definir_posse_de_bola(time_inicial, meia_central_preferido=True)
    contadores = inicializar_contadores(match)

    # Simulação da partida
    for i in range(0, duracao_partida):
        if quick_game == True:
            if i == 46:
                print('Intervalo! ⏱️')
            elif i == 92:
                print('Fim do Tempo Regulamentar! ⏱️')
                if match[0].goals > match[1].goals or match[0].goals < match[1].goals: 
                    break
                else:
                    print('Prorrogação!!')
            elif i == 106:
                print('Intervalo! ⏱️')
                
        n1 = random.randint(1, 100)
        event = ""

        if match[0].ball_possession == True:
            current_team = match[0]
            contadores["team_0_ball_possession"] += 1
        else:
            current_team = match[1]
            contadores["team_1_ball_possession"] += 1

        other_team = match[1] if current_team == match[0] else match[0]
        # Verifique qual jogador está com a bola
        for jogador in current_team.players:
            if jogador.posse_de_bola == True:
                jogador_com_bola = jogador
                

        # Execute as instruções para o jogador com a bola
        if jogador_com_bola.posicao == "GK":
            if quick_game == True:
                jogador_com_bola.decisao_posse_de_bola()
                jogador_destino = random.choice(current_team.players)
                jogador_com_bola.passar_bola(jogador_destino)
            else:
                jogador_destino = random.choice(current_team.players)
                jogador_com_bola.passar_bola_quick(jogador_destino)
        else:
            # Nao acontece nada
            if n1 <= 5:
                if quick_game == True:
                    event = " "             
                    jogador_com_bola.decisao_posse_de_bola()
            # Disputa de bola
            elif n1 <= 30:
                # Chance de troca da posse de bola
                ball_possession_change = random.randint(0, 10)
                if ball_possession_change < 8:
                    pass
                else:
                    # Calcula a chance de manter a posse da bola
                    ladrao_bola = random.choice(other_team.players)
                    if jogador_com_bola.ball_control < ladrao_bola.defesa:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        ladrao_bola.posse_de_bola = True
            # Passar a bola
            elif n1 <= 75:
                # Chance de errar o passe
                    ladrao_bola = random.choice(other_team.players)
                    if jogador_com_bola.passe < ladrao_bola.interceptacao:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        ladrao_bola.posse_de_bola = True
                    else:
                        if quick_game == True:
                            jogador_destino = random.choice(current_team.players)
                            jogador_com_bola.passar_bola(jogador_destino)
                        else:
                            jogador_destino = random.choice(current_team.players)
                            jogador_com_bola.passar_bola_quick(jogador_destino)
            # Chute
            elif n1 <= 95:
                if quick_game == True:
                    jogador_com_bola.chute()
                current_team.chutes+=1
                n4_1 = random.randint(0,10)
                n4_2 = random.randint(5,10) 
                if n4_1 > n4_2:
                    n5_1 = random.randint(0,100)
                    n5_2 = random.randint(80,100)
                    current_team.chutes_gol+=1 
                    if (jogador_com_bola.finalizacao + n5_1) > (other_team.players[0].GK_skill + n5_2):
                        event = str(i) + """' """ + str(jogador_com_bola.nome)
                        contadores["gols_evento"].append(event)
                        if quick_game == True:
                            registrar_gol(current_team, jogador_com_bola, exibir_eventos=True)  # Exibe o gol e registra no log
                            if jogador_com_bola.assistindo:
                                jogador_com_bola.assistindo.assistencias += 1
                            jogador_com_bola.assistindo = None
                        else:
                            registrar_gol(current_team, jogador_com_bola, exibir_eventos=False) # Apenas registra no log
                            if jogador_com_bola.assistindo:
                                jogador_com_bola.assistindo.assistencias += 1
                            jogador_com_bola.assistindo = None
                        quickgoal_sofrido(other_team)
                        current_team.ball_possession = False
                        jogador_com_bola = definir_posse_de_bola(other_team, meia_central_preferido=False)
                    else:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        other_team.players[0].posse_de_bola = True
                else:
                    current_team.ball_possession = False
                    other_team.ball_possession = True
                    other_team.players[0].posse_de_bola = True

            #Falta
            elif n1 <= 99:
                if random.randint(1, 10) >= 8:  # Chance de falta que gera cartão
                    jogadores_disponiveis = [j for j in other_team.players if not j.cartao_vermelho]
                    if jogadores_disponiveis:
                        jogador_faltoso = random.choice(jogadores_disponiveis)
                        if random.randint(1, 100) >= 85:
                            print('vermelho')
                            pass
                            # registrar_cartao(jogador_faltoso, "vermelho", other_team, exibir_eventos=quick_game)
                        else:
                            print('amarelo')
                            registrar_cartao(jogador_faltoso, "amarelo", other_team, exibir_eventos=quick_game)
                    # Cobrança falta
                    n3_1 = random.randint(0,10)
                    if n3_1 >= 9:
                        event = str(i) + """' """ + str(jogador_com_bola.nome) + " (Cobr. de Falta)"
                        contadores["gols_evento"].append(event)
                        current_team.chutes+=1
                        current_team.chutes_gol+=1
                        if quick_game == True: 
                            registrar_gol(current_team, jogador_com_bola, exibir_eventos=True)  # Exibe o gol e registra no log
                        else:
                            registrar_gol(current_team, jogador_com_bola, exibir_eventos=False) # Apenas registra no log
                        quickgoal_sofrido(other_team)
                        current_team.ball_possession = False
                        jogador_com_bola = definir_posse_de_bola(other_team, meia_central_preferido=False)
                    else:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        other_team.players[0].posse_de_bola = True    
            else:
                if quick_game == True:
                    print("VAR: Checando Possivel Penalty! 📺")
                    time.sleep(1)
                #Checa com quem esta a bola para decidir para qual lado ira a decisão do VAR
                nVar = random.randint(0,10)
                if current_team.ball_possession:
                    varteam = current_team
                    varlteam = other_team
                else:
                    varteam = other_team
                    varlteam = current_team
                #60% Chance de penalty
                if nVar > 5:
                    if quick_game == True:
                        print("Penalty para " + str(varteam.name) + "!")
                    nVar_2 = random.randint(0,100)
                    nVar_3 = random.randint(20,100)
                    if (jogador_com_bola.penalty + nVar_2) > (other_team.players[0].GK_skill + nVar_3):
                        event = str(i) + """' """ + str(jogador_com_bola.nome) + " (Penalty)"
                        contadores["gols_evento"].append(event)
                        if quick_game == True:
                            registrar_gol(varteam, jogador_com_bola, exibir_eventos=True)  # Exibe o gol e registra no log
                        else:
                            registrar_gol(varteam, jogador_com_bola, exibir_eventos=False) # Apenas registra no log
                        quickgoal_sofrido(varlteam)
                        current_team.ball_possession = False
                        jogador_com_bola = definir_posse_de_bola(other_team, meia_central_preferido=False)
                    else:
                        if quick_game == True:
                            print("Penalty Perdido! ❌")
                else:
                    if quick_game == True:
                        print("Penalty não marcado! ❌")
        if quick_game == True:
            time.sleep(0.15)
            print(str(i) + """' """ + event)
        # print(n1)

    # Depois do fim da paritda
    if fase == 'playoffs':
        #Penalidades Maximas   
        cobrancas_de_penalty = 5
        if match[0].goals == match[1].goals:
            while cobrancas_de_penalty > 0:
                #Checar se o numero de gols ainda pode ser igualado
                if (match[0].penalti_goals + cobrancas_de_penalty) < match[1].penalti_goals:
                    break
                if (match[1].penalti_goals + cobrancas_de_penalty) < match[0].penalti_goals:
                    break
                #Cobrancas de penalty
                if quick_game == True:
                    cobrança_penalty(match)
                    #Print
                    print(str(match[0].penalti_goals) + '-' + str(match[1].penalti_goals))
                    #contador
                    cobrancas_de_penalty -= 1   
                    time.sleep(0.5)
                else:
                    quickcobrança_penalty(match)
                    #contador
                    cobrancas_de_penalty -= 1           

        #Caso empate apos 5 cobranças
        if cobrancas_de_penalty == 0:     
            if match[0].penalti_goals == match[1].penalti_goals:
                while match[0].penalti_goals == match[1].penalti_goals:
                    if quick_game == True:
                        cobrança_penalty(match)
                    else:
                        quickcobrança_penalty(match)
    
    
    # Atualiza os gols marcados/gols sofridos de cada time
    for team in match:
        for i in json:
            if i == team.name:
                json[i]["goals"] += team.goals 
                json[i]["goals_sofridos"] += team.goals_sofridos
                json[i]["goaldif"] += (team.goals - team.goals_sofridos)

                # Se não existir "suspensos", cria a chave no JSON
                if "suspensos" not in json[i]:
                    json[i]["suspensos"] = []

                # Converte todos os objetos "Jogador" em nomes antes de salvar
                nomes_suspensos = [jogador.nome if isinstance(jogador, Jogador) else jogador for jogador in team.suspensos]

                # Adiciona apenas os novos suspensos que ainda não estão no JSON
                for nome in nomes_suspensos:
                    if nome not in json[i]["suspensos"]:
                        json[i]["suspensos"].append(nome)  # Adiciona apenas o nome do jogador
     

    # Atualiza a lista de jogadores no arquivo JSON com os gols, assistências e cartões
    for team in match:
        for jogador in team.players + [j for j in team.suspensos if isinstance(j, Jogador)]:
            for i in json[team.name]["jogadores"]:
                if i["nome"] == jogador.nome:
                    i["gols"] = jogador.gols
                    i["assistencias"] = jogador.assistencias
                    i["cartoes_amarelos"] = jogador.cartoes_amarelos
                    i["cartoes_vermelhos"] = jogador.cartoes_vermelhos
                    i["cartoes_amarelos_na_partida"] = 0

    # Declarando Vencedor, Perdedor e Empate
    winner = ""
    loser = ""
    draw = False
    if match[0].goals > match[1].goals:
        winner = match[0].name
        loser = match[1].name
    elif match[0].goals < match[1].goals:
        winner = match[1].name
        loser = match[0].name
    elif match[0].penalti_goals > match[1].penalti_goals:
        winner = match[0].name
        loser = match[1].name
    elif match[0].penalti_goals < match[1].penalti_goals:
        winner = match[1].name
        loser = match[0].name
    else:
        draw = True

    if draw == True:
        for i in json:
            for team in match:
                if i == team.name:
                    json[i]["drawn"] += 1
                    json[i]["score"] += 1
    else:
        for i in json:
            if i == winner:
                json[i]["score"] += 3
                json[i]["won"] += 1
            if i == loser:
                json[i]["lost"] += 1
        
    #calcula a porcentagem de posse de bola de cada time
    total_possession = contadores["team_0_ball_possession"] + contadores["team_1_ball_possession"]
    team_0_percentage = (contadores["team_0_ball_possession"] / total_possession) * 100
    team_1_percentage = (contadores["team_1_ball_possession"] / total_possession) * 100

    if quick_game == True:
        print(' ')

    #imprime a porcentagem de posse de bola de cada time
        print("Posse de bola para {}: {}%".format(match[0].name, round(team_0_percentage)))
        print("Posse de bola para {}: {}%".format(match[1].name, round(team_1_percentage)))
        print(' ')
        
        #imprime os chutes
        print('Total de chutes {}: {}({})(ao gol)'.format(match[0].name, match[0].chutes, match[0].chutes_gol))
        print('Total de chutes {}: {}({})(ao gol)'.format(match[1].name, match[1].chutes, match[1].chutes_gol))
        print(' ')
        
        #Gols
        for evento in contadores["gols_evento"]:
            print(evento)
        
        # for jogador in match[0].players:
        #     if jogador.gols > 0:
        #         print('{} Gols de {}'.format(jogador.gols, jogador.nome))
            
        # for jogador in match[1].players:
        #     if jogador.gols > 0:
        #         print('{} Gols de {}'.format(jogador.gols, jogador.nome))
      
    # Print do Resultado
    table = Table(show_header=False)
    table.add_column(justify="right", width=10)
    table.add_column(justify="right", width=2)
    table.add_column(justify="left", width=2)
    table.add_column(justify="left", width=10)
    
    console = Console()

    if match[0].penalti_goals > 0 or match[1].penalti_goals > 0:
        table.add_row(str(match[0].name), str(match[0].goals), str(match[1].goals), str(match[1].name))
        table.add_row(str(" "), str(match[0].penalti_goals), str(match[1].penalti_goals), str(" "))
    else:
        table.add_row(str(match[0].name), str(match[0].goals), str(match[1].goals), str(match[1].name))   
          
    console.print(table)
      
    # return print(str(match[0].name) + ' ' + str(match[0].goals) + '-' + str(match[1].goals) + ' ' + str(match[1].name))
    return json    