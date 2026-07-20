from combate import combate
from utils import limpa
from loja import loja
from personalize import personalizando_heroi
from save import existe_save, salvar_player, carregar_player, apagar_save

import time
import random

def main():
    limpa()
    if existe_save():
        while True:
            print("==============================")
            print("     TORRE DO MAGO SOMBRIO    ")
            print("==============================")
            print("1.Carregar Jogo")
            print("2. Novo Jogo")
            opcao = input("O que deseja? ")

            if opcao == "1":
                limpa()
                print("Carregando jogo...")
                time.sleep(2)
                player = carregar_player()
                break
            elif opcao == "2":
                player = personalizando_heroi()
                break
            else:
                print("Ação inválida. Tente novamente!")
                time.sleep(1.5)
                continue 
    else:
        player = personalizando_heroi()

    while player["hp"] > 0:
        limpa()
        print("=======================================") # MENU PRINCIPAL
        print("       A TORRE DO MAGO SOMBRIO         ")
        print("=======================================")
        print(f"Herói: {player['nome']} | Skin: {player['skin']}")
        print(f"HP: {player['hp']}/{player['hp_max']} | Ouro: {player['ouro']} | Poções: {player['pocoes']}")
        print(f"Ataque: +{player['bonus_ataque']} | Vitórias: {player['vitorias']}")
        print(f"Defesa: +{player['bonus_defesa']}")
        print("---------------------------------------")
        print("1. Explorar a Torre")
        print("2. Tomar Poção")
        print("3. Loja do Mercador")
        print("4. Fugir (Sair do jogo)")
        print("5. Salvar Jogo")
        
        try:
            opcao = int(input("O que você deseja fazer? "))
        except:
            opcao = 0 

        match opcao:
            case 1:
                limpa()
                print("Você avança pelos corredores escuros...\n")
                time.sleep(2)
                evento = random.randint(1, 3)

                if evento == 1:
                    moedas = random.randint(30, 60)
                    player["ouro"] += moedas
                    print(f"Você achou algumas {moedas} moedas de ouro no chão.")
                    time.sleep(2)

                elif evento == 2:
                    combate(player)
                    time.sleep(1)

                else:
                    print("Tudo silencioso por aqui...")
                    time.sleep(2)
            case 2:
                limpa()
                if player["hp"] == player["hp_max"]:
                    print("Vida cheia!")
                    time.sleep(1)
                else:
                    if player["pocoes"] > 0:
                        player["pocoes"] -= 1
                        cura = int(player["hp_max"] * 0.2)
                        player["hp"] = min(player["hp_max"], player["hp"] + cura)
                        print("Você recuperou vida!")
                    else:
                        print("Sem poções! Vá até a loja.")
                    time.sleep(2)
            case 3:
                loja(player)
            
            case 4:
                limpa()
                while True:
                    resposta = input("Tem certeza que deseja fugir da torre? Você perderá todo seu progresso no jogo(Responda com S/N): ").strip().upper()

                    if resposta == "S":
                        print(f"Você fugiu da torre com {player['ouro']} moedas de ouro. Covarde, porém vivo!")
                        time.sleep(3)
                        apagar_save()
                        return
                    elif resposta == "N":
                        print("Voltando para o Menu...")
                        time.sleep(1.5)   
                        break
                    else:
                        print("Resposta Inválida!")  
                        continue                      
            case 5:
                salvar_player(player)
                limpa()
                print("Jogo salvo com sucesso!")
                time.sleep(1.5)
            case _:
                print("Ação inválida!")
                time.sleep(1)
    limpa()
    print("=======================================")
    print("              GAME OVER                ")
    print("=======================================")
    print(f"Seu herói, {player['nome']}, caiu na Torre do Mago Sombrio...")
    print(f"Vitórias conquistadas: {player['vitorias']}")
    print(f"Ouro acumulado: {player['ouro']}")
    print("=======================================")
    time.sleep(4)
    apagar_save()

if __name__ == "__main__":
    main()