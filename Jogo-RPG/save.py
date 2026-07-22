# Salvar, carregar e apagar o progresso do jogador em JSON

import os
import json
from player import criar_player


PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_SAVES = os.path.join(PASTA_ATUAL, "saves")
ARQUIVO_SAVE = os.path.join(PASTA_SAVES, "player.json")

def salvar_player(player):
    os.makedirs(PASTA_SAVES, exist_ok=True)
    with open(ARQUIVO_SAVE, "w", encoding="utf-8") as f:
        json.dump(player, f, ensure_ascii=False, indent=4)

def carregar_player():
    with open(ARQUIVO_SAVE, "r", encoding="utf-8") as f:
        return json.load(f)

def existe_save():
    return os.path.exists(ARQUIVO_SAVE)

def apagar_save():
    if os.path.exists(ARQUIVO_SAVE):
        os.remove(ARQUIVO_SAVE)