import random
import time

from rich.console import Console
from rich.table import Table


def yellow(jogador):
    print("Cartão Amarelo para " + str(jogador.nome) + ' 🟡')
    jogador.cartao_amarelo = True
    

def quickyellow(jogador):
    jogador.cartao_amarelo = True


def red(jogador):
    print("Cartão Vermelho para " + str(jogador.nome) + ' 🔴')
    jogador.cartao_vermelho = True


def quickred(jogador):
    jogador.cartao_vermelho = True


def goal(team, jogador):
    print("Gooool! " + str(team.name) + " marcou! ⚽")
    team.goals += 1
    jogador.gol()


def quickgoal(team, jogador):
    team.goals += 1
    jogador.gol()


def quickgoal_sofrido(team):
    team.goals_sofridos += 1


def cobrança_penalty(match):
    for i in match:
        nVar_penalti = random.randint(0,4)
        if nVar_penalti > 1:
            i.penalti_goals += 1
            print(str(i.name) + ' ' + "Penalty Convertido! ✅")
        else:
            print(str(i.name) + ' ' + "Penalty Perdido!    ❌")
        time.sleep(0.5)


def quickcobrança_penalty(match):
    for i in match:
        nVar_penalti = random.randint(0,4)
        if nVar_penalti > 1:
            i.penalti_goals += 1


