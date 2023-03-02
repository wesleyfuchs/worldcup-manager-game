# if match[0].ball_possession == True:
        #     team_0_ball_possession += 1
        #     # Verifique qual jogador está com a bola
        #     for jogador in match[0].jogadores:
        #         if jogador.posse_de_bola == True:
        #             jogador_com_bola = jogador

        #     # Execute as instruções para o jogador com a bola
        #     if jogador_com_bola:
        #         # Nao acontece nada
        #         if n1 < 100:
        #             event = " "
        #             jogador_com_bola.decisao_posse_de_bola()
        #         # Disputa de bola
        #         elif n1 < 260:
        #             if ball_possession_change < jogador_com_bola.stamina:
        #                 pass
        #             else:
        #                 match[0].ball_possession = False
        #                 match[1].ball_possession = True
        #                 match[1].jogadores[0].posse_de_bola = True
        #         # passar a bola
        #         elif n1 < 280:
        #             jogador_destino = match[0].jogadores[(match[0].jogadores.index(jogador_com_bola) + 1) % len(match[0].jogadores)]
        #             jogador_com_bola.passar_bola(jogador_destino)
        #         # Driblar
        #         elif n1 < 285:
        #             jogador_com_bola.drible()
        #         # Chute
        #         else:
        #             jogador_com_bola.chute()
        
        # # Time 2 com a bola
        # else:
        #     team_1_ball_possession += 1
        #     # Verifique qual jogador está com a bola
        #     for jogador in match[1].jogadores:
        #         if jogador.posse_de_bola == True:
        #             jogador_com_bola = jogador
        #     # Execute as instruções para o jogador com a bola
        #     if jogador_com_bola:
        #         # Nao acontece nada
        #         if n1 < 100:
        #             event = " "
        #             jogador_com_bola.decisao_posse_de_bola()
        #         # Disputa de bola
        #         elif n1 < 260:
        #             if ball_possession_change < jogador_com_bola.stamina:
        #                 pass
        #             else:
        #                 match[1].ball_possession = False
        #                 match[0].ball_possession = True
        #                 match[0].jogadores[0].posse_de_bola = True
        #         # passar a bola
        #         elif n1 < 280:
        #             jogador_destino = match[1].jogadores[(match[1].jogadores.index(jogador_com_bola) + 1) % len(match[1].jogadores)]
        #             jogador_com_bola.passar_bola(jogador_destino)
        #         # Driblar
        #         elif n1 < 285:
        #             jogador_com_bola.drible()
        #         # Chute
        #         else:
        #             jogador_com_bola.chute()
        
        
        
        
        
        #################################################
        
        # Execute as instruções para o jogador com a bola
        # if jogador_com_bola:
        #     # Nao acontece nada
        #     if n1 < 50:
        #         event = " "
        #         jogador_com_bola.decisao_posse_de_bola()
        #     # Disputa de bola
        #     elif n1 < 150:
        #         # Chance de troca da posse de bola
        #         ball_possession_change = random.randint(0,150)
        #         if ball_possession_change < jogador_com_bola.stamina:
        #             pass
        #         else:
        #             current_team.ball_possession = False
        #             # other_team = match[1] if current_team == match[0] else match[0]
        #             other_team.ball_possession = True
        #             other_team.jogadores[0].posse_de_bola = True
        #     # passar a bola
        #     elif n1 < 240:
        #         jogador_destino = current_team.jogadores[random.randint(0,10)]
        #         # jogador_destino = current_team.jogadores[(current_team.jogadores.index(jogador_com_bola) + 1) % len(current_team.jogadores)]
        #         jogador_com_bola.passar_bola(jogador_destino)
        #     # Driblar
        #     elif n1 < 250:
        #         jogador_com_bola.drible()
        #     # Chute
        #     elif n1 < 290:
        #         jogador_com_bola.chute()
        #         current_team.chutes+=1
        #         n4_1 = random.randint(1,100)
        #         n4_2 = random.randint(1,100) 
        #         if n4_1 > n4_2:
        #             n5_1 = random.randint(1,100)
        #             n5_2 = random.randint(1,100)
        #             current_team.chutes_gol+=1
        #             # other_team = match[1] if current_team == match[0] else match[0] 
        #             if (jogador_com_bola.finalizacao + n5_1) > (other_team.jogadores[0].defense + n5_2):
        #                 goal(current_team, jogador_com_bola)
        #                 quickgoal_sofrido(other_team)
        #                 current_team.ball_possession = False
        #                 other_team.ball_possession = True
        #                 other_team.jogadores[0].posse_de_bola = True
        #             else:
        #                 current_team.ball_possession = False
        #                 other_team.ball_possession = True
        #                 other_team.jogadores[0].posse_de_bola = True
        #         else:
        #             current_team.ball_possession = False
        #             other_team.ball_possession = True
        #             other_team.jogadores[0].posse_de_bola = True
        #     # Cartao Amarelo
        #     else:
        #         jogador_faltoso = other_team.jogadores[random.randint(0,10)]
        #         if jogador_faltoso.cartao_amarelo == False:
        #             yellow(jogador_faltoso)
        #         else:
        #             red(jogador_faltoso)
                
                
        
        
         
        #Posse de bola
        # ball_possession_change = random.randint(0,100)
        # if ball_possession_change > 50:
        #     if match[0].ball_possession:
        #         # calculates the chance of team1 maintaining ball possession
        #         chance_of_keeping_possession = match[0].stamina
        #         print('Chance da França manter posse:{} vs {}'.format(chance_of_keeping_possession, ball_possession_change))
        #         if ball_possession_change < chance_of_keeping_possession:
        #             match[0].ball_possession = True
        #             match[1].ball_possession = False
        #             team_0_ball_possession += 1
        #         else:
        #             match[0].ball_possession = False
        #             match[1].ball_possession = True
        #             team_1_ball_possession += 1
        #     else:
        #         # calculates the chance of team2 maintaining ball possession
        #         chance_of_keeping_possession = match[1].stamina
        #         print('Chance da Argentina manter posse:{} vs {}'.format(chance_of_keeping_possession, ball_possession_change))
        #         if ball_possession_change < chance_of_keeping_possession:
        #             match[0].ball_possession = False
        #             match[1].ball_possession = True
        #             team_1_ball_possession += 1
        #         else:
        #             match[0].ball_possession = True
        #             match[1].ball_possession = False
        #             team_0_ball_possession += 1
        
        # #VAR
        # elif n1 < 273:
        #     print("VAR: Checando Possivel Penalty! 📺")
        #     time.sleep(1)
        #     #compares the random VAR number for each team plus their luck stat to determine who gets the penalty
        #     nVar = random.randint(0,10)
        #     # nVar_1 = random.randint(1,100)
        #     # nVar_2 = random.randint(1,100)
        #     # if (match[0].luck + nVar_1) > (match[1].luck + nVar_2):
        #     if match[0].ball_possession == True:
        #         varteam = match[0]
        #         varlteam = match[1]
        #     else:
        #         varteam = match[1]
        #         varlteam = match[0]
        #     #70% chance for a penalty to be given
        #     if nVar > 3:
        #         print("Penalty para " + str(varteam.name) + "!")
        #         #75% chance to get a goal from penalty
        #         nVar_3 = random.randint(0,4)
        #         if nVar_3 > 1:
        #             goal(varteam)
        #             quickgoal_sofrido(varlteam)
        #         else:
        #             print("Penalty Perdido! ❌")
        #     else:
        #         print("Penalty não marcado! ❌")
        
        
        
