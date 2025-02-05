import json

def load_data(filepath: str) -> dict:
    """Carrega os dados do arquivo JSON."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Arquivo {filepath} não encontrado.")
        return {}

def save_data(filepath: str, data: dict) -> None:
    """Salva os dados no arquivo JSON."""
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def zerar_pontuacao(database):
    '''Zera a pontuação de cada time'''
    for team in database:
        database[team]['score'] = 0

def reset_team_stats(database):
    """Reseta as estatísticas dos times no banco de dados."""
    for team in database:
        database[team]['goaldif'] = 0
        database[team]['goals'] = 0
        database[team]['goals_sofridos'] = 0
        database[team]['won'] = 0
        database[team]['drawn'] = 0
        database[team]['lost'] = 0
        database[team]['suspensos'] = []

def reset_player_stats(database):
    """Reseta as estatísticas dos jogadores no banco de dados."""
    for team in database:
        for jogador in database[team]['jogadores']:
            jogador['gols'] = 0
            jogador['assistencias'] = 0
            jogador['cartoes_amarelos'] = 0
            jogador['cartoes_vermelhos'] = 0
            jogador['partidas_suspenso'] = 0

def ordenar_fase_final(confrontos):
    '''Ordena os times por pontuação e depois por saldo de gols'''
    selecoes_ordenado = []
    for grupos in confrontos:
        dicc = {}
        for team in grupos:
            dicc[grupos[team]['name']] = (
                grupos[team]["score"], grupos[team]["goaldif"])

        sorteddicc = sorted(dicc, key=lambda x: (-dicc[x][0], -dicc[x][1]))
        selecoes_ordenado.append(sorteddicc)
    return selecoes_ordenado


def listar_equipes(lista_de_partidas, database):
    equipes_database = []
    for confronto in lista_de_partidas:
        quartas = {k: database[k] for k in confronto}
        equipes_database.append(quartas)
    return equipes_database