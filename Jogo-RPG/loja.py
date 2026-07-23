# Compra de itens/upgrades usando o ouro do jogador

import time
from utils import limpa
from cores import AMARELO, VERDE, AZUL, VERMELHO, RESET

def loja(player):
    while True:
        # Preço sobe 35 moedas a cada compra (base 90) pra evitar que o jogador
        # empilhe bônus de ataque/defesa infinitamente gastando pouco ouro
        preco_espada = 90 + (player["compras_espada"] * 35)
        preco_escudo = 90 + (player["compras_escudo"] * 35)
        limpa()
        print("------------ LOJA SOMBRIA ------------")
        print(f"Seu ouro: {AMARELO}{player['ouro']}{RESET}")
        print("---------------------------------------------")
        print(f"1. Poção de cura {AMARELO}(50 moedas){RESET}")
        print(f"2. Afiar Espada({VERDE}+5 Dano fixo {RESET}) ({AMARELO}{preco_espada} Moedas{RESET})")
        print(f"3. Comprar Escudo ({VERDE}+5 Defesa{RESET}) {AMARELO}({preco_escudo} Moedas{RESET})")
        print(f"4. Comprar Bomba ({AMARELO}100 Moedas{RESET})")
        print("5. Voltar para a Torre")
        print("---------------------------------------------")
        try:
            acao = int(input("O que deseja fazer?"))
        except ValueError:
            acao = 0

        if acao == 1:
            if player["ouro"] >=50:
                player["ouro"] -= 50
                player["pocoes"] += 1
                print("")
                print(f"{VERDE}Poção comprada!{RESET}")
                time.sleep(1)
            else:
                print(" ")
                print(f"{VERMELHO}Ouro insuficiente!{RESET}")
                time.sleep(1)

        elif acao == 2:
            if player["ouro"] >= preco_espada:
                player["ouro"] -= preco_espada
                player["bonus_ataque"] += 5
                player["compras_espada"] += 1
                print("")
                print(f"{AZUL}Sua espada esta mais afiada{RESET}, Vá para o combate!")
                time.sleep(2)
            else:
                print("")
                print(f"{VERMELHO}Ouro insuficiente!{RESET}")
                time.sleep(2)

        elif  acao == 3:
            if player["ouro"] >= preco_escudo:
                player["ouro"] -= preco_escudo
                player["bonus_defesa"] += 5
                player["compras_escudo"] += 1
                print("")
                print(f"Você está {AZUL}mais protegido!{RESET}")
                time.sleep(1)
            else:
                print("")
                print(f"{VERMELHO}Ouro insuficiente!{RESET}")
                time.sleep(1)

        elif acao == 4:
            if player["ouro"] >= 100:
                player["ouro"] -= 100
                player["bomba"] += 1
                print("")
                print(f"Você comprou uma {VERMELHO}bomba!{RESET}")
                time.sleep(1)
            else:
                print(" ")
                print(f"{VERMELHO}Ouro insuficiente!{RESET}")
                time.sleep(1)

        elif acao == 5:
            print("")
            print("Saindo...")
            time.sleep(1)
            break
        else:
            print(" ")
            print(f"{VERMELHO}Ação inválida!{RESET} Tente novamente.")
            time.sleep(3)