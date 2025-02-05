import json

# Caminho do arquivo
arquivo = "data/teams_jogadores.txt"

# Carregar o JSON existente
with open(arquivo, "r", encoding="utf-8") as f:
    database = json.load(f)

# Percorre todos os times e jogadores para adicionar os novos campos
for team_name, team_data in database.items():
    for jogador in team_data["jogadores"]:
        if "cartoes_amarelos" not in jogador:
            jogador["cartoes_amarelos"] = 0
        if "cartoes_vermelhos" not in jogador:
            jogador["cartoes_vermelhos"] = 0
        if "suspenso" not in jogador:
            jogador["suspenso"] = False

# Salvar o JSON atualizado
with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(database, f, indent=4, ensure_ascii=False)

print("Atualização concluída! Campos adicionados para todos os jogadores.")
