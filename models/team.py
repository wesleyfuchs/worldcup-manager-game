
class Team:
    def __init__(self, key, name, score, penalti_goals, goaldif, goals, goals_sofridos, won, drawn, lost, jogadores, suspensos):
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
        self.jogadores = jogadores
        self.players = []
        self.reservas = []
        self.suspensos = suspensos
        self.ball_possession = False
        
    def adicionar_jogador(self, jogador):
        self.players.append(jogador)
        
    def adicionar_reservas(self, jogador):
        self.reservas.append(jogador)
