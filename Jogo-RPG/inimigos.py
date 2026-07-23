# Dados de todos os inimigos e sorteio de qual aparece, com base nas vitórias

import random
import copy
from cores import VERDE, RESET

INIMIGOS = {
    "esqueleto": {"id": "esqueleto", "nome": "o Esqueleto", "hp": 130, "dano_min": 17, "dano_max": 22, "ouro": 40, "vitorias_min": 0},
    "rato": {"id": "rato", "nome": "o Rato Gigante", "hp": 60, "dano_min": 8, "dano_max": 14, "ouro": 20, "vitorias_min": 0},
    "zumbi": {"id": "zumbi", "nome": "o Zumbi", "hp": 160, "dano_min": 15, "dano_max": 20, "ouro": 45, "vitorias_min": 1},
    "aranha": {"id": "aranha", "nome": "a Aranha", "hp": 100, "dano_min": 12, "dano_max": 18, "ouro": 35, "vitorias_min": 1},
    "cavaleiro": {"id": "cavaleiro", "nome": "o Cavaleiro Sombrio", "hp": 220, "dano_min": 22, "dano_max": 28, "ouro": 70, "vitorias_min": 3},
    "fantasma": {"id": "fantasma", "nome": "o Fantasma", "hp": 90, "dano_min": 20, "dano_max": 30, "ouro": 50, "vitorias_min": 3},
    "troll": {"id": "troll", "nome": "o Troll", "hp": 300, "dano_min": 25, "dano_max": 32, "ouro": 90, "vitorias_min": 5},
    "bruxa": {"id": "bruxa", "nome": "a Bruxa", "hp": 150, "dano_min": 18, "dano_max": 24, "ouro": 60, "vitorias_min": 5},
    "golem": {"id": "golem", "nome": "o Golem", "hp": 350, "dano_min": 20, "dano_max": 26, "ouro": 100, "vitorias_min": 7},
    "mago_sombrio": {"id": "mago_sombrio", "nome": "o Mago Sombrio", "hp": 500, "dano_min": 30, "dano_max": 40, "ouro": 300, "vitorias_min": 10},
}
def escolher_inimigo(vitorias):
    candidatos = [i for i in INIMIGOS.values() if i["vitorias_min"] <= vitorias]
    return copy.deepcopy(random.choice(candidatos)) 
    # deepcopy evita alterar o HP original do inimigo no dicionário INIMIGOS.
    # Sem isso, o dano tomado numa luta "vazava" pro próximo combate com o mesmo inimigo.


frases_encontro = [
    "CILADA! {inimigo} bloqueia seu caminho!",
    "{inimigo} surge das sombras, pronto para atacar!",
    "Você sente uma presença hostil... {inimigo} aparece!",
    "Passos pesados ecoam... {inimigo} vem em sua direção!",
    "Sem aviso, {inimigo} salta na sua frente!"
]

def frase_de_encontro(inimigo):
    frase = random.choice(frases_encontro)
    return frase.format(inimigo=inimigo)

frases_vitoria = [
    VERDE + "VITÓRIA!" + RESET + " Você derrotou {inimigo} em {rounds} rounds!",
    "{inimigo} cai derrotado! " + VERDE + "Vitória" + RESET + " conquistada em {rounds} rounds!",
    "Com um golpe final, você venceu {inimigo}! ({rounds} rounds)",
    "{inimigo} não teve chances! " + VERDE + "Vitória" + RESET + " em {rounds} rounds!",
]

def frase_de_vitoria(inimigo, round):
    frase = random.choice(frases_vitoria)
    return frase.format(inimigo=inimigo, rounds=round)