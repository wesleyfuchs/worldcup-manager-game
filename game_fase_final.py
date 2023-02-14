import random
import time
import json

from rich.console import Console
from rich.table import Table

class Team:
    def __init__(self, key, name, score, penalti_goals, goaldif, goals, goals_sofridos, won, drawn, lost, attack, defense, luck, speed, stamina): 
        self.key = key
        self.name = name
        self.score = score
        self.penalti_goals = penalti_goals
        self.goaldif = goaldif
        self.goals = goals
        self.goals_sofridos = goals_sofridos
        self.won = won
        self.drawn = drawn
        self.lost = lost
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.speed = speed
        self.stamina = stamina
        self.red = False
        self.ball_possession = False

    def update_possession(self, possession):
        self.possession = possession

team1 = Team('Team1', 1, 0, 0, 0, 0, 0, 0, 0, 0, 60, 60, 60, 60, 60)
team2 = Team('Team2', 2, 0, 0, 0, 0, 0, 0, 0, 0, 60, 60, 60, 60, 60)

match = [team1, team2]

def cobrança_penalty(match):
    for i in match:
        nVar_penalti = random.randint(0,4)
        if nVar_penalti > 1:
            i.penalti_goals += 1
            print(str(i.name) + ' ' + "Penalty Convertido! ✅")
        else:
            print(str(i.name) + ' ' + "Penalty Perdido!    ❌")
        time.sleep(0.5)


def goal(team):
    print("Goool! " + str(team.name) + " marcou! ⚽")
    team.goals += 1


def quickgoal(team):
    team.goals += 1


#Quando um cartão amarelo é aplicado é reduzido 10 de cada stat
yelnum = 10
def yellow(team):
    print("Cartão Amarelo para " + str(team.name) + ' 🟡')
    team.attack -= yelnum
    team.defense -= yelnum
    team.luck -= yelnum
    team.speed -= yelnum
    team.stamina -= yelnum
    

#Quando um cartão vermelhor é aplicado é reduzido 50 de cada stat
rednum = 50
def red(team):
    if team.red == False:
        print("Cartão Vermelho para" + str(team.name) + ' 🔴')
        team.red = True
        team.attack -= rednum
        team.defense -= rednum
        team.luck -= rednum
        team.speed -= rednum
        team.stamina -= rednum
    else:
        pass


#Quando um cartão vermelhor é aplicado é reduzido 50 de cada stat
def quickred(team):
    if team.red == False:
        team.red = True
        team.attack -= rednum
        team.defense -= rednum
        team.luck -= rednum
        team.speed -= rednum
        team.stamina -= rednum
    else:
        pass

def quickyellow(team):
    team.attack -= yelnum
    team.defense -= yelnum
    team.luck -= yelnum
    team.speed -= yelnum
    team.stamina -= yelnum


def quickcobrança_penalty(match):
    for i in match:
        nVar_penalti = random.randint(0,4)
        if nVar_penalti > 1:
            i.penalti_goals += 1

