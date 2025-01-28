class Jogador:
    def __init__(self, nome, numero, gols, posicao, finalizacao, defesa, interceptacao, penalty, passe, stamina, GK_skill, ball_control, assistencias):
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
        self.cartao_amarelo = False
        self.cartao_vermelho = False

        # Novos atributos
        self.assistencias = assistencias
        self.passes_bem_sucedidos = 0
        self.desarmes = 0
        self.assistindo = None  # Jogador que passou a bola para este jogador

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
