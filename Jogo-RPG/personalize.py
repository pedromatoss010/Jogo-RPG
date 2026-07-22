from utils import limpa
from player import criar_player
from cores import BRANCO, MARROM, CIANO, VERMELHO, VERDE, RESET
import time

def personalizando_heroi():
    limpa()
    print("=======================================")    
    print("                HERÓI                  ")
    print("=======================================")
    nome = input("Digite o nome do seu herói: ")
    print(f"Bem-vindo, {nome}!")
    time.sleep(2)
    limpa()

    player = criar_player(nome)

    while True:
        limpa()
        print("=======================================") # ESCOLHER SKIN
        print("       PERSONALIZE SEU HERÓI           ")
        print("=======================================\n")
        print('Escolha a skin do seu herói: ')
        print("1. Skin Vovô Casado")
        print("2. Skin Detetive")
        print("3. Skin Caçador") 
        try:
            roupa = int(input("Qual vai escolher? "))
        except ValueError:
            roupa = 0
        if roupa == 1:
            print(f"{VERDE}PARABÉNS!{RESET} Sua skin é a do Vovô Casado!") 
            player["skin"] = "Vovô Casado"
            time.sleep(2) 
            break
           
        elif roupa == 2:
            print(f"{VERDE}PARABÉNS!{RESET} Sua skin é do Detetive!") 
            player["skin"] = "Detetive"
            time.sleep(2)
            break
        elif roupa == 3:
            print(f"{VERDE}PARABÉNS!{RESET} Sua skin é a do Caçador!")        
            player["skin"] = "Caçador"
            time.sleep(2)
            break
        else:
            print(f"{VERMELHO}NÃO TEMOS ESSA SKIN{RESET}, Escolha uma das opções acima!")
            time.sleep(2)
        
    while True:
        limpa()
        print("=======================================") # ESCOLHER ESPADA
        print("        EQUIPAMENTO DE BATALHA         ")
        print("=======================================")
        print("Escolha sua espada: ")
        print(f"1. {MARROM}Espada de Madeira{RESET}")
        print(f"2. {BRANCO}Espada de Ferro{RESET}")
        print(f"3. {CIANO}Espada de Diamante{RESET}")
        try:
            espada = int(input("Qual espada você quer? "))
        except ValueError:
            espada = 0
            
        print(' ')
        if espada == 1:
            print(f"BOA ESCOLHA! {MARROM}Espada de Madeira{RESET} equipada!")
            player["bonus_ataque"] += 2
            time.sleep(2)
            break
            
        elif espada == 2:
            print(f"ÓTIMA ESCOLHA! {BRANCO}Espada de Ferro{RESET} equipada!")
            player["bonus_ataque"] += 3
            time.sleep(2)
            break
            
        elif espada == 3:
            print(f"EXCELENTE ESCOLHA! {CIANO}Espada de Diamante{RESET}!")
            player["bonus_ataque"] += 4
            time.sleep(2)
            break
            
        else:
            print(f"{VERMELHO}NÃO TEMOS ESSA ESPADA{RESET}, Escolha uma das opções acima!")
            time.sleep(2)

    return player
        
