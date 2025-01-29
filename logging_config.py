import logging

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,  # Alterar para INFO ou WARNING em produção
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("game.log"),  # Salvar logs em arquivo
            logging.StreamHandler()          # Mostrar logs no console
        ]
    )
