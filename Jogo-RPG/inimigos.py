import random
import copy

INIMIGOS = {
    "esqueleto": {"nome": "Esqueleto", "hp": 130, "dano_min": 17, "dano_max": 22, "ouro": 40, "vitorias_min": 0},
    "rato": {"nome": "Rato Gigante", "hp": 60, "dano_min": 8, "dano_max": 14, "ouro": 20, "vitorias_min": 0},
    "zumbi": {"nome": "Zumbi", "hp": 160, "dano_min": 15, "dano_max": 20, "ouro": 45, "vitorias_min": 1},
    "aranha": {"nome": "Aranha", "hp": 100, "dano_min": 12, "dano_max": 18, "ouro": 35, "vitorias_min": 1},
    "cavaleiro": {"nome": "Cavaleiro Sombrio", "hp": 220, "dano_min": 22, "dano_max": 28, "ouro": 70, "vitorias_min": 3},
    "fantasma": {"nome": "Fantasma", "hp": 90, "dano_min": 20, "dano_max": 30, "ouro": 50, "vitorias_min": 3},
    "troll": {"nome": "Troll", "hp": 300, "dano_min": 25, "dano_max": 32, "ouro": 90, "vitorias_min": 5},
    "bruxa": {"nome": "Bruxa", "hp": 150, "dano_min": 18, "dano_max": 24, "ouro": 60, "vitorias_min": 5},
    "golem": {"nome": "Golem", "hp": 350, "dano_min": 20, "dano_max": 26, "ouro": 100, "vitorias_min": 7},
    "mago_sombrio": {"nome": "Mago Sombrio", "hp": 500, "dano_min": 30, "dano_max": 40, "ouro": 300, "vitorias_min": 10},
}

def escolher_inimigo(vitorias):
    candidatos = [i for i in INIMIGOS.values() if i["vitorias_min"] <= vitorias]
    return copy.deepcopy(random.choice(candidatos)) 