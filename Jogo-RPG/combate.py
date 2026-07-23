# Lógica de turnos do combate: ataque, poção, bomba e dano do inimigo

from utils import limpa
from inimigos import escolher_inimigo, frase_de_encontro, frase_de_vitoria
from recompensas import abrir_bau
from cores import CIANO, VERDE, VERMELHO, RESET

import time
import random

def combate(player):
    inimigo = escolher_inimigo(player["vitorias"])
    print(frase_de_encontro(inimigo['nome']))
    time.sleep(2.6)
    limpa()
 
    round_atual = 1

    while player["hp"] > 0 and inimigo["hp"] > 0:  #
        limpa()
        print(f"--- COMBATE  COM {inimigo['nome']}---")
        print(f"Seu HP:  {player['hp']} | {inimigo['nome']}: {inimigo['hp']}")
        print(f"Round: {round_atual}")
        print("1. Atacar")
        print(f"2. Tomar Poção (Restam: {player['pocoes']})")
        print(f"3. Lançar a Bomba (restam: {player['bomba']})")
        try:
            acao_combate = int(input("Ação: "))
        except ValueError:
            acao_combate = 0
        
        if acao_combate == 1: 
            dano_jogador = random.randint(19, 26) + player["bonus_ataque"]
            inimigo["hp"] -= dano_jogador
            print(f"--> Você causou {CIANO}{dano_jogador}{RESET} de dano!")
            time.sleep(0.8)

        elif acao_combate == 2: 
            if player["pocoes"] > 0:
                player["pocoes"] -= 1
                cura = int(player["hp_max"] * 0.3)
                player["hp"] = min(player["hp_max"], player["hp"] + cura)
                print(f"{VERDE}Você recuperou energia!{RESET}")
                time.sleep(0.7)
            else:
                print(f"Você não tem poções! {VERMELHO}Perdeu o turno!{RESET}")
                time.sleep(0.7)

        elif acao_combate == 3:
            if player["bomba"] > 0:
                dano_bomba = random.randint(30, 55)
                inimigo["hp"] -= dano_bomba
                player["bomba"] -= 1
                print(f"Bomba causou {VERMELHO}{dano_bomba}{RESET} de dano!")
                time.sleep(0.7)
            else:
                print(f"Você não tem bombas! {VERMELHO} Perdeu o turno!{RESET}")
                time.sleep(0.7)

        if inimigo["hp"] > 0: 
            dano_inimigo = max(0, random.randint(inimigo["dano_min"], inimigo["dano_max"]) - player["bonus_defesa"])
            player["hp"] -= dano_inimigo
            print(f"--> {inimigo['nome']} causou {VERMELHO}{dano_inimigo}{RESET} de dano!")
            time.sleep(0.8)

            round_atual += 1

    if player["hp"] > 0: # 
        print(frase_de_vitoria(inimigo['nome'], round_atual))
        player["ouro"] += inimigo['ouro']
        player["vitorias"] += 1
        round_atual = 0
        time.sleep(3)

        sorte = random.randint(1,2)
        if sorte == 1:
            print("Você encontrou um baú. Vamos descobrir oque tem dentro dele!")
            time.sleep(1.5)
            abrir_bau(player)
    if inimigo["id"] == "mago_sombrio":
        return True
    return False
