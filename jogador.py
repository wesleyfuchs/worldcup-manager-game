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
        
       