def matchday(match, json):
    match[0].ball_possession = False
    match[1].ball_possession = False
    # Define a equipe com a posse de bola no início do jogo
    ball_possession_start = random.randint(1,100)
    if ball_possession_start > 50:
        match[0].ball_possession = True
    else:
        match[1].ball_possession = True
        
    #contadores para armazenar a quantidade de vezes que cada time teve posse de bola
    team_0_ball_possession = 0
    team_1_ball_possession = 0
    #contadores para armazenar a quantidade de chutes
    team_0_chutes = 0
    team_1_chutes = 0
    #contadores para armazenar a quantidade de chutes a gol
    team_0_chutes_gol = 0
    team_1_chutes_gol = 0
    #plays a game for 90 mins
    for i in range(0, 91):
        if i < 46:
            secondhalf = False
        elif i == 46:
            print('Intervalo! ⏱️')
            secondhalf = True
        else:
            secondhalf = True
                 
        #picks a random number 1-300 for each game minute to determine what event happens
        n1 = random.randint(1, 300)
        #picks a random team for event to happen to
        n2 = random.randint(0,1)
        
            
        #Posse de bola
        ball_possession_change = random.randint(0,100)
        if ball_possession_change > 50:
            if match[0].ball_possession:
                # calculates the chance of team1 maintaining ball possession
                chance_of_keeping_possession = match[0].stamina
                if ball_possession_change < chance_of_keeping_possession:
                    match[0].ball_possession = True
                    match[1].ball_possession = False
                    team_0_ball_possession += 1
                else:
                    match[0].ball_possession = False
                    match[1].ball_possession = True
                    team_1_ball_possession += 1
            else:
                # calculates the chance of team2 maintaining ball possession
                chance_of_keeping_possession = match[1].stamina
                if ball_possession_change < chance_of_keeping_possession:
                    match[0].ball_possession = False
                    match[1].ball_possession = True
                    team_1_ball_possession += 1
                else:
                    match[0].ball_possession = True
                    match[1].ball_possession = False
                    team_0_ball_possession += 1
        
        event = ""
        #nothing happening
        if n1 < 270:
            event = " "
        #VAR
        elif n1 < 273:
            print("VAR: Checando Possivel Penalty! 📺")
            time.sleep(1)
            nVar = random.randint(0,10)
            if match[0].ball_possession == True:
                varteam = match[0]
                varlteam = match[1]
            else:
                varteam = match[1]
                varlteam = match[0]
            #70% chance for a penalty to be given
            if nVar > 3:
                print("Penalty para " + str(varteam.name) + "!")
                #75% chance to get a goal from penalty
                nVar_3 = random.randint(0,4)
                if nVar_3 > 1:
                    goal(varteam)
                    quickgoal_sofrido(varlteam)
                else:
                    print("Penalty Perdido! ❌")
            else:
                print("Penalty não marcado! ❌")
        #Chute a gol
        elif n1 < 295:
            if match[0].ball_possession == True:
                team_0_chutes +=1
                n4_1 = random.randint(1,100)
                n4_2 = random.randint(1,100)
                if (match[0].luck + n4_1) > (match[1].luck + n4_2):
                    team_0_chutes_gol +=1
                    n4_1 = random.randint(1,100)
                    n4_2 = random.randint(1,100)
                    if (match[0].attack + n4_1) > (match[1].defense + n4_2):
                        goal(match[0])
                        quickgoal_sofrido(match[1])
                    else:
                        pass
                else:
                    pass    
            else:
                team_1_chutes +=1
                n4_1 = random.randint(1,100)
                n4_2 = random.randint(1,100) 
                if (match[1].luck + n4_1) > (match[0].luck + n4_2):
                    team_1_chutes_gol+=1
                    n4_1 = random.randint(1,100)
                    n4_2 = random.randint(1,100)  
                    if (match[1].attack + n4_1) > (match[0].defense + n4_2):
                        goal(match[1])
                        quickgoal_sofrido(match[0])
                    else:
                        pass
                else:
                    pass 
        #yellow card
        elif n1 < 299:
            yellow(match[n2])
        #red card 
        else:
            red(match[n2])
        
        time.sleep(0.15)
        print(str(i) + """' """ + event)
        
    #adds goals for each of the teams at the end
    for team in match:
        for i in json:
            if i == team.name:
                json[i]["goals"] += team.goals 
                json[i]["goals_sofridos"] += team.goals_sofridos
                json[i]["goaldif"] += (team.goals - team.goals_sofridos)
        
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

    # #imprime a porcentagem de posse de bola de cada time
    # print("Posse de bola para {}: {}%".format(match[0].name, round(team_0_percentage)))
    # print("Posse de bola para {}: {}%".format(match[1].name, round(team_1_percentage)))
    
    # #imprime os chutes
    # print('Total de chutes {}: {}({})(ao gol)'.format(match[0].name, team_0_chutes, team_0_chutes_gol))
    # print('Total de chutes {}: {}({})(ao gol)'.format(match[1].name, team_1_chutes, team_1_chutes_gol))
      
    table = Table(show_header=False)
    table.add_column(justify="right", width=10)
    table.add_column(justify="right", width=2)
    table.add_column(justify="left", width=2)
    table.add_column(justify="left", width=10)
    
    console = Console()

    table.add_row(str(match[0].name), str(match[0].goals), str(match[1].goals), str(match[1].name))   
    console.print(table)
      
    # return print(str(match[0].name) + ' ' + str(match[0].goals) + '-' + str(match[1].goals) + ' ' + str(match[1].name))
    return json  

