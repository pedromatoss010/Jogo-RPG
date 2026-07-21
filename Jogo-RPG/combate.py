from utils import limpa
from inimigos import escolher_inimigo
from recompensas import abrir_bau

import time
import random

def combate(player):
    inimigo = escolher_inimigo(player["vitorias"])
    limpa()
    print(f"CILADA! Um {inimigo['nome']} bloqueia seu caminho!")
    time.sleep(2)
    
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
            print(f"--> Você causou {dano_jogador} de dano!")
            time.sleep(0.7)

        elif acao_combate == 2: 
            if player["pocoes"] > 0:
                player["pocoes"] -= 1
                cura = int(player["hp_max"] * 0.3)
                player["hp"] = min(player["hp_max"], player["hp"] + cura)
                print("Você recuperou energia!")
                time.sleep(0.7)
            else:
                print("Você não tem poções! Perdeu o turno!")
                time.sleep(0.7)

        elif acao_combate == 3:
            if player["bomba"] > 0:
                dano_bomba = random.randint(30, 55)
                inimigo["hp"] -= dano_bomba
                player["bomba"] -= 1
                print(f"Bomba causou {dano_bomba} de dano!")
                time.sleep(0.7)
            else:
                print("Você não tem bombas!")
                time.sleep(0.7)

        if inimigo["hp"] > 0: 
            dano_inimigo = max(0, random.randint(inimigo["dano_min"], inimigo["dano_max"]) - player["bonus_defesa"])
            player["hp"] -= dano_inimigo
            print(f"O {inimigo['nome']} causou {dano_inimigo} de dano!")
            time.sleep(0.7)

            round_atual += 1

    if player["hp"] > 0: # 
        print(f"VITÓRIA! Você derrotou o {inimigo["nome"]} em {round_atual} rounds!")
        player["ouro"] += inimigo['ouro']
        player["vitorias"] += 1
        round_atual = 0
        time.sleep(3)

        sorte = random.randint(1,2)
        if sorte == 1:
            print("Você encontrou um baú. Vamos descobrir oque tem dentro dele!")
            time.sleep(1.5)
            abrir_bau(player)
