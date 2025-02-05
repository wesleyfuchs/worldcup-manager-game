import json

# Caminho do arquivo
arquivo = "data/teams_jogadores.txt"

# Carregar o JSON existente
with open(arquivo, "r", encoding="utf-8") as f:
    database = json.load(f)


# Percorre todos os times e jogadores
for team_name, team_data in database.items():
    for jogador in team_data["jogadores"]:
        if "cartoes_vermelhos_na_partida" not in jogador:
            jogador["cartoes_vermelhos_na_partida"] = 0  # Adiciona a chave caso não exista


# Salvar o JSON atualizado
with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(database, f, indent=4, ensure_ascii=False)

print("Atualização concluída! Campos adicionados para todos os jogadores.")


