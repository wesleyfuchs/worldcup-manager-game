import random
import time
import json

# opens the json file with team data
with open('data/teams_jogadores.txt') as f:
    database = json.load(f)


class Jogador:
    def __init__(self, nome, posicao, finalizacao, defesa, passe, ball_control, gols):
        self.nome = nome
        self.posicao = posicao
        self.finalizacao = finalizacao
        self.defesa = defesa
        self.passe = passe
        self.ball_control = ball_control
        self.gols = gols
        self.posse_de_bola = False
        self.cartao_amarelo = False
        self.cartao_vermelho = False

    def decisao_posse_de_bola(self):
        # Instruções para o jogador com a bola
        print(f"Jogador {self.nome} está com a bola.")

    def passar_bola(self, jogador):
        # Passar a bola para outro jogador
        print(f"Jogador {self.nome} passou a bola.")
        self.posse_de_bola = False
        jogador.posse_de_bola = True
    
    # def drible(self):
    #     print(f"Jogador {self.nome} fez um drible.")

    def passar_bola_quick(self, jogador):
        # Passar a bola para outro jogador sem o print
        self.posse_de_bola = False
        jogador.posse_de_bola = True
    
    def chute(self):
        print(f"Jogador {self.nome} chutou.")
        
    def gol(self):
        self.gols +=1
        
       
    
class Team:
    def __init__(self, key, name, score, penalti_goals, goaldif, goals, goals_sofridos, won, drawn, lost):
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
        self.jogadores = []
        self.suspensos = []
        self.ball_possession = False
        
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

# create player instances

# player1 = Jogador("Saad Al Sheeb", 'goleiro', 12, 62, 13, 20, 0)
# player2 = Jogador('Bassam Al Rawi', 'zagueiro', 38, 70, 58, 63, 0)
# player3 = Jogador('Boualem Khoukhi', 'zagueiro', 49, 68, 55, 53, 0)
# player4 = Jogador('Ismael Mohammad', 'zagueiro', 64, 63, 64, 65, 0)
# player5 = Jogador('Tarek Salman', 'zagueiro', 31, 65, 58, 58, 0)
# player6 = Jogador('Homam Ahmed', 'zagueiro', 37, 64, 64, 63, 0)
# player7 = Jogador('Hassan Al Haydos', 'meio-campo', 66, 23, 68, 74, 0)
# player8 = Jogador('Karim Boudiaf', 'meio-campo', 60, 65, 70, 72, 0)
# player9 = Jogador('Abluzaziz Hatem', 'atacante', 64, 60, 72, 68, 0)
# player10 = Jogador('Almoez Ali', 'atacante', 76, 15, 50, 65, 0)
# player11 = Jogador('Akram Afif', 'atacante', 74, 30, 74, 78, 0)

player1 = Jogador("Lloris", 'goleiro', 10, 81, 49, 29, 0)
player2 = Jogador('Koude', 'zagueiro', 47, 84, 70, 73, 0)
player3 = Jogador('Varane', 'zagueiro', 46, 84, 70, 75, 0)
player4 = Jogador('Upamecano', 'zagueiro', 39, 84, 70, 68, 0)
player5 = Jogador('Theo Hernandez', 'zagueiro', 69, 80, 79, 81, 0)
player6 = Jogador('Tchouameni', 'meio-campo', 67, 80, 78, 79, 0)
player7 = Jogador('Rabiot', 'meio-campo', 68, 76, 81, 80, 0)
player8 = Jogador('Griezmann', 'meio-campo', 82, 52, 83, 85, 0)
player9 = Jogador('Giroud', 'atacante', 86, 25, 70, 80, 0)
player10 = Jogador('Mbappe', 'atacante', 93, 33, 82, 92, 0)
player11 = Jogador('Dembele', 'atacante', 75, 31, 81, 87, 0)

player12 = Jogador('E. Martinez', 'goleiro', 16, 85, 50, 35, 0)
player13 = Jogador('Otamendi', 'zagueiro', 54, 83, 73, 66, 0)
player14 = Jogador('Molina', 'zagueiro', 67, 73, 75, 77, 0)
player15 = Jogador('Acuña', 'zagueiro', 66, 85, 86, 88, 0)
player16 = Jogador('C. Romero', 'zagueiro', 48, 86, 72, 68, 0)
player17 = Jogador('De Paul', 'meia', 76, 78, 85, 86, 0)
player18 = Jogador('Mac Allister', 'meia', 77, 52, 78, 77, 0)
player20 = Jogador('Enzo Fernandez', 'meia', 64, 74, 80, 80, 0)
player19 = Jogador('Di Maria', 'atacante', 76, 50, 83, 88, 0)
player21 = Jogador('Alvarez', 'atacante', 80, 47, 74, 83, 0)
player22 = Jogador('Messi', 'atacante', 91, 25, 91, 95, 0)