def matchday(match, json, quick_game, duracao_partida, fase):
    
    # Inicializa a posse de bola
    match[0].ball_possession = False
    match[1].ball_possession = False
    jogador_com_bola = None
    ball_possession_start = random.randint(1,100)
    if ball_possession_start > 50:
        match[0].ball_possession = True
        match[0].players[10].posse_de_bola = True
    else:
        match[1].ball_possession = True
        match[1].players[10].posse_de_bola = True
    
    # Inicializa contadores
    team_0_ball_possession = 0
    team_1_ball_possession = 0
    match[0].chutes = 0
    match[1].chutes = 0
    match[0].chutes_gol = 0
    match[1].chutes_gol = 0
    
    #Joga um jogo por 90 mins
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
            team_0_ball_possession += 1
        else:
            current_team = match[1]
            team_1_ball_possession += 1

        other_team = match[1] if current_team == match[0] else match[0]
        # Verifique qual jogador está com a bola
        for jogador in current_team.players:
            if jogador.posse_de_bola == True:
                jogador_com_bola = jogador
                
        qnt_jogadores_current_team = (len(current_team.players) - 1)
        qnt_jogadores_other_team = (len(other_team.players)- 1)
        
        # Execute as instruções para o jogador com a bola
        if jogador_com_bola.posicao == 'GK':
            if quick_game == True:
                jogador_com_bola.decisao_posse_de_bola()
                jogador_destino = current_team.players[random.randint(0, qnt_jogadores_current_team)]
                jogador_com_bola.passar_bola(jogador_destino)
            else:
                jogador_destino = current_team.players[random.randint(0, qnt_jogadores_current_team)]
                jogador_com_bola.passar_bola_quick(jogador_destino)
        else:
            # Nao acontece nada
            if n1 <= 5:
                if quick_game == True:
                    event = " "
                    jogador_com_bola.decisao_posse_de_bola()
            # Disputa de bola
            elif n1 <= 20:
                # Chance de troca da posse de bola
                ball_possession_change = random.randint(0, 10)
                if ball_possession_change < 8:
                    pass
                else:
                    # Calcula a chance de manter a posse da bola
                    ladrao_bola = other_team.players[random.randint(0,qnt_jogadores_other_team)]
                    if jogador_com_bola.ball_control < ladrao_bola.defesa:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        ladrao_bola.posse_de_bola = True
            # Passar a bola
            elif n1 <= 75:
                # Chance de errar o passe
                    ladrao_bola = other_team.players[random.randint(0,qnt_jogadores_other_team)]
                    if jogador_com_bola.passe < ladrao_bola.interceptacao:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        ladrao_bola.posse_de_bola = True
                    else:
                        if quick_game == True:
                            jogador_destino = current_team.players[random.randint(0, qnt_jogadores_current_team)]
                            jogador_com_bola.passar_bola(jogador_destino)
                        else:
                            jogador_destino = current_team.players[random.randint(0, qnt_jogadores_current_team)]
                            jogador_com_bola.passar_bola_quick(jogador_destino)
            # Chute
            elif n1 <= 95:
                if quick_game == True:
                    jogador_com_bola.chute()
                current_team.chutes+=1
                n4_1 = random.randint(0,10)
                n4_2 = random.randint(5,10) 
                if n4_1 > n4_2:
                    n5_1 = random.randint(0,50)
                    n5_2 = random.randint(0,60)
                    current_team.chutes_gol+=1 
                    if (jogador_com_bola.finalizacao + n5_1) > (other_team.players[0].GK_skill + n5_2):
                        if quick_game == True:
                            goal(current_team, jogador_com_bola)
                        else:
                            quickgoal(current_team, jogador_com_bola)
                        quickgoal_sofrido(other_team)
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        other_team.players[10].posse_de_bola = True
                    else:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        other_team.players[0].posse_de_bola = True
                else:
                    current_team.ball_possession = False
                    other_team.ball_possession = True
                    other_team.players[0].posse_de_bola = True
            #Falta
            elif n1 < 99:
                n2_1 = random.randint(1,10) 
                if n2_1 > 8:
                    # Cartao Amarelo
                    jogador_faltoso = other_team.players[random.randint(0, qnt_jogadores_other_team)]
                    if jogador_faltoso.cartao_amarelo == False:
                        if quick_game == True:
                            yellow(jogador_faltoso)
                        else:
                            quickyellow(jogador_faltoso)
                    else:
                        pass
                        # red(jogador_faltoso)
                        # for jogador in other_team.players:
                        #     if jogador.cartao_vermelho:
                        #         jogador_red_index = jogador
                        #         jogador_red_index = other_team.players.index(jogador_red_index)
                        #         jogador_red = other_team.players.pop(jogador_red_index)
                        #         other_team.suspensos.append(jogador_red)
                    # Cobrança falta
                    n3_1 = random.randint(1,10)
                    if n3_1 >= 9:
                        current_team.chutes+=1
                        current_team.chutes_gol+=1
                        if quick_game == True: 
                            goal(current_team, jogador_com_bola)
                        else:
                            quickgoal(current_team, jogador_com_bola)
                        quickgoal_sofrido(other_team)
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        other_team.players[10].posse_de_bola = True
                    else:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        other_team.players[0].posse_de_bola = True    
            else:
                if quick_game == True:
                    print("VAR: Checando Possivel Penalty! 📺")
                    time.sleep(1)
                #compares the random VAR number for each team plus their luck stat to determine who gets the penalty
                nVar = random.randint(0,10)
                if current_team.ball_possession:
                    varteam = current_team
                    varlteam = other_team
                else:
                    varteam = other_team
                    varlteam = current_team
                #70% chance for a penalty to be given
                if nVar > 4:
                    if quick_game == True:
                        print("Penalty para " + str(varteam.name) + "!")
                    #75% chance to get a goal from penalty
                    nVar_3 = random.randint(0,4)
                    if nVar_3 > 1:
                        if quick_game == True:
                            goal(varteam, jogador_com_bola)
                        else:
                            quickgoal(varteam, jogador_com_bola)
                        quickgoal_sofrido(varlteam)
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
    
    
    #adds goals for each of the teams at the end
    for team in match:
        for i in json:
            if i == team.name:
                json[i]["goals"] += team.goals 
                json[i]["goals_sofridos"] += team.goals_sofridos
                json[i]["goaldif"] += (team.goals - team.goals_sofridos)
     

    # atualiza a lista de jogadores no arquivo JSON com os gols marcados na partida
    contador_time = 0
    for t in match:
        # print('-----')
        for j in match[contador_time].players:
            # print(j)
            for i in json[t.name]["jogadores"]:
                if i['nome'] == j.nome:
                    # print(i)
                    # print(j["nome"])
                    i["gols"] = j.gols
                    # i["gols"] = 0
        contador_time +=1

    #declaring winner, loser or a draw
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
    total_possession = team_0_ball_possession + team_1_ball_possession
    team_0_percentage = (team_0_ball_possession / total_possession) * 100
    team_1_percentage = (team_1_ball_possession / total_possession) * 100

    if quick_game == True:
        #imprime a porcentagem de posse de bola de cada time
        print("Posse de bola para {}: {}%".format(match[0].name, round(team_0_percentage)))
        print("Posse de bola para {}: {}%".format(match[1].name, round(team_1_percentage)))
        
        #imprime os chutes
        print('Total de chutes {}: {}({})(ao gol)'.format(match[0].name, match[0].chutes, match[0].chutes_gol))
        print('Total de chutes {}: {}({})(ao gol)'.format(match[1].name, match[1].chutes, match[1].chutes_gol))
    
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