def matchday_fase_final(match, json):
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
    #Jogo de 120 min 
    for i in range(0, 121):
        if i < 46:
            secondhalf = False
        elif i == 46:
            print('Intervalo! ⏱️')
            secondhalf = True
        elif i == 91:
            print('Fim do Tempo Regulamentar! ⏱️')
            if match[0].goals > match[1].goals or match[0].goals < match[1].goals: 
                break
            else:
                print('Prorrogação!!')
        elif i == 106:
              print('Intervalo! ⏱️')
        else:
            secondhalf = True
            
        #picks a random number 1-300 for each game minute to determine what event happens
        n1 = random.randint(1, 300)
        #picks a random team for event to happen to
        n2 = random.randint(0,1)
        
        # Calculo speed stamina
        team1.speed_factor = match[0].speed * 0.01
        team2.speed_factor = match[1].speed * 0.01

        team1.stamina_factor = match[0].stamina * 0.01
        team2.stamina_factor = match[1].stamina * 0.01
        
        #Posse de bola
        ball_possession_change = random.randint(0,400)
        if ball_possession_change > 100:
            if match[0].ball_possession:
                # calculates the chance of team1 maintaining ball possession
                chance_of_keeping_possession = (team1.speed_factor + team1.stamina_factor) * 100
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
                chance_of_keeping_possession = (team2.speed_factor + team2.stamina_factor) * 100
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
        if n1 < 284:
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
                    # quickgoal_sofrido(varlteam)
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
                        # quickgoal_sofrido(match[1])
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
                        # quickgoal_sofrido(match[0])
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
            cobrança_penalty(match)
            #Print
            print(str(match[0].penalti_goals) + '-' + str(match[1].penalti_goals))
            #contador
            cobrancas_de_penalty -= 1   
            time.sleep(0.5)
        else:
            print('-Cobraças Alternadas-')

    #Caso empate apos 5 cobranças
    if cobrancas_de_penalty == 0:     
        if match[0].penalti_goals == match[1].penalti_goals:
            while match[0].penalti_goals == match[1].penalti_goals:
                cobrança_penalty(match)
    else:
        print("----------")
                
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

    # #imprime a porcentagem de posse de bola de cada time
    # print("Posse de bola para {}: {}%".format(match[0].name, round(team_0_percentage)))
    # print("Posse de bola para {}: {}%".format(match[1].name, round(team_1_percentage)))
    
    # #imprime os chutes
    # print('Total de chutes {}: {}({})(ao gol)'.format(match[0].name, team_0_chutes, team_0_chutes_gol))
    # print('Total de chutes {}: {}({})(ao gol)'.format(match[1].name, team_1_chutes, team_1_chutes_gol))
    
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

    return json
    
def quickmatchday_fase_final(match, json):
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
    #Jogo de 120 min 
    for i in range(0, 121):
        if i < 46:
            secondhalf = False
        elif i == 46:
            secondhalf = True
        elif i == 91:
            if match[0].goals > match[1].goals or match[0].goals < match[1].goals: 
                break
            else:
                pass
        elif i == 106:
              pass
        else:
            secondhalf = True
            
        #picks a random number 1-300 for each game minute to determine what event happens
        n1 = random.randint(1, 300)
        #picks a random team for event to happen to
        n2 = random.randint(0,1)
        
        # Calculo speed stamina
        team1.speed_factor = match[0].speed * 0.01
        team2.speed_factor = match[1].speed * 0.01

        team1.stamina_factor = match[0].stamina * 0.01
        team2.stamina_factor = match[1].stamina * 0.01
        
        #Posse de bola
        ball_possession_change = random.randint(0,400)
        if ball_possession_change > 100:
            if match[0].ball_possession:
                # calculates the chance of team1 maintaining ball possession
                chance_of_keeping_possession = (team1.speed_factor + team1.stamina_factor) * 100
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
                chance_of_keeping_possession = (team2.speed_factor + team2.stamina_factor) * 100
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
        if n1 < 284:
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
                    # quickgoal_sofrido(varlteam)
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
                        # quickgoal_sofrido(match[1])
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
                        # quickgoal_sofrido(match[0])
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
            quickcobrança_penalty(match)
            #contador
            cobrancas_de_penalty -= 1   
        else:
            pass

    #Caso empate apos 5 cobranças
    if cobrancas_de_penalty == 0:     
        if match[0].penalti_goals == match[1].penalti_goals:
            while match[0].penalti_goals == match[1].penalti_goals:
                quickcobrança_penalty(match)
    else:
        pass
                
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

    # #imprime a porcentagem de posse de bola de cada time
    # print("Posse de bola para {}: {}%".format(match[0].name, round(team_0_percentage)))
    # print("Posse de bola para {}: {}%".format(match[1].name, round(team_1_percentage)))
    
    # #imprime os chutes
    # print('Total de chutes {}: {}({})(ao gol)'.format(match[0].name, team_0_chutes, team_0_chutes_gol))
    # print('Total de chutes {}: {}({})(ao gol)'.format(match[1].name, team_1_chutes, team_1_chutes_gol))
    
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
    