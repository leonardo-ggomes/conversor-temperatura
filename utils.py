import os
import sys

def get_file_path(nome_arquivo):
    if getattr(sys, 'frozen', False):  # Verifica se está rodando como .exe
        caminho_base = sys._MEIPASS
    else:
        caminho_base = os.path.dirname(__file__)  # Modo normal (script Python)

    return os.path.join(caminho_base, nome_arquivo)