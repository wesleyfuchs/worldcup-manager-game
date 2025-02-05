class Jogador:
    def __init__(self, nome, numero, gols, posicao, finalizacao, defesa, interceptacao, penalty, passe, stamina, GK_skill, ball_control, assistencias, cartoes_amarelos, cartoes_vermelhos):
        self.nome = nome
        self.numero = numero
        self.gols = gols
        self.posicao = posicao
        self.finalizacao = finalizacao
        self.defesa = defesa
        self.interceptacao = interceptacao
        self.penalty = penalty
        self.passe = passe
        self.stamina = stamina
        self.GK_skill = GK_skill
        self.ball_control = ball_control

        self.posse_de_bola = False
        self.cartoes_amarelos = cartoes_amarelos 
        self.cartoes_vermelhos = cartoes_vermelhos
        self.cartoes_amarelos_na_partida = 0
        self.cartao_vermelho = False

        self.assistencias = assistencias
        self.passes_bem_sucedidos = 0
        self.desarmes = 0
        self.assistindo = None  # Jogador que passou a bola para este jogador


    def recebeu_cartao_amarelo(self):
        self.cartoes_amarelos += 1
        self.cartoes_amarelos_na_partida +=1

    def recebeu_cartao_vermelho(self):
        self.cartoes_vermelhos += 1

    def passar_bola(self, jogador):
        # Passar a bola para outro jogador
        print(f"Jogador {self.nome} passou a bola.")
        self.posse_de_bola = False
        jogador.posse_de_bola = True
        jogador.assistindo = self  # Define quem passou a bola

    def decisao_posse_de_bola(self):
        # Instruções para o jogador com a bola
        print(f"Jogador {self.nome} está com a bola.")

    def passar_bola_quick(self, jogador):
        # Passar a bola para outro jogador sem o print
        self.posse_de_bola = False
        jogador.posse_de_bola = True
        jogador.assistindo = self  # Define quem passou a bola

    def chute(self):
        print(f"Jogador {self.nome} chutou.")
        
    def gol(self):
        self.gols += 1
