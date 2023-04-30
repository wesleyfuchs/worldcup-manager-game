from rich.console import Console
from rich.table import Table
from rich import inspect


def criar_tabela(data, leaguecolor, teamcolor, userteam, gameweek):
    '''Cria a tabela da fase de grupos'''
    
    table = Table(show_header=True, header_style=leaguecolor)
    table.add_column(" ", style="dim", width=1)
    table.add_column("Equipe", width=15)
    table.add_column("Pts", justify="right", style="bold", width=4)
    table.add_column("PJ", justify="right", width=4)
    table.add_column("VIT", justify="right", width=4)
    table.add_column("E", justify="right", width=4)
    table.add_column("DER", justify="right", width=4)
    table.add_column("GM", justify="right", width=4)
    table.add_column("GC", justify="right", width=4)
    table.add_column("SG", justify="right", width=4)
    
    
    console = Console()
    dicc = {}

    # for team in data:
    #     dicc[data[team]['name']] = data[team]["score"]

    # sorteddicc = sorted(dicc, key=dicc.get, reverse=True)
    
    for team in data:
        dicc[data[team]['name']] = (data[team]["score"], data[team]["goaldif"])

    sorteddicc = sorted(dicc, key=lambda x: (-dicc[x][0], -dicc[x][1]))
    
    position = 0
    for team in sorteddicc:
        
        #Colocar cor no time escolhido
        position += 1
        if team == userteam:
            table.add_row(str(position), str(data[team]["name"]), str(data[team]["score"]), str(gameweek), str(data[team]["won"]), str(data[team]["drawn"]), str(data[team]["lost"]), str(data[team]["goals"]), str(data[team]["goals_sofridos"]), str(data[team]["goaldif"]),  style=teamcolor)
        else:    
            table.add_row(str(position), str(data[team]["name"]), str(data[team]["score"]), str(gameweek), str(data[team]["won"]), str(data[team]["drawn"]), str(data[team]["lost"]), str(data[team]["goals"]), str(data[team]["goals_sofridos"]), str(data[team]["goaldif"]))
        
    console.print(table)

    
    