# create team instance with player instances
team1 = Team(1, "Franca", 0, 0, 0, 0, 0, 0, 0, 0)
team2 = Team(0, "Argentina", 0, 0, 0, 0, 0, 0, 0, 0)

team1.adicionar_jogador(player1)
team1.adicionar_jogador(player2)
team1.adicionar_jogador(player3)
team1.adicionar_jogador(player4)
team1.adicionar_jogador(player5)
team1.adicionar_jogador(player6)
team1.adicionar_jogador(player7)
team1.adicionar_jogador(player8)
team1.adicionar_jogador(player9)
team1.adicionar_jogador(player10)
team1.adicionar_jogador(player11)

team2.adicionar_jogador(player12)
team2.adicionar_jogador(player13)
team2.adicionar_jogador(player14)
team2.adicionar_jogador(player15)
team2.adicionar_jogador(player16)
team2.adicionar_jogador(player17)
team2.adicionar_jogador(player18)
team2.adicionar_jogador(player19)
team2.adicionar_jogador(player20)
team2.adicionar_jogador(player21)
team2.adicionar_jogador(player22)


match = [team1, team2]


def yellow(jogador):
    print("Cartão Amarelo para " + str(jogador.nome) + ' 🟡')
    jogador.cartao_amarelo = True
    

def red(jogador):
    print("Cartão Vermelho para " + str(jogador.nome) + ' 🔴')
    jogador.cartao_vermelho = True


def goal(team, jogador):
    print("Gooool! " + str(team.name) + " marcou! ⚽")
    team.goals += 1
    jogador.gol()


def quickgoal(team):
    team.goals += 1


def quickgoal_sofrido(team):
    team.goals_sofridos += 1