def quickmatchday(match, json):
    match[0].ball_possession = False
    match[1].ball_possession = False
    # Define a equipe com a posse de bola no início do jogo
    ball_possession_start = random.randint(1,100)
    if ball_possession_start > 50:
        match[0].ball_possession = True
    else:
        match[1].ball_possession = True
        
    #contadores para armazenar a quantidade de vezes que cada time teve posse de bola
    team_0_ball_possession = 0
    team_1_ball_possession = 0
    #contadores para armazenar a quantidade de chutes
    team_0_chutes = 0
    team_1_chutes = 0
    #contadores para armazenar a quantidade de chutes a gol
    team_0_chutes_gol = 0
    team_1_chutes_gol = 0
    #plays a game for 90 mins
    for i in range(0, 91):
        if i < 46:
            secondhalf = False
        elif i == 46:
            secondhalf = True
        else:
            secondhalf = True
                 
        #picks a random number 1-300 for each game minute to determine what event happens
        n1 = random.randint(1, 300)
        #picks a random team for event to happen to
        n2 = random.randint(0,1)
            
        #Posse de bola
        ball_possession_change = random.randint(0,100)
        if ball_possession_change > 50:
            if match[0].ball_possession:
                # calculates the chance of team1 maintaining ball possession
                chance_of_keeping_possession = match[0].stamina
                if ball_possession_change < chance_of_keeping_possession:
                    match[0].ball_possession = True
                    match[1].ball_possession = False
                    team_0_ball_possession += 1
                else:
                    match[0].ball_possession = False
                    match[1].ball_possession = True
                    team_1_ball_possession += 1
            else:
                # calculates the chance of team2 maintaining ball possession
                chance_of_keeping_possession = match[1].stamina
                if ball_possession_change < chance_of_keeping_possession:
                    match[0].ball_possession = False
                    match[1].ball_possession = True
                    team_1_ball_possession += 1
                else:
                    match[0].ball_possession = True
                    match[1].ball_possession = False
                    team_0_ball_possession += 1
        
        event = ""
        #nothing happening
        if n1 < 270:
            event = " "
        #VAR
        elif n1 < 273:
            nVar = random.randint(0,10)
            if match[0].ball_possession == True:
                varteam = match[0]
                varlteam = match[1]
            else:
                varteam = match[1]
                varlteam = match[0]
            #70% chance for a penalty to be given
            if nVar > 3:
                #75% chance to get a goal from penalty
                nVar_3 = random.randint(0,4)
                if nVar_3 > 1:
                    quickgoal(varteam)
                    quickgoal_sofrido(varlteam)
                else:
                    pass
            else:
                pass
        #Chute a gol
        elif n1 < 295:
            if match[0].ball_possession == True:
                team_0_chutes +=1
                n4_1 = random.randint(1,100)
                n4_2 = random.randint(1,100)
                if (match[0].luck + n4_1) > (match[1].luck + n4_2):
                    team_0_chutes_gol +=1
                    n4_1 = random.randint(1,100)
                    n4_2 = random.randint(1,100)
                    if (match[0].attack + n4_1) > (match[1].defense + n4_2):
                        quickgoal(match[0])
                        quickgoal_sofrido(match[1])
                    else:
                        pass
                else:
                    pass    
            else:
                team_1_chutes +=1
                n4_1 = random.randint(1,100)
                n4_2 = random.randint(1,100) 
                if (match[1].luck + n4_1) > (match[0].luck + n4_2):
                    team_1_chutes_gol+=1
                    n4_1 = random.randint(1,100)
                    n4_2 = random.randint(1,100)  
                    if (match[1].attack + n4_1) > (match[0].defense + n4_2):
                        quickgoal(match[1])
                        quickgoal_sofrido(match[0])
                    else:
                        pass
                else:
                    pass 
        #yellow card
        elif n1 < 299:
            quickyellow(match[n2])
        #red card 
        else:
            quickred(match[n2])
        
    #adds goals for each of the teams at the end
    for team in match:
        for i in json:
            if i == team.name:
                json[i]["goals"] += team.goals 
                json[i]["goals_sofridos"] += team.goals_sofridos
                json[i]["goaldif"] += (team.goals - team.goals_sofridos)
        
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

    # #imprime a porcentagem de posse de bola de cada time
    # print("Posse de bola para {}: {}%".format(match[0].name, round(team_0_percentage)))
    # print("Posse de bola para {}: {}%".format(match[1].name, round(team_1_percentage)))
    
    # #imprime os chutes
    # print('Total de chutes {}: {}({})(ao gol)'.format(match[0].name, team_0_chutes, team_0_chutes_gol))
    # print('Total de chutes {}: {}({})(ao gol)'.format(match[1].name, team_1_chutes, team_1_chutes_gol))
      
    table = Table(show_header=False)
    table.add_column(justify="right", width=10)
    table.add_column(justify="right", width=2)
    table.add_column(justify="left", width=2)
    table.add_column(justify="left", width=10)
    
    console = Console()

    table.add_row(str(match[0].name), str(match[0].goals), str(match[1].goals), str(match[1].name))   
    console.print(table)
      
    # return print(str(match[0].name) + ' ' + str(match[0].goals) + '-' + str(match[1].goals) + ' ' + str(match[1].name))
    return json  


