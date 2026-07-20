import time
from utils import limpa


def loja(player):
    preco_espada = 110 + (player["compras_espada"] * 35)
    preco_escudo = 110 + (player["compras_escudo"] * 35)
    while True:
        limpa()
        print("------------ LOJA SOMBRIA ------------")
        print(f"Seu ouro: {player['ouro']}")
        print("---------------------------------------------")
        print("1. Poção de cura (50 moedas)")
        print("2. Afiar Espada(+5 Dano fixo) (110 Moedas)")
        print("3. Comprar Escudo (+5 Defesa) (110 Moedas)")
        print("4. Comprar Bomba (100 Moedas)")
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
                print("Poção comprada!")
                time.sleep(1)
            else:
                print("Ouro insuficiente!")
                time.sleep(1)

        elif acao == 2:
            if player["ouro"] >= preco_espada:
                player["ouro"] -= preco_espada
                player["bonus_ataque"] += 5
                player["compras_espada"] += 1
                print("")
                print("Sua espada esta mais afiada, Vá para o combate!")
                time.sleep(2)
            else:
                print("Ouro insuficiente!")
                time.sleep(2)

        elif  acao == 3:
            if player["ouro"] >= preco_escudo:
                player["ouro"] -= preco_escudo
                player["bonus_defesa"] += 5
                player["compras_escudo"] += 1
                print("")
                print("Você está mais protegido!")
                time.sleep(1)
            else:
                print("Ouro insuficiente!")
                time.sleep(1)

        elif acao == 4:
            if player["ouro"] >= 100:
                player["ouro"] -= 100
                player["bomba"] += 1
                print("")
                print("Você comprou uma bomba!")
                time.sleep(1)
            else:
                print("Ouro insuficiente!")
                time.sleep(1)

        elif acao == 5:
            print("")
            print("Saindo...")
            time.sleep(1)
            break
        else:
            print("Ação inválida! Tente novamente.")
            time.sleep(3)