def matchday(match):
    # Inicializa a posse de bola
    match[0].ball_possession = False
    match[1].ball_possession = False
    jogador_com_bola = None
    ball_possession_start = random.randint(1,100)
    if ball_possession_start > 50:
        match[0].ball_possession = True
        match[0].jogadores[10].posse_de_bola = True
    else:
        match[1].ball_possession = True
        match[1].jogadores[10].posse_de_bola = True
    
    # Inicializa contadores
    team_0_ball_possession = 0
    team_1_ball_possession = 0
    match[0].chutes = 0
    match[1].chutes = 0
    match[0].chutes_gol = 0
    match[1].chutes_gol = 0
    
    #Joga um jogo por 90 mins
    for i in range(0, 91):
        if i == 46:
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
        for jogador in current_team.jogadores:
            if jogador.posse_de_bola == True:
                jogador_com_bola = jogador
                
        qnt_jogadores_current_team = (len(current_team.jogadores) - 1)
        qnt_jogadores_other_team = (len(other_team.jogadores)- 1)
        
        # Execute as instruções para o jogador com a bola
        if jogador_com_bola.posicao == 'goleiro':
            jogador_com_bola.decisao_posse_de_bola()
            jogador_destino = current_team.jogadores[random.randint(0, qnt_jogadores_current_team)]
            jogador_com_bola.passar_bola(jogador_destino)
        else:
            # Nao acontece nada
            if n1 <= 5:
                event = " "
                jogador_com_bola.decisao_posse_de_bola()
            # Disputa de bola
            elif n1 <= 25:
                # Chance de troca da posse de bola
                ball_possession_change = random.randint(0, 60)
                if ball_possession_change < 20:
                    pass
                else:
                    # calculates the chance of maintaining ball possession
                    ladrao_bola = other_team.jogadores[random.randint(0,qnt_jogadores_other_team)]
                    if jogador_com_bola.ball_control < ladrao_bola.ball_control:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        ladrao_bola.posse_de_bola = True
                    else: 
                        pass
            # Passar a bola
            elif n1 <= 65:
                # Chance de errar o passe
                    ladrao_bola = other_team.jogadores[random.randint(0,qnt_jogadores_other_team)]
                    if jogador_com_bola.passe < ladrao_bola.defesa:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        ladrao_bola.posse_de_bola = True
                    else: 
                        jogador_destino = current_team.jogadores[random.randint(0, qnt_jogadores_current_team)]
                        jogador_com_bola.passar_bola(jogador_destino)
            # Chute
            elif n1 <= 95:
                jogador_com_bola.chute()
                current_team.chutes+=1
                n4_1 = random.randint(1,100)
                n4_2 = random.randint(50,100) 
                if n4_1 > n4_2:
                    n5_1 = random.randint(1,100)
                    n5_2 = random.randint(50,100)
                    current_team.chutes_gol+=1 
                    if (jogador_com_bola.finalizacao + n5_1) > (other_team.jogadores[0].defesa + n5_2):
                        goal(current_team, jogador_com_bola)
                        quickgoal_sofrido(other_team)
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        other_team.jogadores[10].posse_de_bola = True
                    else:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        other_team.jogadores[0].posse_de_bola = True
                else:
                    current_team.ball_possession = False
                    other_team.ball_possession = True
                    other_team.jogadores[0].posse_de_bola = True
            #Falta
            elif n1 < 99:
                n2_1 = random.randint(1,10) 
                if n2_1 > 8:
                    # Cartao Amarelo
                    jogador_faltoso = other_team.jogadores[random.randint(0, qnt_jogadores_other_team)]
                    if jogador_faltoso.cartao_amarelo == False:
                        yellow(jogador_faltoso)
                    else:
                        red(jogador_faltoso)
                        for jogador in other_team.jogadores:
                            if jogador.cartao_vermelho:
                                jogador_red_index = jogador
                                jogador_red_index = other_team.jogadores.index(jogador_red_index)
                                jogador_red = other_team.jogadores.pop(jogador_red_index)
                                other_team.suspensos.append(jogador_red)
                    # Cobrança falta
                    n3_1 = random.randint(1,10)
                    if n3_1 >= 9:
                        current_team.chutes+=1
                        current_team.chutes_gol+=1 
                        goal(current_team, jogador_com_bola)
                        quickgoal_sofrido(other_team)
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        other_team.jogadores[10].posse_de_bola = True
                    else:
                        current_team.ball_possession = False
                        other_team.ball_possession = True
                        other_team.jogadores[0].posse_de_bola = True    
            else:
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
                    print("Penalty para " + str(varteam.name) + "!")
                    #75% chance to get a goal from penalty
                    nVar_3 = random.randint(0,4)
                    if nVar_3 > 1:
                        goal(varteam, jogador_com_bola)
                        quickgoal_sofrido(varlteam)
                    else:
                        print("Penalty Perdido! ❌")
                else:
                    print("Penalty não marcado! ❌")
        time.sleep(0.15)
        print(str(i) + """' """ + event)
        print(n1)
    # Depois do fim da paritda
    
    #adds goals for each of the teams at the end
    # for team in match:
    #     for i in json:
    #         if i == team.name:
    #             json[i]["goals"] += team.goals 
    #             json[i]["goals_sofridos"] += team.goals_sofridos
    #             json[i]["goaldif"] += (team.goals - team.goals_sofridos)
        
    #declaring winner, loser or a draw
    # winner = ""
    # loser = ""
    # draw = False
    # if match[0].goals > match[1].goals:
    #     winner = match[0].name
    #     loser = match[1].name
    # elif match[0].goals < match[1].goals:
    #     winner = match[1].name
    #     loser = match[0].name
    # else:
    #     draw = True

    # if draw == True:
    #     for i in json:
    #         for team in match:
    #             if i == team.name:
    #                 json[i]["drawn"] += 1
    #                 json[i]["score"] += 1
    # else:
    #     for i in json:
    #         if i == winner:
    #             json[i]["score"] += 3
    #             json[i]["won"] += 1
    #         if i == loser:
    #             json[i]["lost"] += 1
        
    #calcula a porcentagem de posse de bola de cada time
    total_possession = team_0_ball_possession + team_1_ball_possession
    team_0_percentage = (team_0_ball_possession / total_possession) * 100
    team_1_percentage = (team_1_ball_possession / total_possession) * 100

    #imprime a porcentagem de posse de bola de cada time
    print("Posse de bola para {}: {}%".format(match[0].name, round(team_0_percentage)))
    print("Posse de bola para {}: {}%".format(match[1].name, round(team_1_percentage)))
    
    #imprime os chutes
    print('Total de chutes {}: {}({})(ao gol)'.format(match[0].name, match[0].chutes, match[0].chutes_gol))
    print('Total de chutes {}: {}({})(ao gol)'.format(match[1].name, match[1].chutes, match[1].chutes_gol))
    
    for jogador in match[0].jogadores:
        if jogador.gols > 0:
            print('{} Gols de {}'.format(jogador.gols, jogador.nome))
        
    for jogador in match[1].jogadores:
        if jogador.gols > 0:
            print('{} Gols de {}'.format(jogador.gols, jogador.nome))
      
    # table = Table(show_header=False)
    # table.add_column(justify="right", width=10)
    # table.add_column(justify="right", width=2)
    # table.add_column(justify="left", width=2)
    # table.add_column(justify="left", width=10)
    
    # console = Console()

    # table.add_row(str(match[0].name), str(match[0].goals), str(match[1].goals), str(match[1].name))   
    # console.print(table)
      
    return print(str(match[0].name) + ' ' + str(match[0].goals) + '-' + str(match[1].goals) + ' ' + str(match[1].name))
    # return json  

matchday(match)

