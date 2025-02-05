import logging

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("game.log", encoding="utf-8"),  # Configuração para Unicode
            logging.StreamHandler()  # Exibe os logs no console
        ]
    )
